from bs4 import BeautifulSoup
import requests as req
    
def is_site_correct(url, name):
    html = ''
    try:
        resp = req.get(url)
        html = resp.text
    except:
        return False
    trans = '[0123456789.,!@\"#№;$%^:&?*()\'\\/|'
    for c in trans:
        name = name.replace(c, '')
    words = name.split()
    buff = []
    for word in words:
        if (len(word) > 2):
            buff.append(word)
    words = buff
    count = 0
    try:
        for word in words:
            if html.find(word) != -1:
                count += 1
    except:
        return False    
    print(html)
    if count >= len(words) / 3:
        return True
    return False;
    
# print(is_site_correct('https://www.dvpion.ru', 'Красноярский краевой Дворец пионеров'))