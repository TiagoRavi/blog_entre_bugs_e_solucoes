
import logging
from urllib.parse import urljoin, urlparse

import requests

logger = logging.getLogger(__name__)

INDEXNOW_KEY = "b7360389d77240f3940b63ae081517d9"
HOST = "entrebugsesolucoes.com.br"
BASE_URL = f"https://{HOST}"
KEY_LOCATION = f"{BASE_URL}/{INDEXNOW_KEY}.txt"


def submit_to_indexnow(urls: list[str]):
    endpoint = "https://api.indexnow.org/IndexNow"

    absolute_urls = [urljoin(f"{BASE_URL}/", url) for url in urls]

    # Não enviar URLs de outro host por engano.
    for url in absolute_urls:
        parsed = urlparse(url)

        if parsed.scheme != "https" or parsed.hostname != HOST:
            logger.warning("IndexNow ignorado: URL inválida para o host: %s", url)
            return None, "URL inválida ou host divergente"

    if not absolute_urls:
        return None, "Nenhuma URL informada"

    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": absolute_urls,
    }

    try:
        response = requests.post(endpoint, json=payload, timeout=10)

        if response.status_code not in (200, 202):
            logger.warning(
                "IndexNow falhou: status=%s, resposta=%s, URLs=%s",
                response.status_code,
                response.text,
                absolute_urls,
            )

        return response.status_code, response.text

    except requests.RequestException:
        logger.exception("Erro ao enviar URLs para IndexNow")
        return None, "Falha na requisição HTTP"
