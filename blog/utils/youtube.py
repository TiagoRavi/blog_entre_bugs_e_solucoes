import re


def extract_youtube_id(value: str) -> str | None:
    """
    Extrai o ID do vídeo do YouTube a partir de uma URL ou retorna
    o valor se já parecer um ID válido.
    """
    if not value:
        return None

    value = value.strip()

    paterns = (
        r"youtu\.be/(?P<id>[^/?&]+)",
        r"youtube\.com/watch\?v=(?P<id>[^&]+)",
        r"youtube\.com/embed/(?P<id>[^/?&]+)",
        r"youtube\.com/shorts/(?P<id>[^/?&]+)",
    )

    for patern in paterns:
        match = re.search(patern, value)
        if match:
            return match.group("id")

    # Fallback: se já for um ID válido (11 caracteres)
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", value):
        return value

    return None
