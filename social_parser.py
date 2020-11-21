from bs4 import BeautifulSoup
import requests
import json
import vk
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0', 'accept': '*/*'}
HOST = 'http://dop.edu.ru'
URL = "http://dop.edu.ru/organization/list?page=0&perPage=999999"
def get_html(url): # делаем запрос на html страничку
    try:
        r = requests.get(url, headers=HEADERS, params=None)
        return r
    except:
        print('SOME TROUBLE WITH INTERNET') #не смогли сделать запрос т.к. произошла ошибка с связью
def find_number(index,string): # ищем следующее число после строки
    KolKov=0
    stroka=''
    for i in range(index,len(string)):
        if(string[i]==chr(34)):
            KolKov+=1
        if(KolKov==5):
            break
        if(KolKov==4 and string[i]!=chr(34)):
            stroka=stroka+string[i]
    return stroka
def YoutubeFollowers(url):
    try:
        HTML2=get_html(url).text
        soup=str(BeautifulSoup(HTML2,'html.parser'))
        ind = soup.find('subscriberCountText')
        if(ind==-1):
            return 0
        else:
            return (find_number(ind,soup))
    except:
        return 0
def get_true_followers(s):
    s=str(s)
    s = s.replace(',', '.')
    s = s.replace(chr(160), ' ')
    if (s.find('млн подписчиков') != -1):
        s = s.replace(' млн подписчиков', '')
        return int(float(s) * 1000000)
    if (s.find(' тыс. подписчиков') != -1):
        s = s.replace(' тыс. подписчиков', '')
        return int(float(s) * 1000)
    s = s.replace(' подписчиков', '')
    s = s.replace(' подписчика', '')
    s = s.replace(' подписчик', '')    
    return int(float(s))
def VKFollowers(url_name):
    if(url_name.find('public')!=-1):
        try:
            id_of_group=(url_name[21:])
            podpisota = vk_api.groups.getMembers(group_id=id_of_group, v=5.92)['count']
        except:
            podpisota=0
    elif(url_name.find('club')!=-1):
        try:
            id_of_group=(url_name[19:])
            podpisota = vk_api.groups.getMembers(group_id=id_of_group, v=5.92)['count']
        except:
            podpisota=0
    else:
        try:
            id_of_group=url_name[15:]
            podpisota = vk_api.groups.getMembers(group_id=id_of_group, v=5.92)['count']
        except:
            podpisota=0
    return podpisota
def InstFollowers(url_name):
    try:
        url_name=url_name+'?__a=1'
        HTML2=get_html(url_name).text
        data = json.loads(HTML2)
        return(data['graphql']['user']['edge_followed_by']['count'])
    except:
        return 0
def get_social_links(links):
    prefixes = [['https://www.youtube.com/c/', 'https://www.youtube.com/channel/', 'https://www.youtube.com/user/'], ['https://vk.com/'], ['https://www.instagram.com/']]
    youtube = []
    vk = []
    inst = []
    for link in links:
        for i in range(len(prefixes)):
            val = ''
            for media in prefixes[i]:
                if (link.find(media) != -1):
                    val = link
            if (len(val) != 0):
                if(i==0):
                    youtube.append(val)
                if(i==1):
                    vk.append(val)
                if(i==2):
                    inst.append(val)                
    result = []
    if (len(youtube) != 0):
        val = -1
        for link in youtube:
            follow = get_true_followers(YoutubeFollowers(link))
            if (follow > val):
                val = follow
        youtube_count = val
    if (len(vk) != 0):
        val = -1
        for link in vk:
            follow = VKFollowers(link)
            if (follow > val):
                val = follow
        vk_count=val
    if (len(inst) != 0):
        val = -1
        for link in inst:
            follow = InstFollowers(link) 
            if (follow > val):
                val = follow
        inst_count = val
    return youtube_count,vk_count,inst_count
token = "3fb7074e3fb7074e3fb7074e373fc20ea433fb73fb7074e6000a2640396190c4d381005"  # Сервисный ключ доступа
session = vk.Session(access_token=token)
vk_api = vk.API(session)
#my_links = {'https://www.instagram.com/_egor.bocharov/','https://www.youtube.com/c/Spoontamerfw', 'https://vk.com/countryballs_re','https://petux.com', 'https://www.youtube.com/c/Spoontamer'}
#print(get_social_links(my_links))
