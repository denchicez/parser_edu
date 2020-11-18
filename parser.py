from bs4 import BeautifulSoup
import requests
import csv
import sys
import validators
import json
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0', 'accept': '*/*'}
HOST = 'http://dop.edu.ru'
URL = "http://dop.edu.ru/organization/list?page=0&perPage=999999"
def get_html(url):         # делаем запрос на html страничку
    try:
        r = requests.get(url, headers=HEADERS, params=None)
        return r
    except:
        print('SOME TROUBLE WITH INTERNET') #не смогли сделать запрос т.к. произошла ошибка с связью
        return sys.exit()
def urlChecker(url): #Работает ли URL?
    if not validators.url(url):
        return False
    r = requests.head(url)
    return r.status_code == 200
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
def NameCheck(string,code1,code2): #Можно ли расшифровать stirng с помощью code1 и code2
    letters = ['<','>','«','»',chr(13),chr(10),'(',')','|',':',' ',chr(34),'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','а','a','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я','-','+',',','.','/','[',']','1','2','3','4','5','6','7','8','9','0','#','№','-','—','_','=','}','{','+','!','?','#']
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
def get_content(organization,coun): #узнаем все параметры организации
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
        count=count+1
        org_id=organization['id']
        HTML=get_html(HOST+'/organization/view/'+str(org_id)).text
        soup=BeautifulSoup(HTML,'html.parser')
        try:
            full_name=organization['full_name']
            if(full_name=='' or full_name==None or full_name==' '):
                full_name='Не известно'
        except:
            full_name='Не известно'
        try:
            short_name=organization['name']
            if(short_name=='' or short_name==None or short_name==' '):
                short_name='Не известно'
        except:
            short_name='Не известно'
        try:
            adress=organization['origin_address']
            if(adress=='' or adress==None or adress==' '):
                adress='Не известно'
        except:
            adress='Не известно'
        try:
            phone=organization['phone']
            if(phone=='' or phone==None or phone==' '):
                phone='Не известно'
        except:
            phone='Не известно'
        try:
            phone_add=organization['phone_add']
            if(phone_add=='' or phone_add==None or phone_add==' '):
                phone_add='Не известно'
        except:
            phone_add='Не известно'
        try:
            email=organization['email']
            if(email=='' or email==None or email==' '):
                email='Не известно'
        except:
            email='Не известно'
            
        try:
            url_name=organization['site_url']
            if(url_name=='' or url_name==None or url_name==' '):
                url_name='Не известно'
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
            url_name='Не известно'
            
        if(site_is_work==True):
            HTML2=get_html(url_name).text
            soup2=BeautifulSoup(HTML2,'html.parser')
            all_code = ['UTF-8','UTF-16','cp1251','latin1']
            try:
                title_org_site=((soup2.find('head')).find('title')).text
                print(title_org_site)
                if(title_org_site.find('�',0,len(title_org_site))==-1):
                    code1='UTF-8'
                    code2='UTF-8'
                    chk=0
                    for code_in_all1 in all_code:
                        for code_in_all2 in all_code:
                            if(NameCheck(title_org_site,code_in_all1,code_in_all2)==True):
                                code1=code_in_all1
                                code2=code_in_all2
                                chk=1
                                break
                        if(chk==1):
                            title_org_site=title_org_site.encode(code1).decode(code2)
                            break
                    if(chk==0):
                        title_org_site='У сайта неизвестная кодировка'
                    print(title_org_site)
                else:
                    title_org_site='У сайта неизвестная кодировка' 
                
            except:
                code1='UTF-8'
                code2='UTF-8'
                title_org_site='Не найдено'  
            if(title_org_site!='У сайта неизвестная кодировка'):
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
            else:
                description_org_site='У сайта неизвестная кодировка'
                keywords_org_site='У сайта неизвестная кодировка'
        else:
            title_org_site='Cайт не работает или не существует'
            description_org_site='Cайт не работает или не существует'
            keywords_org_site='Cайт не работает или не существует'
        try:
            region_id=organization['region_id']
            if(region_id=='' or region_id==None or region_id==' '):
                region_id='Не известно'
        except:
            region_id='Не известно'
        try:
            year_create=soup.find(title='Дата создания организации').text
            if(year_create=='' or year_create==None or year_create==' '):
                year_create='Не известно'
        except:
            year_create='Не известно'
        try:
            filial=soup.find(title='Юридическое лицо / Филиал').text
            if(filial=='' or filial==None or filial==' '):
                filial='Не известно'
        except:
            filial='Не известно'
        try:
            all_personal=soup.find(title='Общее количество сотрудников').text
            if(all_personal=='' or all_personal==None or all_personal==' '):
                all_personal='Не известно'
        except:
            all_personal='Не известно'
        try:
            name_region=soup.find(title='Субъект РФ').text
            if(name_region=='' or name_region==None or name_region==' '):
                name_region='Не известно'
        except:
            name_region='Не известно'
        try:
            type_organ=organization['institution_type_name']
            if(type_organ=='' or type_organ==None or type_organ==' '):
                type_organ='Не известно'
        except:
            type_organ='Не известно'
        try:
            fact_napoln=soup.find(title='Фактическая наполняемость').text
            if(fact_napoln=='' or fact_napoln==None or fact_napoln==' '):
                fact_napoln='Не известно'
        except:
            fact_napoln='Не известно'
            
        tmp=HTML.find("Всего:",0,len(HTML))
        if(HTML[tmp+7].isdigit()==False):
            tmp=HTML.find("Всего:",tmp+7,len(HTML))
        if(tmp!=-1):
            last=tmp+7
            all_ped=find_number(tmp+6,HTML)
        else:
            all_ped=0
            
        tmp=HTML.find("Художественная направленность:",0,len(HTML))
        if(HTML[tmp+31].isdigit()==False):
            tmp=HTML.find("Художественная направленность:",tmp+31,len(HTML))
        if(tmp!=-1):
            last=tmp+31
            count_ped_paints=find_number(tmp+30,HTML)
        else:
            count_ped_paints=0
            
            
        tmp=HTML.find("Естественнонаучная направленность:,",0,len(HTML))
        if(HTML[tmp+35].isdigit()==False):
            tmp=HTML.find("Естественнонаучная направленность:",tmp+35,len(HTML))
        if(tmp!=-1):
            last=tmp+35
            count_ped_estesv=find_number(tmp+34,HTML)
        else:
            count_ped_estesv=0
            
            
        tmp=HTML.find("Техническая направленность:",0,len(HTML))
        if(HTML[tmp+28].isdigit()==False):
            tmp=HTML.find("Техническая направленность:",tmp+28,len(HTML))
        if(tmp!=-1):
            last=tmp+28
            count_ped_techno=find_number(tmp+27,HTML)
        else:
            count_ped_techno=0
            
            
        tmp=HTML.find("Социально-педагогическая направленность:",0,len(HTML))
        if(HTML[tmp+41].isdigit()==False):
            tmp=HTML.find("Социально-педагогическая направленность:",tmp+41,len(HTML))
        if(tmp!=-1):
            last=tmp+41
            count_ped_socium=find_number(tmp+40,HTML)
        else:
            count_ped_socium=0
        tmp=HTML.find("Физкультурно-спортивная направленность:",0,len(HTML))
        if(HTML[tmp+40].isdigit()==False):
            tmp=HTML.find("Физкультурно-спортивная направленность:",tmp+40,len(HTML))
        if(tmp!=-1):
            last=tmp+40
            count_ped_fizra=find_number(tmp+39,HTML)
        else:
            count_ped_fizra=0
        tmp=HTML.find("Туристско-краеведческая направленность:",0,len(HTML))
        if(HTML[tmp+40].isdigit()==False):
            tmp=HTML.find("Туристско-краеведческая направленность:",tmp+40,len(HTML))
        if(tmp!=-1):
            last=tmp+40
            count_ped_turist=find_number(tmp+39,HTML)
        else:
            count_ped_turist=0
            
            
        tmp=HTML.find("Интеллектуальные игры направленность:",0,len(HTML))
        if(HTML[tmp+38].isdigit()==False):
            tmp=HTML.find("Интеллектуальные игры направленность:",tmp+38,len(HTML))
        if(tmp!=-1):
            last=tmp+38
            count_ped_intellect=find_number(tmp+37,HTML)
        else:
            count_ped_intellect=0
            
        tmp=HTML.find("Всего:",last,len(HTML))
        if(HTML[tmp+7].isdigit()==False):
            tmp=HTML.find("Всего:",tmp+7,len(HTML))
        if(tmp!=-1):
            last=tmp+7
            all_child=find_number(tmp+6,HTML)
        else:
            all_child=0
            
            
        tmp=HTML.find("Художественная направленность:",last,len(HTML))
        if(HTML[tmp+31].isdigit()==False):
            tmp=HTML.find("Художественная направленность:",tmp+30,len(HTML))
        if(tmp!=-1):
            count_child_paints=find_number(tmp+30,HTML)
        else:
            count_child_paints=0
            
        tmp=HTML.find("Естественнонаучная направленность:",last,len(HTML))
        if(HTML[tmp+35].isdigit()==False):
            tmp=HTML.find("Естественнонаучная направленность:",tmp+34,len(HTML))
        if(tmp!=-1):
            count_child_estesv=find_number(tmp+34,HTML)
        else:
            count_child_estesv=0
            
        tmp=HTML.find("Техническая направленность:",last,len(HTML))
        if(HTML[tmp+28].isdigit()==False):
            tmp=HTML.find("Техническая направленность:",tmp+27,len(HTML))
        if(tmp!=-1):
            count_child_techno=find_number(tmp+27,HTML)
        else:
            count_child_techno=0
            
            
        tmp=HTML.find("Социально-педагогическая направленность:",last,len(HTML))
        if(HTML[tmp+41].isdigit()==False):
            tmp=HTML.find("Социально-педагогическая направленность:",tmp+40,len(HTML))
        if(tmp!=-1):
            count_child_socium=find_number(tmp+40,HTML)
        else:
            count_child_socium=0
            
            
        tmp=HTML.find("Физкультурно-спортивная направленность:",last,len(HTML))
        if(HTML[tmp+40].isdigit()==False):
            tmp=HTML.find("Физкультурно-спортивная направленность:",tmp+39,len(HTML))
        if(tmp!=-1):
            count_child_fizra=find_number(tmp+39,HTML)
        else:
            count_child_fizra=0
            
            
        tmp=HTML.find("Туристско-краеведческая направленность:",last,len(HTML))
        if(HTML[tmp+40].isdigit()==False):
            tmp=HTML.find("Туристско-краеведческая направленность:",tmp+39,len(HTML))
        if(tmp!=-1):
            count_child_turist=find_number(tmp+39,HTML)
        else:
            count_child_turist=0
            
            
        tmp=HTML.find("Интеллектуальные игры направленность:",last,len(HTML))
        if(HTML[tmp+38].isdigit()==False):
            tmp=HTML.find("Туристско-краеведческая направленность:",tmp+37,len(HTML))
        if(tmp!=-1):
            count_child_intellect=find_number(tmp+37,HTML)
        else:
            count_child_intellect=0
            
            
            
        try:
            okfs=organization['okfs']
            if(okfs=='' or okfs==None or okfs==' '):
                okfs='Не известно'
        except:
            okfs='Не известно'
        try:
            indef_of_organ=soup.find(title='Идентификатор организации').text
            if(indef_of_organ=='' or indef_of_organ==None or indef_of_organ==' '):
                indef_of_organ='Не известно'
        except:
            indef_of_organ='Не известно'
        try:
            okopf=organization['okopf']
            if(okopf=='' or okopf==None or okopf==' '):
                okopf='Не известно'
        except:
            okopf='Не известно'                    
        try:
            ogrn=organization['ogrn']
            if(ogrn=='' or ogrn==None or ogrn==' '):
                ogrn='Не известно'
        except:
            ogrn='Не известно'
        try:
            inn=organization['inn']
            if(inn=='' or inn==None or inn==' '):
                inn='Не известно'
        except:
            inn='Не известно'
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
                'indef_of_organ': indef_of_organ,
                'okopf': okopf,
                'ogrn': ogrn,
                'inn': inn,
                'id': org_id,
                'Техническое': techno,
                'Естественнонаучная': estestv
        })
        coun=coun+1
x=get_html(URL).text
data = json.loads(x)
organizationsss=[]
count=0;
for organization in data["data"]["list"]:
    get_content(organization,count)
    if(count>500):
        break
with open('org.csv', 'w', newline="") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Адрес организации','Номер телефона орагнизации','Номер дополнительного телефона орагнизации','email aдрес',
                     'Адрес сайта','Работает ли сайт?','title сайта организации','description сайта организации','keywords сайта организации',
                     'id региона','Полное наименование организации (по уставу)','Краткое наименование организации','Дата создания организации',
                     'Юридическое лицо / Филиал','Общее количество сотрудников','Субъект РФ','Тип организации','Количество занимающихся детей',
                     'Количество занимающихся детей художественной направленностью','Количество занимающихся детей естественно-научной направленностью',
                     'Количество занимающихся детей технической направленностью','Количество занимающихся детей социально-педагогической направленностью',
                     'Количество занимающихся детей физкультурно-спортивной направленностью','Количество занимающихся детей туристической направленностью',
                     'Количество занимающихся детей интеллектуально игровой направленностью','Фактическая наполняемость','Количество педагогов',
                     'Количество педагогов художественной направленности' ,'Количество педагогов естественно-научной направленности',
                     'Количество педагогов технической направленности' ,'Количество педагогов социально-педагогической направленности' ,
                     'Количество педагогов физкультурно-спортивной направленности' ,'Количество педагогов туристической направленности',
                     'Количество педагогов интеллектуально игровой направленности','okfs','okopf','ogrn','inn','id','Техническое','Естественнонаучная'])
    for organizat in organizationsss:
        organizat['Адрес сайта']=organizat['Адрес сайта'].replace('\u200b','')
        try:
            writer.writerow([organizat['Адрес организации'],organizat['Номер телефона орагнизации'],organizat['Номер дополнительного телефона орагнизации'],organizat['email aдрес'],organizat['Адрес сайта'],organizat['Работает ли сайт?'],organizat['title сайта организации'],organizat['description сайта организации'],organizat['keywords сайта организации'],organizat['id региона'],organizat['Полное наименование организации (по уставу)'],organizat['Краткое наименование организации'],organizat['Дата создания организации'],organizat['Юридическое лицо / Филиал'],organizat['Общее количество сотрудников'],organizat['Субъект РФ'],organizat['Тип организации'],organizat['Количество занимающихся детей'],organizat['Количество занимающихся детей художественной направленностью'],organizat['Количество занимающихся детей естественно-научной направленностью'],organizat['Количество занимающихся детей технической направленностью'],organizat['Количество занимающихся детей социально-педагогической направленностью'],organizat['Количество занимающихся детей физкультурно-спортивной направленностью'],organizat['Количество занимающихся детей туристической направленностью'],organizat['Количество занимающихся детей интеллектуально игровой направленностью'],organizat['Фактическая наполняемость'],organizat['Количество педагогов'],organizat['Количество педагогов художественной направленности'],organizat['Количество педагогов естественно-научной направленности'],organizat['Количество педагогов технической направленности'],organizat['Количество педагогов социально-педагогической направленности'],organizat['Количество педагогов физкультурно-спортивной направленности'],organizat['Количество педагогов туристической направленности'],organizat['Количество педагогов интеллектуально игровой направленности'],organizat['okfs'],organizat['okopf'],organizat['ogrn'],organizat['inn'],organizat['id'],organizat['Техническое'],organizat['Естественнонаучная']])
        except:
            writer.writerow(['ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR','ERROR'])
