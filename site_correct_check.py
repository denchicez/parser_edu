# This Python file uses the following encoding: utf-8
from bs4 import BeautifulSoup
import requests as req
    
def get_lower(string): # лучше метода не нашёл
    small = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    big = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    alpha = {}
    for i in range(len(big)):
        alpha[big[i]] = small[i]
    res = ''
    for c in string:
        if (alpha.get(c) != None):
            print(c, alpha.get(c))
            res = res + alpha.get(c)
        else:
            res = res + c
    return res
    

def is_site_correct(url, name):
    html = ''
    try:
        resp = req.get(url)
        html = resp.text
    except:
        return False

    # сюда бы нежный славный декодер html
    # дальше я считаю что html и name в норм кодировке и работаю с ними
    name = get_lower(name)
    html = get_lower(html)
    trans = '[0123456789.,!@\"#№;$%^:&?*()\'\\/|' # 'плохие' символы
    for c in trans:
        name = name.replace(c, '') # убираем их
    words = name.split() # делим на слова
    buff = []
    for word in words:
        if (len(word) > 2):
            buff.append(word) # удаляем короткие
    words = buff
    count = 0
    try:
        for word in words:
            if html.find(word) != -1: # ищем
                count += 1
    except:
        return False    
    if count > 0: # !тут надо подумать как лучше
        return True
    return False;

# print(get_lower('Красноярский краевой Дворец пионеров'))
    
# print(is_site_correct('https://www.dvpion.ru', 'Красноярский краевой Дворец пионеров'))
