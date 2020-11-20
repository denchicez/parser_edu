from bs4 import BeautifulSoup
import requests
import json
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0', 'accept': '*/*'}
HOST = 'http://dop.edu.ru'
URL = "http://dop.edu.ru/organization/list?page=0&perPage=999999"
def get_html(url): # делаем запрос на html страничку
    try:
        r = requests.get(url, headers=HEADERS, params=None)
        return r
    except:
        print('SOME TROUBLE WITH INTERNET') #не смогли сделать запрос т.к. произошла ошибка с связью
def InstFollowers(url_name):
    url_name=url_name+'?__a=1'
    HTML2=get_html(url_name).text
    data = json.loads(HTML2)
    return(data['graphql']['user']['edge_followed_by']['count'])
    
    
    
#inst_link='https://www.instagram.com/_f3dorov_/'
#print(InstFollowers(inst_link))
#inst_link='https://www.instagram.com/denchicez/'
#print(InstFollowers(inst_link))
