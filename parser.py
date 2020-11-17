from bs4 import BeautifulSoup
import requests
import csv
import sys
import validators
import json
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0', 'accept': '*/*'}
HOST = 'http://dop.edu.ru'
URL = "http://dop.edu.ru/organization/list?page=0&perPage=999999"
def get_html(url):
    try:
        r = requests.get(url, headers=HEADERS, params=None)
        return r
    except:
        print('SOME TROUBLE WITH INTERNET')
        return sys.exit()
def urlChecker(url):
    if not validators.url(url):
        return False
    r = requests.head(url)
    return r.status_code == 200
def find_number(index,string):
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
def get_content(organization):
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
        org_id=organization['id']    
        HTML=get_html(HOST+'/organization/view/'+str(org_id)).text
        soup=BeautifulSoup(HTML,'html.parser')
        try:
            full_name=organization['full_name']
        except:
            full_name=''
        try:
            short_name=organization['name']
        except:
            short_name=''
        try:
            adress=organization['origin_address']
        except:
            adress=''
        try:
            phone=organization['phone']
        except:
            phone=''
        try:
            phone_add=organization['phone_add']
        except:
            phone_add=''
        try:
            email=organization['email']
        except:
            email=''
        try:
            url_name=organization['site_url']
            site_is_work=urlChecker(url_name)
        except:
            site_is_work=False
            url_name=''
            
        if(site_is_work==True):
            HTML2=get_html(url_name).text
            soup2=BeautifulSoup(HTML2,'html.parser')
            
            try:
                title_org_site=soup2.find('title').text
            except:
                title_org_site='не найдено'
            try:
                description_org_site=soup2.find('meta',name='description').text
            except:
                description_org_site='Не найдено'
            try:
                keywords_org_site=soup2.find('meta',name='keywords').text
            except:
                keywords_org_site='Не найдено'
        else:
            title_org_site='Cайт не работает или не существует'
            description_org_site='Cайт не работает или не существует'
            keywords_org_site='Cайт не работает или не существует'
            
            
            
            
        try:
            region_id=organization['region_id']
        except:
            region_id=''
        try:
            year_create=soup.find(title='Дата создания организации').text
        except:
            year_create=''
        try:
            filial=soup.find(title='Юридическое лицо / Филиал').text
        except:
            filial=''
        try:
            all_personal=soup.find(title='Общее количество сотрудников').text
        except:
            all_personal=''
        try:
            name_region=soup.find(title='Субъект РФ').text
        except:
            name_region=''
        try:
            type_organ=organization['institution_type_name']
        except:
            type_organ=''
        try:
            fact_napoln=soup.find(title='Фактическая наполняемость').text
        except:
            fact_napoln=''
            
        tmp=HTML.find("Всего:",0,len(HTML))
        if(tmp!=-1):
            last=tmp+7
            all_ped=find_number(tmp+6,HTML)
        else:
            all_ped=0
        tmp=HTML.find("Художественная направленность:",0,len(HTML))
        if(tmp!=-1):
            last=tmp+31
            count_ped_paints=find_number(tmp+30,HTML)
        else:
            count_ped_paints=0
        tmp=HTML.find("Естественнонаучная направленность:",0,len(HTML))
        if(tmp!=-1):
            last=tmp+35
            count_ped_estesv=find_number(tmp+34,HTML)
        else:
            count_ped_estesv=0
        tmp=HTML.find("Техническая направленность:",0,len(HTML))
        if(tmp!=-1):
            last=tmp+28
            count_ped_techno=find_number(tmp+27,HTML)
        else:
            count_ped_techno=0
        tmp=HTML.find("Социально-педагогическая направленность:",0,len(HTML))
        if(tmp!=-1):
            last=tmp+41
            count_ped_socium=find_number(tmp+40,HTML)
        else:
            count_ped_socium=0
        tmp=HTML.find("Физкультурно-спортивная направленность:",0,len(HTML))
        if(tmp!=-1):
            last=tmp+40
            count_ped_fizra=find_number(tmp+39,HTML)
        else:
            count_ped_fizra=0
        tmp=HTML.find("Туристско-краеведческая направленность:",0,len(HTML))
        if(tmp!=-1):
            last=tmp+40
            count_ped_turist=find_number(tmp+39,HTML)
        else:
            count_ped_turist=0
        tmp=HTML.find("Интеллектуальные игры направленность:",0,len(HTML))
        if(tmp!=-1):
            last=tmp+38
            count_ped_intellect=find_number(tmp+37,HTML)
        else:
            count_ped_intellect=0
        tmp=HTML.find("Всего:",last,len(HTML))
        if(tmp!=-1):
            last=tmp+7
            all_child=find_number(tmp+6,HTML)
        else:
            all_child=0
        tmp=HTML.find("Художественная направленность:",last,len(HTML))
        if(tmp!=-1):
            count_child_paints=find_number(tmp+30,HTML)
        else:
            count_child_paints=0
        tmp=HTML.find("Естественнонаучная направленность:",last,len(HTML))
        if(tmp!=-1):
            count_child_estesv=find_number(tmp+34,HTML)
        else:
            count_child_estesv=0
        tmp=HTML.find("Техническая направленность:",last,len(HTML))
        if(tmp!=-1):
            count_child_techno=find_number(tmp+27,HTML)
        else:
            count_child_techno=0
        tmp=HTML.find("Социально-педагогическая направленность:",last,len(HTML))
        if(tmp!=-1):
            count_child_socium=find_number(tmp+40,HTML)
        else:
            count_child_socium=0
        tmp=HTML.find("Физкультурно-спортивная направленность:",last,len(HTML))
        if(tmp!=-1):
            count_child_fizra=find_number(tmp+39,HTML)
        else:
            count_child_fizra=0
        tmp=HTML.find("Туристско-краеведческая направленность:",last,len(HTML))
        if(tmp!=-1):
            count_child_turist=find_number(tmp+39,HTML)
        else:
            count_child_turist=0
        tmp=HTML.find("Интеллектуальные игры направленность:",last,len(HTML))
        if(tmp!=-1):
            count_child_intellect=find_number(tmp+37,HTML)
        else:
            count_child_intellect=0
        try:
            okfs=organization['okfs']
        except:
            okfs=''
        try:
            indef_of_organ=soup.find(title='Идентификатор организации').text
        except:
            indef_of_organ=''
        try:
            okopf=organization['okopf']
        except:
            okopf=''                    
        try:
            ogrn=organization['ogrn']
        except:
            ogrn=''
        try:
            inn=organization['inn']
        except:
            inn=''
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
        print(org_id)
x=get_html(URL).text
data = json.loads(x)
organizationsss=[]
for organization in data["data"]["list"]:
    get_content(organization)
with open('org.csv', 'w', newline="") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Адрес организации','Номер телефона орагнизации','Номер дополнительного телефона орагнизации','email aдрес','Адрес сайта','Работает ли сайт?','title сайта организации','description сайта организации','keywords сайта организации','id региона','Полное наименование организации (по уставу)','Краткое наименование организации','Дата создания организации','Юридическое лицо / Филиал','Общее количество сотрудников','Субъект РФ','Тип организации','Количество занимающихся детей','Количество занимающихся детей художественной направленностью','Количество занимающихся детей естественно-научной направленностью','Количество занимающихся детей технической направленностью','Количество занимающихся детей социально-педагогической направленностью','Количество занимающихся детей физкультурно-спортивной направленностью','Количество занимающихся детей туристической направленностью','Количество занимающихся детей интеллектуально игровой направленностью','Фактическая наполняемость','Количество педагогов','Количество педагогов художественной направленности' ,'Количество педагогов естественно-научной направленности','Количество педагогов технической направленности' ,'Количество педагогов социально-педагогической направленности' ,'Количество педагогов физкультурно-спортивной направленности' ,'Количество педагогов туристической направленности','Количество педагогов интеллектуально игровой направленности','okfs','indef_of_organ','okopf','ogrn','inn','id','Техническое','Естественнонаучная'])
    for organizat in organizationsss:
        organizat['Адрес сайта']=organizat['Адрес сайта'].replace('\u200b','')
        writer.writerow([organizat['Адрес организации'],organizat['Номер телефона орагнизации'],organizat['Номер дополнительного телефона орагнизации'],organizat['email aдрес'],organizat['Адрес сайта'],organizat['Работает ли сайт?'],organizat['title сайта организации'],organizat['description сайта организации'],organizat['keywords сайта организации'],organizat['id региона'],organizat['Полное наименование организации (по уставу)'],organizat['Краткое наименование организации'],organizat['Дата создания организации'],organizat['Юридическое лицо / Филиал'],organizat['Общее количество сотрудников'],organizat['Субъект РФ'],organizat['Тип организации'],organizat['Количество занимающихся детей'],organizat['Количество занимающихся детей художественной направленностью'],organizat['Количество занимающихся детей естественно-научной направленностью'],organizat['Количество занимающихся детей технической направленностью'],organizat['Количество занимающихся детей социально-педагогической направленностью'],organizat['Количество занимающихся детей физкультурно-спортивной направленностью'],organizat['Количество занимающихся детей туристической направленностью'],organizat['Количество занимающихся детей интеллектуально игровой направленностью'],organizat['Фактическая наполняемость'],organizat['Количество педагогов'],organizat['Количество педагогов художественной направленности'],organizat['Количество педагогов естественно-научной направленности'],organizat['Количество педагогов технической направленности'],organizat['Количество педагогов социально-педагогической направленности'],organizat['Количество педагогов физкультурно-спортивной направленности'],organizat['Количество педагогов туристической направленности'],organizat['Количество педагогов интеллектуально игровой направленности'],organizat['okfs'],organizat['indef_of_organ'],organizat['okopf'],organizat['ogrn'],organizat['inn'],organizat['id'],organizat['Техническое'],organizat['Естественнонаучная']])
opener ="open" if sys.platform == "darwin" else "xdg-open"
subprocess.call([opener, 'org.csv'])
