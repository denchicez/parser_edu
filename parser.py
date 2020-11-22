#pip install beautifulsoup4
#pip install requests
#pip install validators
from bs4 import BeautifulSoup
import vk
import requests
import csv
import sys
import validators
import urllib.request
import json
import time
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0', 'accept': '*/*'}
HOST = 'http://dop.edu.ru'
URL = "http://dop.edu.ru/organization/list?page=0&perPage=999999"
def getVariantsOfWords(word): # получаем слово в нормальной кодировке]
    trans = '[]{}0123456789.,!@\"#№;$%^:&?*()\'\\/|' # 'плохие' символы
    for c in trans:
        word = word.replace(c, '') # убираем их
    small = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    big = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    enSmall = 'abcdefghijklmnopqrstuvwxyz'
    enBig = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphaToSmall = {}
    alphaToBig = {}
    for i in range(len(big)):
        alphaToSmall[big[i]] = small[i]
        alphaToBig[small[i]] = big[i]
    for i in range(len(enBig)):
        alphaToSmall[enBig[i]] = enSmall[i]
        alphaToBig[enSmall[i]] = enBig[i]    
    res = ''
    words = []
    for c in word:
        if (alphaToSmall.get(c) != None):
            res = res + alphaToSmall.get(c)
        else:
            res = res + c
    words.append(res)
    if (len(res) > 0 and alphaToBig.get(res[0]) != None):
        res = alphaToBig.get(res[0]) + res[1:]
    words.append(res)
    res = ''
    for c in word:
        if (alphaToBig.get(c) != None):
            res = res + alphaToBig.get(c)
        else:
            res = res + c
    words.append(res)
    return words # возвращаем маленькими, с большой, большие
def get_html(url): # делаем запрос на html страничку
    try:
        r = requests.get(url, headers=HEADERS, params=None)
        return r
    except:
        print('SOME TROUBLE WITH INTERNET') #не смогли сделать запрос т.к. произошла ошибка с связью
        with open('org.csv', 'w', newline="") as file: #cохраняем то что имеем.
            writer = csv.writer(file, delimiter=',')
            writer.writerow(['Адрес организации','Номер телефона орагнизации','Номер дополнительного телефона орагнизации','email aдрес',
                             'Адрес сайта','Работает ли сайт?','title сайта организации','description сайта организации','keywords сайта организации',
                             'Cайт принадлежит организации?','Количество подписчиков Instagramm','Количество подписчиков VK','Количество подписчиков youtube','id региона','Полное наименование об организации (по уставу)','Краткое наименование организации','Дата создания организации',
                             'Юридическое лицо / Филиал','Общее количество сотрудников','Субъект РФ','Тип организации','Количество занимающихся детей',
                             'Количество занимающихся детей художественной направленностью','Количество занимающихся детей естественно-научной направленностью',
                             'Количество занимающихся детей технической направленностью','Количество занимающихся детей социально-педагогической направленностью',
                             'Количество занимающихся детей физкультурно-спортивной направленностью','Количество занимающихся детей туристической направленностью',
                             'Количество занимающихся детей интеллектуально игровой направленностью','Фактическая наполняемость','Количество педагогов',
                             'Количество педагогов художественной направленности' ,'Количество педагогов естественно-научной направленности',
                             'Количество педагогов технической направленности' ,'Количество педагогов социально-педагогической направленности' ,
                             'Количество педагогов физкультурно-спортивной направленности' ,'Количество педагогов туристической направленности',
                             'Количество педагогов интеллектуально игровой направленности','okfs','okopf','ogrn','inn','Номер бланка лицензии','Кем выдана лицензии','Cрок лицензии',
                             'id','Техническое','Естественнонаучная'])
            for organizat in organizationsss:
                organizat['Адрес сайта']=organizat['Адрес сайта'].replace('\u200b','')
                try:
                    writer.writerow([organizat['Адрес организации'],organizat['Номер телефона орагнизации'],organizat['Номер дополнительного телефона орагнизации'],organizat['email aдрес'],organizat['Адрес сайта'],organizat['Работает ли сайт?'],organizat['title сайта организации'],organizat['description сайта организации'],organizat['keywords сайта организации'],organizat['Cайт принадлежит организации?'],organizat['Количество подписчиков Instagramm'],organizat['Ссылки на соц. сети в Instagramm'],organizat['Количество подписчиков VK'],organizat['Ссылки на соц. сети в VK'],organizat['Количество подписчиков youtube'],organizat['Ссылки на соц. сети в youtube'],organizat['id региона'],organizat['Полное наименование организации (по уставу)'],organizat['Краткое наименование организации'],organizat['Дата создания организации'],organizat['Юридическое лицо / Филиал'],organizat['Общее количество сотрудников'],organizat['Субъект РФ'],organizat['Тип организации'],organizat['Количество занимающихся детей'],organizat['Количество занимающихся детей художественной направленностью'],organizat['Количество занимающихся детей естественно-научной направленностью'],organizat['Количество занимающихся детей технической направленностью'],organizat['Количество занимающихся детей социально-педагогической направленностью'],organizat['Количество занимающихся детей физкультурно-спортивной направленностью'],organizat['Количество занимающихся детей туристической направленностью'],organizat['Количество занимающихся детей интеллектуально игровой направленностью'],organizat['Фактическая наполняемость'],organizat['Количество педагогов'],organizat['Количество педагогов художественной направленности'],organizat['Количество педагогов естественно-научной направленности'],organizat['Количество педагогов технической направленности'],organizat['Количество педагогов социально-педагогической направленности'],organizat['Количество педагогов физкультурно-спортивной направленности'],organizat['Количество педагогов туристической направленности'],organizat['Количество педагогов интеллектуально игровой направленности'],organizat['okfs'],organizat['okopf'],organizat['ogrn'],organizat['inn'],organizat['Номер бланка лицензии'],organizat['Кем выдана лицензии'],organizat['Cрок лицензии'],organizat['id'],organizat['Техническое'],organizat['Естественнонаучная']])
                except:
                    writer.writerow([organizat['Адрес организации'],organizat['Номер телефона орагнизации'],organizat['Номер дополнительного телефона орагнизации'],organizat['email aдрес'],organizat['Адрес сайта'],organizat['Работает ли сайт?'],'Неизвестная кодировка','Неизвестная кодировка','Неизвестная кодировка',organizat['Cайт принадлежит организации?'],organizat['Количество подписчиков Instagramm'].organizat['Ссылки на соц. сети в Instagramm'],organizat['Количество подписчиков VK'],organizat['Ссылки на соц. сети в VK'],organizat['Количество подписчиков youtube'],organizat['Ссылки на соц. сети в youtube'],organizat['id региона'],organizat['Полное наименование организации (по уставу)'],organizat['Краткое наименование организации'],organizat['Дата создания организации'],organizat['Юридическое лицо / Филиал'],organizat['Общее количество сотрудников'],organizat['Субъект РФ'],organizat['Тип организации'],organizat['Количество занимающихся детей'],organizat['Количество занимающихся детей художественной направленностью'],organizat['Количество занимающихся детей естественно-научной направленностью'],organizat['Количество занимающихся детей технической направленностью'],organizat['Количество занимающихся детей социально-педагогической направленностью'],organizat['Количество занимающихся детей физкультурно-спортивной направленностью'],organizat['Количество занимающихся детей туристической направленностью'],organizat['Количество занимающихся детей интеллектуально игровой направленностью'],organizat['Фактическая наполняемость'],organizat['Количество педагогов'],organizat['Количество педагогов художественной направленности'],organizat['Количество педагогов естественно-научной направленности'],organizat['Количество педагогов технической направленности'],organizat['Количество педагогов социально-педагогической направленности'],organizat['Количество педагогов физкультурно-спортивной направленности'],organizat['Количество педагогов туристической направленности'],organizat['Количество педагогов интеллектуально игровой направленности'],organizat['okfs'],organizat['okopf'],organizat['ogrn'],organizat['inn'],organizat['Номер бланка лицензии'],organizat['Кем выдана лицензии'],organizat['Cрок лицензии'],organizat['id'],organizat['Техническое'],organizat['Естественнонаучная']])
        return sys.exit()
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
    
def get_links_from_page(url):
    links = set()
    try:
        resp = urllib.request.urlopen(url)
        soup = BeautifulSoup(resp, 'html.parser')
    except:
        return links
    try:
        for link in soup.find_all('a', href=True):
            links.add(link['href'])
    except:
        return links
    return links


def voidless(per): #проверка пустоты строчки
    if(per=='' or per==None or per==' '):
        return('Неизвестно')
    else:
        return(per)
def count_predkov(string,start,html):
    last=0
    tmp=html.find(string,start,len(html))
    if(html[tmp+len(string)+1].isdigit()==False):
        tmp=html.find(string,tmp+len(string)+1,len(html))
    if(tmp!=-1):
        last=tmp+len(string)+1
        counter=find_number(tmp+len(string),html)
    else:
        counter=0
    return counter,last
def get_api_of(name): #возвращает значение для name из json файла инфы об организации
    try:
        tmp=organization[name]
        tmp=voidless(tmp)
    except:
        tmp='Неизвестно'
    return tmp
def get_parse_of(supchik,stringfind):
    try:
        name=supchik.find(title=stringfind).text
        name=voidless(name)
    except:
        name='Не известно'
    return name
def urlChecker(url): #работает ли сайт?
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
def find_number(index,string): # ищем следующее число после строки
    check=0
    ch=0
    for i in range(index,len(string)):
        if(not(string[i].isdigit()) and not(string[i]==' ')):
            break
        if(check==1 and not((string[i].isdigit()))):
            break
        if(check==1):
            ch=ch*10+ord(string[i])-ord('0')
        if(check==0 and string[i].isdigit()):
            check=1
            ch=ord(string[i])-ord('0')
    return ch
def find_number_youtube(index,string): # ищем следующее число после строки
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
def NameCheck(string,code1,code2): #Можно ли расшифровать stirng с помощью code1 и code2
    letters = ['<','>','«','»',chr(9),chr(13),chr(10),'(',')','|',':',' ',chr(34),'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','а','a','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я','-','+',',','.','/','[',']','1','2','3','4','5','6','7','8','9','0','#','№','-','—','_','=','}','{','+','!','?','#']
    try:
        string=string.encode(code1).decode(code2) #декодируем если можно
    except:
        return False # выходим
    try:
        string=string.lower() # пытаемся сделать нижний регистр
    except:
        string=string
    for delite_symbole in letters: #удаляем символы
        string=string.replace(delite_symbole,'')
    if(len(string)>2): #Если длина остатков больше 2 выходим
        return False
    else:
        return True #все верно
    
def decode(string):
    all_code = ['UTF-8','cp1251','latin1'] #возможные виды кодировок
    chk=0
    for code_in_all1 in all_code:
        for code_in_all2 in all_code:
            if(NameCheck(string,code_in_all1,code_in_all2)==True):
                code1=code_in_all1
                code2=code_in_all2
                chk=1
                break
        if(chk==1): #если нашлась кодировка 
            string=string.encode(code1).decode(code2) #декодируем
            return string,code1,code2
    return 'У сайта неизвестная кодировка','UTF-8', 'UTF-8'
def is_site_correct(html_str, all_names,code1,code2):
    allwords=getVariantsOfWords(all_names)
    for name in allwords:
        trans = '[]{}0123456789.,!@\"#№;$%^:&?*()\'\\/|' # 'плохие' символы
        for c in trans:
            name = name.replace(c, '') # убираем их
        try:
            name=name.encode(code2).decode(code1) #кодируем в кодировку сайта
        except:
            return False
        words = name.split() # делим на слова
        buff = []
        for word in words:
            if (len(word) > 2):
                buff.append(word) # удаляем короткие, добовляем хорошие
        words = buff
        try:
            for word in words:
                if html_str.find(word) != -1: # ищем
                    return True
        except:
            return False
    return False
def YoutubeFollowers(url):
    try:
        HTML_youtube=get_html(url).text
        soup_youtube=str(BeautifulSoup(HTML_youtube,'html.parser'))
        ind = soup_youtube.find('subscriberCountText')
        if(ind==-1):
            return 0
        else:
            return (find_number_youtube(ind,soup_youtube))
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
    try:
        return int(float(s))
    except:
        return 0
def get_social_links(links):
    prefixes = [['https://www.youtube.com/channel/','http://www.youtube.com/', 'https://www.youtube.com/user/','https://www.youtube.com/c/'], ['https://vk.com/'], ['https://www.instagram.com/']]
    youtube = []
    youtube_links=set()
    vk = []
    vk_links=set()
    inst = []
    inst_links=set()
    youtube_count=0
    vk_count=0
    inst_count=0
    for link in links:
        for i in range(len(prefixes)):
            val = ''
            for media in prefixes[i]:
                if (link.find(media) != -1):
                    val = link
            if(len(val)!=0):
                if(i==0):
                    youtube_links.add(link)
                    youtube.append(val)
                if(i==1):
                    vk_links.add(link)
                    vk.append(val)
                if(i==2):
                    inst_links.add(link)
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
    return youtube_count,vk_count,inst_count,youtube_links,vk_links,inst_links


def get_content(organization): #узнаем все параметры организации
    try:
        techno=organization['orientation_name'].find('Техническая',0,len(organization['orientation_name']))
    except:
        techno=-1
    try:
        estestv=organization['orientation_name'].find('Естественнонаучная',0,len(organization['orientation_name']))
    except:
        estestv=-1
        
    if(techno<0):
        techno=False
    else:
        techno=True
    if(estestv<0):
        estestv=False
    else:
        estestv=True
    if(estestv==1 or techno==1):
        global count
        print(count,'/ 1562')
        count=count+1
        org_id=organization['id']
        HTML=get_html(HOST+'/organization/view/'+str(org_id)).text
        soup=BeautifulSoup(HTML,'html.parser')
        #находит полное наименование
        full_name=get_api_of('full_name')
        #находит краткое наименование         
        short_name=get_api_of('name')
        #находит адресс
        adress=get_api_of('origin_address')
        #находит телефон
        phone=get_api_of('phone')
        #находит дополнительный телефон
        phone_add=get_api_of('phone_add')
        #находит email
        email=get_api_of('email')
        url_name=get_api_of('site_url')
        #Работает ли сайт? + дополнение и исправление расширение сайта(http,www,https)
        try:
            if(url_name=='Неизвестно'):
                site_is_work=False
            else:
                if(urlChecker(url_name)==False):    
                    if(url_name[:4]!='http'):
                        url_name='http://'+url_name
                    site_is_work=urlChecker(url_name)
                    if(site_is_work==False):
                        if(url_name[:5]=='http:'):
                            url_name= 'https'+url_name[4-(len(url_name)):]
                            site_is_work=urlChecker(url_name)
                else:
                    site_is_work=True
        except:
            site_is_work=False
        podpis_inst='Нет аккаунта'
        podpis_vk='Нет аккаунта'
        podpis_youtube='Нет аккаунта'
        links_youtube='Нет аккаунта'
        links_vk='Нет аккаунта'
        links_inst='Нет аккаунта'
        #парсинг title, keywords, description           
        if(site_is_work==True):
            HTML2=get_html(url_name).text
            soup2=BeautifulSoup(HTML2,'html.parser') 
            all_code = ['UTF-8','cp1251','latin1'] #возможные виды кодировок
            try:
                title_org_site=((soup2.find('head')).find('title')).text #title с кодировкой сайта 
                title_org_site,code1,code2 = decode(title_org_site)
                site_correct=is_site_correct(url_name,full_name,code1,code2)
            except:
                code1='UTF-8'
                code2='UTF-8'
                title_org_site='Не найдено' 
                site_correct='False'
            if(title_org_site!='У сайта неизвестная кодировка' and title_org_site!='Не найдено'):
                #парсинг description сайта c декодировкой
                podpis_youtube,podpis_vk,podpis_inst, youtubes,vks,insts=social_links=get_social_links(get_links_from_page(url_name))
                if(podpis_youtube==0):
                    podpis_youtube='Нет аккаунта'
                else:
                    links_youtube=youtubes 
                if(podpis_vk==0):
                    podpis_vk='Нет аккаунта'
                else:
                    links_vk=vks 
                if(podpis_inst==0):
                    podpis_inst='Нет аккаунта'
                else:
                    links_inst=insts
                try:
                    description_org_site=soup2.find(attrs={"name":"description"})
                    description_org_site=str(description_org_site)
                    description_org_site = BeautifulSoup(description_org_site, 'html.parser')
                    description_org_site=description_org_site.meta['content']
                    description_org_site=description_org_site.encode(code1).decode(code2)
                except:
                    description_org_site='Не найдено'
                if(description_org_site==''):
                    description_org_site='Отсутсвует'
                #парсинг keywords сайта c декодировкой
                try:
                   keywords_org_site=soup2.find(attrs={"name":"keywords"})
                   keywords_org_site=str(keywords_org_site)
                   keywords_org_site = BeautifulSoup(keywords_org_site, 'html.parser')
                   keywords_org_site=keywords_org_site.meta['content']
                   keywords_org_site=keywords_org_site.encode(code1).decode(code2)
                except:
                    keywords_org_site='Не найдено'
                if(keywords_org_site==''):
                    keywords_org_site='Отсутсвует'
                site_correct=is_site_correct(HTML2,full_name,code1,code2)
                    
            #неизвестная кодировка сайта
            else:
                site_correct='False'
                title_org_site='Cайт не работает или не существует'
                description_org_site='У сайта неизвестная кодировка'
                keywords_org_site='У сайта неизвестная кодировка'
        else:
            site_correct='False'
            title_org_site='Cайт не работает или не существует'
            description_org_site='Cайт не работает или не существует'
            keywords_org_site='Cайт не работает или не существует'
        #находит id региона
        region_id=get_api_of('region_id')
        #находит год создания
        year_create=get_parse_of(soup,'Дата создания организации')
        #находит Юридическое лицо/Филиал
        filial=get_parse_of(soup,'Юридическое лицо / Филиал')
        #находит количество сотрудников
        all_personal=get_parse_of(soup,'Общее количество сотрудников')
        #находит название региона 
        name_region=get_parse_of(soup,'Субъект РФ')
        #находит тип организации
        type_organ=get_api_of('institution_type_name')
        #находит фактическую наполняемость
        fact_napoln=get_parse_of(soup,'Фактическая наполняемость')
        #находит ОКФС     
        okfs=get_api_of('okfs')
        #Находит ОКОПФ
        okopf=get_api_of('okopf')
        #находит ОГРН     
        ogrn=get_api_of('ogrn')
        #Находит ИНН
        inn=get_api_of('inn')
        #
        number_license=get_parse_of(soup,'Номер бланка лицензии')
        give_license=get_parse_of(soup,'Кем выдана лицензия')
        srok_license=get_parse_of(soup,'Срок действия лицензии')
        
        #--------------Количество педагогов в каждом из направлений и в целом--------------#
        all_ped, last=count_predkov("Всего:",0,HTML)
        count_ped_paints, last=count_predkov("Художественная направленность:",0,HTML)
        count_ped_estesv, last=count_predkov("Естественнонаучная направленность:",0,HTML)
        count_ped_techno, last=count_predkov("Техническая направленность:",0,HTML)
        count_ped_socium, last=count_predkov("Социально-педагогическая направленность:",0,HTML)
        count_ped_fizra, last=count_predkov("Физкультурно-спортивная направленность:",0,HTML)
        count_ped_turist, last=count_predkov("Туристско-краеведческая направленность:",0,HTML)
        count_ped_intellect, last=count_predkov("Интеллектуальные игры направленность:",0,HTML)
        #--------------Количество детей в каждом из направлений и в целом--------------#
        all_child, last=count_predkov("Всего:",last,HTML)
        count_child_paints, last=count_predkov("Художественная направленность:",last,HTML)
        count_child_estesv, last=count_predkov("Естественнонаучная направленность:",last,HTML)
        count_child_techno, last=count_predkov("Техническая направленность:",last,HTML)
        count_child_socium, last=count_predkov("Социально-педагогическая направленность:",last,HTML)
        count_child_fizra, last=count_predkov("Физкультурно-спортивная направленность:",last,HTML)
        count_child_turist, last=count_predkov("Туристско-краеведческая направленность:",last,HTML)
        count_child_intellect, last=count_predkov("Интеллектуальные игры направленность:",last,HTML)
        
        organizationsss.append({
                'Адрес организации':adress,
                'Номер телефона орагнизации':phone,
                'Номер дополнительного телефона орагнизации':phone_add,
                'email aдрес':email,
                'Адрес сайта': url_name,
                'Работает ли сайт?': site_is_work,
                'title сайта организации': title_org_site,               
                'description сайта организации': description_org_site,
                'keywords сайта организации': keywords_org_site,
                'Cайт принадлежит организации?': site_correct,
                'Количество подписчиков Instagramm': podpis_inst,
                'Ссылки на соц. сети в Instagramm': links_inst, #
                'Количество подписчиков VK': podpis_vk,
                'Ссылки на соц. сети в VK': links_vk, #
                'Количество подписчиков youtube': podpis_youtube,
                'Ссылки на соц. сети в youtube': links_youtube, #
                'id региона': region_id,
                'Полное наименование организации (по уставу)': full_name,
                'Краткое наименование организации': short_name,
                'Дата создания организации': year_create,
                'Юридическое лицо / Филиал': filial,
                'Общее количество сотрудников': all_personal,
                'Субъект РФ': name_region,
                'Тип организации': type_organ,
                'Количество занимающихся детей': all_child,
                'Количество занимающихся детей художественной направленностью': count_child_paints,
                'Количество занимающихся детей естественно-научной направленностью': count_child_estesv,
                'Количество занимающихся детей технической направленностью': count_child_techno,
                'Количество занимающихся детей социально-педагогической направленностью': count_child_socium,
                'Количество занимающихся детей физкультурно-спортивной направленностью': count_child_fizra,
                'Количество занимающихся детей туристической направленностью': count_child_turist,
                'Количество занимающихся детей интеллектуально игровой направленностью': count_child_intellect,
                'Фактическая наполняемость': fact_napoln,
                'Количество педагогов': all_ped,
                'Количество педагогов художественной направленности': count_ped_paints,
                'Количество педагогов естественно-научной направленности': count_ped_estesv,
                'Количество педагогов технической направленности': count_ped_techno,
                'Количество педагогов социально-педагогической направленности': count_ped_socium,
                'Количество педагогов физкультурно-спортивной направленности': count_ped_fizra,
                'Количество педагогов туристической направленности': count_ped_turist,
                'Количество педагогов интеллектуально игровой направленности': count_ped_intellect,
                'okfs': okfs,
                'okopf': okopf,
                'ogrn': ogrn,
                'inn': inn,
                #
                'Номер бланка лицензии': number_license,
                'Кем выдана лицензии': give_license,
                'Cрок лицензии': srok_license, 
                #
                'id': org_id,
                'Техническое': techno,
                'Естественнонаучная': estestv
        })
import time
start_time = time.time()
token = "3fb7074e3fb7074e3fb7074e373fc20ea433fb73fb7074e6000a2640396190c4d381005"  # Сервисный ключ доступа
session = vk.Session(access_token=token)
vk_api = vk.API(session)
x=get_html(URL).text
data = json.loads(x)
organizationsss=[]
count=1;
for organization in data["data"]["list"]:
    #print(organization['id'])
    get_content(organization)
with open('org.csv', 'w', newline="") as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['Адрес организации','Номер телефона орагнизации','Номер дополнительного телефона орагнизации','email aдрес',
                     'Адрес сайта','Работает ли сайт?','title сайта организации','description сайта организации','keywords сайта организации',
                     'Cайт принадлежит организации?','Количество подписчиков Instagramm','Ссылки на соц. сети в Instagramm','Количество подписчиков VK','Ссылки на соц. сети в VK',
                     'Количество подписчиков youtube','Ссылки на соц. сети в youtube','id региона','Полное наименование об организации (по уставу)','Краткое наименование организации','Дата создания организации',
                     'Юридическое лицо / Филиал','Общее количество сотрудников','Субъект РФ','Тип организации','Количество занимающихся детей',
                     'Количество занимающихся детей художественной направленностью','Количество занимающихся детей естественно-научной направленностью',
                     'Количество занимающихся детей технической направленностью','Количество занимающихся детей социально-педагогической направленностью',
                     'Количество занимающихся детей физкультурно-спортивной направленностью','Количество занимающихся детей туристической направленностью',
                     'Количество занимающихся детей интеллектуально игровой направленностью','Фактическая наполняемость','Количество педагогов',
                     'Количество педагогов художественной направленности' ,'Количество педагогов естественно-научной направленности',
                     'Количество педагогов технической направленности' ,'Количество педагогов социально-педагогической направленности' ,
                     'Количество педагогов физкультурно-спортивной направленности' ,'Количество педагогов туристической направленности',
                     'Количество педагогов интеллектуально игровой направленности','okfs','okopf','ogrn','inn','Номер бланка лицензии','Кем выдана лицензии','Cрок лицензии',
                     'id','Техническое','Естественнонаучная'])
    for organizat in organizationsss:
        organizat['Адрес сайта']=organizat['Адрес сайта'].replace('\u200b','')
        try:
            writer.writerow([organizat['Адрес организации'],organizat['Номер телефона орагнизации'],organizat['Номер дополнительного телефона орагнизации'],organizat['email aдрес'],organizat['Адрес сайта'],organizat['Работает ли сайт?'],organizat['title сайта организации'],organizat['description сайта организации'],organizat['keywords сайта организации'],organizat['Cайт принадлежит организации?'],organizat['Количество подписчиков Instagramm'],organizat['Ссылки на соц. сети в Instagramm'],organizat['Количество подписчиков VK'],organizat['Ссылки на соц. сети в VK'],organizat['Количество подписчиков youtube'],organizat['Ссылки на соц. сети в youtube'],organizat['id региона'],organizat['Полное наименование организации (по уставу)'],organizat['Краткое наименование организации'],organizat['Дата создания организации'],organizat['Юридическое лицо / Филиал'],organizat['Общее количество сотрудников'],organizat['Субъект РФ'],organizat['Тип организации'],organizat['Количество занимающихся детей'],organizat['Количество занимающихся детей художественной направленностью'],organizat['Количество занимающихся детей естественно-научной направленностью'],organizat['Количество занимающихся детей технической направленностью'],organizat['Количество занимающихся детей социально-педагогической направленностью'],organizat['Количество занимающихся детей физкультурно-спортивной направленностью'],organizat['Количество занимающихся детей туристической направленностью'],organizat['Количество занимающихся детей интеллектуально игровой направленностью'],organizat['Фактическая наполняемость'],organizat['Количество педагогов'],organizat['Количество педагогов художественной направленности'],organizat['Количество педагогов естественно-научной направленности'],organizat['Количество педагогов технической направленности'],organizat['Количество педагогов социально-педагогической направленности'],organizat['Количество педагогов физкультурно-спортивной направленности'],organizat['Количество педагогов туристической направленности'],organizat['Количество педагогов интеллектуально игровой направленности'],organizat['okfs'],organizat['okopf'],organizat['ogrn'],organizat['inn'],organizat['Номер бланка лицензии'],organizat['Кем выдана лицензии'],organizat['Cрок лицензии'],organizat['id'],organizat['Техническое'],organizat['Естественнонаучная']])
        except:
            writer.writerow([organizat['Адрес организации'],organizat['Номер телефона орагнизации'],organizat['Номер дополнительного телефона орагнизации'],organizat['email aдрес'],organizat['Адрес сайта'],organizat['Работает ли сайт?'],'Неизвестная кодировка','Неизвестная кодировка','Неизвестная кодировка',organizat['Cайт принадлежит организации?'],organizat['Количество подписчиков Instagramm'].organizat['Ссылки на соц. сети в Instagramm'],organizat['Количество подписчиков VK'],organizat['Ссылки на соц. сети в VK'],organizat['Количество подписчиков youtube'],organizat['Ссылки на соц. сети в youtube'],organizat['id региона'],organizat['Полное наименование организации (по уставу)'],organizat['Краткое наименование организации'],organizat['Дата создания организации'],organizat['Юридическое лицо / Филиал'],organizat['Общее количество сотрудников'],organizat['Субъект РФ'],organizat['Тип организации'],organizat['Количество занимающихся детей'],organizat['Количество занимающихся детей художественной направленностью'],organizat['Количество занимающихся детей естественно-научной направленностью'],organizat['Количество занимающихся детей технической направленностью'],organizat['Количество занимающихся детей социально-педагогической направленностью'],organizat['Количество занимающихся детей физкультурно-спортивной направленностью'],organizat['Количество занимающихся детей туристической направленностью'],organizat['Количество занимающихся детей интеллектуально игровой направленностью'],organizat['Фактическая наполняемость'],organizat['Количество педагогов'],organizat['Количество педагогов художественной направленности'],organizat['Количество педагогов естественно-научной направленности'],organizat['Количество педагогов технической направленности'],organizat['Количество педагогов социально-педагогической направленности'],organizat['Количество педагогов физкультурно-спортивной направленности'],organizat['Количество педагогов туристической направленности'],organizat['Количество педагогов интеллектуально игровой направленности'],organizat['okfs'],organizat['okopf'],organizat['ogrn'],organizat['inn'],organizat['Номер бланка лицензии'],organizat['Кем выдана лицензии'],organizat['Cрок лицензии'],organizat['id'],organizat['Техническое'],organizat['Естественнонаучная']])
print("--- %s seconds ---" % (time.time() - start_time)) 
