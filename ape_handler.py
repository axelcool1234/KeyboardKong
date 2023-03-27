# ape_handler.py
# Module handles API search requests for Monkey Type.
import json
import urllib.parse
import urllib.request

BASE_MONKEYTYPE_URL = 'https://api.monkeytype.com/'

def generate_response(APE_KEY: str, request: tuple) -> dict:
    url = build_search_url(request[0], request[1])
    response = get_result(url,APE_KEY)
    return response

def build_search_url(query_parameters: dict, search_type: str) -> str:
    return f'{BASE_MONKEYTYPE_URL}{search_type}?{urllib.parse.urlencode(query_parameters)}'

def get_result(url: str, APE_KEY: str) -> dict:
    response = None
    header = {'Authorization': 'ApeKey '+APE_KEY,
              'User-Agent': 'KeyboardKong'}
    try:
        request = urllib.request.Request(url, method='GET', headers = header)
        response = urllib.request.urlopen(request)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)
    finally:
        if response != None:
            response.close()