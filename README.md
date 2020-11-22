# Парсер сайта http://dop.edu.ru/organization по Московской области и технологическому направлению
## Download packages
```
- sudo apt update
- sudo apt install python3-pip
- pip3 install beautifulsoup4
- pip3 install requests
- pip3 install vk
- pip3 install validators
```
## Run script
### Script template
##### Script template input
```
python3 <путь до parser.py>
```
##### Script template output
```
Файл - org.csv
```

### Script simple
##### Script simple input
```
python3 /home/user/test/parser.py
```
##### Script simple output
```
Файл - /home/user/org.csv
```
###### org.csv
| Полное наименование| Краткое наименование | Адрес сайта |
| ------------------ |:--------------------:| -----------:|
| Государственное бюджетное образовательное учреждение высшего образования Московской области «Технологический университет» / Центр дополнительного образования «Детский технопарк «Кванториум»    | ГБОУ ВО МО «Технологический университет» / Детский технопарк «КВАНТОРИУМ» г. Королев    | http://unitech-mo.ru/obrazovanie/school-divisions/kvantorium/ |
