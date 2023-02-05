import requests as req

def get_response() -> int:
    return req.get('https://www.google.co.kr/').status_code
