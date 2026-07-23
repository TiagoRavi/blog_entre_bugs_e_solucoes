import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

SECTION_TITLES = {
    "introdução",
    "conclusão",
    "considerações finais",
    "resumo",
    "próximos passos",
}

CALLOUT_EMOJIS = r"[⚠️👉🔹✅❌💡🧠🚀🎯]"


def strip_emoji(text: str) -> str:
    """Remove emojis do início da linha para análise semântica"""
    return re.sub(r"^[\W_]+", "", text).strip()


@register.filter(name="text_to_html")
def text_to_html(text):
    if not text:
        return ""

    lines = text.splitlines()
    html = []
    in_list = False

    for raw_line in lines:
        line = raw_line.strip()

        # Linha vazia
        if not line:
            if in_list:
                html.append("</ul>")
                in_list = False
            continue

        clean = strip_emoji(line).lower()

        # 🔹 Callout / Destaque (emoji + texto, não é título)
        if (
            re.match(rf"^{CALLOUT_EMOJIS}", line)
            and not clean.endswith("?")
            and not clean.endswith(":")
        ):
            if in_list:
                html.append("</ul>")
                in_list = False
            html.append(f"<p><strong>{line}</strong></p>")
            continue

        # 🔹 H2 — Títulos fixos (Introdução, Conclusão etc.)
        if clean in SECTION_TITLES:
            if in_list:
                html.append("</ul>")
                in_list = False
            html.append(f"<h2>{line}</h2>")
            continue

        # 🔹 H2 — Perguntas ou títulos com :
        if clean.endswith("?") or (clean.endswith(":") and len(clean) < 90):
            if in_list:
                html.append("</ul>")
                in_list = False
            html.append(f"<h2>{line}</h2>")
            continue

        # 🔹 H2 — Numeração (1. 2. 3.)
        if re.match(r"^\d+\.\s+", clean):
            if in_list:
                html.append("</ul>")
                in_list = False
            html.append(f"<h2>{line}</h2>")
            continue

        # 🔹 Lista
        if re.match(r"^[-•*]\s+", line):
            if not in_list:
                html.append("<ul>")
                in_list = True
            item = re.sub(r"^[-•*]\s+", "", line)
            html.append(f"<li>{item}</li>")
            continue

        # 🔹 Parágrafo padrão
        if in_list:
            html.append("</ul>")
            in_list = False

        html.append(f"<p>{line}</p>")

    if in_list:
        html.append("</ul>")

    return mark_safe("\n".join(html))
