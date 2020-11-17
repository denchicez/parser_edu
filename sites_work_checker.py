import requests
import validators

def urlChecker(url):
    try:
        if not validators.url(url):
            return False
    except:
        return False
    try:
        r = requests.head(url)
        return r.status_code == 200
    except:
        return False
