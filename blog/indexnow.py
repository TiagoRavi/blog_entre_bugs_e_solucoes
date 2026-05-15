import requests

INDEXNOW_KEY = "b7360389d77240f3940b63ae081517d9"
HOST = "entrebugsesolucoes.com.br"
KEY_LOCATION = f"https://{HOST}/{INDEXNOW_KEY}.txt"

def submit_to_indexnow(urls: list[str]):
    endpoint = "https://api.indexnow.org/IndexNow"

    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }

    response = requests.post(endpoint, json=payload, timeout=10)
    return response.status_code, response.text
