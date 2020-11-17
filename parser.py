#pip install beautifulsoup4
#pip install requests
from bs4 import BeautifulSoup
import requests
import csv
import json
import os
import subprocess, sys
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'accept': '*/*'}
HOST = 'http://dop.edu.ru'
URL = "http://dop.edu.ru/organization/list?orientation=3,4&page=1&perPage=999999"
def get_html(url):
    r = requests.get(url, headers=HEADERS, params=None)
    return r
def get_content(organization):
    full_name=organization['full_name']
    short_name=organization['name']
    url_name=str(organization['site_url'])
    org_id=organization['id']
    if(full_name==''):
        full_name="NOT FOUND"
    if(short_name==''):
        short_name="NOT FOUND"
    if(url_name==''):
        url_name="NOT FOUND"
    organizationsss.append({
            'Полное наименование организации (по уставу)': full_name,
            'Краткое наименование организации': short_name,
            'Адрес сайта': url_name,
            'id': org_id
    })
x=get_html(URL).text
data = json.loads(x)
organizationsss=[]
for organization in data["data"]["list"]:
    get_content(organization)
with open('org.csv', 'w', newline="") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Полное наименование организации (по уставу)', 'Краткое наименование организации', 'Адрес сайта','id'])
    for organizat in organizationsss:
        organizat['Адрес сайта']=organizat['Адрес сайта'].replace('\u200b','')
        writer.writerow([organizat['Полное наименование организации (по уставу)'], organizat['Краткое наименование организации'], organizat['Адрес сайта'], organizat['id']])
opener ="open" if sys.platform == "darwin" else "xdg-open"
subprocess.call([opener, 'org.csv'])
