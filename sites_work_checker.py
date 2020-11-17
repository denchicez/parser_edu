import requests
import validators

def urlChecker(url):
    if not validators.url(url):
        return False
    r = requests.head(url)
    return r.status_code == 200

