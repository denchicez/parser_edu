# Парсер сайта http://dop.edu.ru/organization по естественнонаучному и технологическому направлению.
## Download packages
```
- sudo apt update
- sudo apt install python3-pip
- pip3 install beautifulsoup4
- pip3 install requests
- pip3 install vk
- pip3 install validators
```
## Дополнительные фичи
#### 1. Декордировка различных видов кодировок сайтов (latin1,cp1251,UTF-8)
#### 2. Подписчики (максимальное число из всех ссылок) и ссылки на все социальные сети (ютуб,вк,инст) организации
#### 3. Количество учащихся и преподователей по всем направлениям
#### 4. Информация о лицензии организации
#### 5. Резервное сохранение информации при отключение интернета 
### И многие другие улучшения сбора и поиска информации при некорректном заполнение сайта
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
