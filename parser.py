#pip install beautifulsoup4
#pip install requests
from bs4 import BeautifulSoup
import requests
import csv
import json
import os
import subprocess, sys
URL = 'http://dop.edu.ru/contingent/institution/placesList?region=42'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'accept': '*/*'}
HOST = 'http://dop.edu.ru'
FILE = 'cars.csv'

def get_html(url):
    r = requests.get(url, headers=HEADERS, params=None)
    return r
def get_content(id):
    URL_NEW='http://dop.edu.ru/organization/view/'+str(id)
    html=get_html(URL_NEW).text
    soup = BeautifulSoup(html, 'html.parser')
    stroka=html
    proverka=stroka.find("Техническая направленность:",0,len(stroka))
    if(not(proverka is None) and proverka!=-1):
        full_name=soup.find(title="Полное наименование организации (по уставу)")
        if(not(full_name is None)):
            full_name=soup.find(title="Полное наименование организации (по уставу)").get_text()
        else:
            full_name="ERROR"
        short_name=soup.find(title="Краткое наименование организации")
        if(not(short_name is None)):
            short_name=soup.find(title="Краткое наименование организации").get_text()
        else:
            short_name="ERROR"
        url_name=soup.find(title="Адрес сайта")
        if(not(url_name is None)):
            url_name=soup.find(title="Адрес сайта").get_text()
        else:
            url_name="ERROR"
        organizationsss.append({
                'Полное наименование организации (по уставу)': full_name,
                'Краткое наименование организации': short_name,
                'Адрес сайта': url_name
        })
x=get_html(URL).text
data = json.loads(x)
organizationsss=[]
for organization in data["data"]["list"]:
    id_organization=organization["id"]
    get_content(id_organization)
with open('org.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Полное наименование', 'Краткое наименование', 'Адрес сайта'])
    for organizat in organizationsss:
        writer.writerow([organizat['Полное наименование организации (по уставу)'], organizat['Краткое наименование организации'], organizat['Адрес сайта']])
opener ="open" if sys.platform == "darwin" else "xdg-open"
subprocess.call([opener, 'org.csv'])
