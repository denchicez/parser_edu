from bs4 import BeautifulSoup
import requests
import csv
import json
import os
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0', 'accept': '*/*'}
HOST = 'http://dop.edu.ru'
URL = "http://dop.edu.ru/organization/list?orientation=3,4&page=1&perPage=999999"
def get_html(url):
    r = requests.get(url, headers=HEADERS, params=None)
    return r
def get_content(organization):
    techno=organization['orientation_name'].find('Техническая',0,len(organization['orientation_name']))
    estestv=organization['orientation_name'].find('Естественнонаучная',0,len(organization['orientation_name']))
    if(techno<0):
        techno=0
    else:
        techno=1
    if(estestv<0):
        estestv=0
    else:
        estestv=1
    if(estestv|techno==1):
        org_id=organization['id']    
        HTML=get_html(HOST+'/organization/view/'+str(org_id)).text
        soup=BeautifulSoup(HTML,'html.parser')
        full_name=organization['full_name']
        short_name=organization['name']
        adress=organization['origin_address']
        phone=organization['phone']
        phone_add=organization['phone_add']
        email=organization['email']
        url_name=organization['site_url']
        region_id=organization['region_id']
        year_create=soup.find(title='Дата создания организации').text
        filial=soup.find(title='Юридическое лицо / Филиал').text
        all_personal=soup.find(title='Общее количество сотрудников').text
        name_region=soup.find(title='Субъект РФ').text
        type_organ=organization['institution_type_name']
        all_child=HTML.find("Всего:",0,len(HTML))
        print(all_child,' ',HTML[all_child])
        count_child_paints=''
        count_child_estesv=''
        count_child_techno=''
        count_child_socium=''
        count_child_fizra=''
        count_child_turist=''
        count_child_intellect=''
        fact_napoln=soup.find(title='Фактическая наполняемость').text
        all_ped=''
        count_ped_paints=''
        count_ped_estesv=''
        count_ped_techno=''
        count_ped_socium=''
        count_ped_fizra=''
        count_ped_turist=''
        count_ped_intellect=''
        okfs=organization['okfs']
        indef_of_organ=soup.find(title='Идентификатор организации').text
        okopf=organization['okopf']
        ogrn=organization['ogrn']
        inn=organization['inn']
        organizationsss.append({
                'Адрес организации':adress,
                'Номер телефона орагнизации':phone,
                'Номер дополнительного телефона орагнизации':phone_add,
                'email aдрес':email,
                'Адрес сайта': url_name,
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
x=get_html(URL).text
data = json.loads(x)
organizationsss=[]
for organization in data["data"]["list"]:
    get_content(organization)
    break
with open('org.csv', 'w', newline="") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Адрес организации','Номер телефона орагнизации','Номер дополнительного телефона орагнизации','email aдрес','Адрес сайта','id региона','Полное наименование организации (по уставу)','Краткое наименование организации','Дата создания организации','Юридическое лицо / Филиал','Общее количество сотрудников','Субъект РФ','Тип организации','Количество занимающихся детей','Количество занимающихся детей художественной направленностью','Количество занимающихся детей естественно-научной направленностью','Количество занимающихся детей технической направленностью','Количество занимающихся детей социально-педагогической направленностью','Количество занимающихся детей физкультурно-спортивной направленностью','Количество занимающихся детей туристической направленностью','Количество занимающихся детей интеллектуально игровой направленностью','Фактическая наполняемость','Количество педагогов','Количество педагогов художественной направленности' ,'Количество педагогов естественно-научной направленности','Количество педагогов технической направленности' ,'Количество педагогов социально-педагогической направленности' ,'Количество педагогов физкультурно-спортивной направленности' ,'Количество педагогов туристической направленности','Количество педагогов интеллектуально игровой направленности','okfs','indef_of_organ','okopf','ogrn','inn','id','Техническое','Естественнонаучная'])
    for organizat in organizationsss:
        organizat['Адрес сайта']=organizat['Адрес сайта'].replace('\u200b','')
        writer.writerow([organizat['Адрес организации'],organizat['Номер телефона орагнизации'],organizat['Номер дополнительного телефона орагнизации'],organizat['email aдрес'],organizat['Адрес сайта'],organizat['id региона'],organizat['Полное наименование организации (по уставу)'],organizat['Краткое наименование организации'],organizat['Дата создания организации'],organizat['Юридическое лицо / Филиал'],organizat['Общее количество сотрудников'],organizat['Субъект РФ'],organizat['Тип организации'],organizat['Количество занимающихся детей'],organizat['Количество занимающихся детей художественной направленностью'],organizat['Количество занимающихся детей естественно-научной направленностью'],organizat['Количество занимающихся детей технической направленностью'],organizat['Количество занимающихся детей социально-педагогической направленностью'],organizat['Количество занимающихся детей физкультурно-спортивной направленностью'],organizat['Количество занимающихся детей туристической направленностью'],organizat['Количество занимающихся детей интеллектуально игровой направленностью'],organizat['Фактическая наполняемость'],organizat['Количество педагогов'],organizat['Количество педагогов художественной направленности'],organizat['Количество педагогов естественно-научной направленности'],organizat['Количество педагогов технической направленности'],organizat['Количество педагогов социально-педагогической направленности'],organizat['Количество педагогов физкультурно-спортивной направленности'],organizat['Количество педагогов туристической направленности'],organizat['Количество педагогов интеллектуально игровой направленности'],organizat['okfs'],organizat['indef_of_organ'],organizat['okopf'],organizat['ogrn'],organizat['inn'],organizat['id'],organizat['Техническое'],organizat['Естественнонаучная']])
opener ="open" if sys.platform == "darwin" else "xdg-open"
subprocess.call([opener, 'org.csv'])
