# Проект парсинга pep на фреймворке scrapy

Парсер собирает информацию  о статусе всех существующих PEP. Со страниц PEP парсер собирает номер, название, статус и сохраняет в файл в формате csv

Стек: Python v3.9, Scrapy.

#### Как запустить проект:

+ клонируем репозиторий
```
https://github.com/milkyaway13/scrapy_parser_pep
```

+ переходим в корневую папку проекта
```
cd scrapy_parser_pep
```
+ создаем виртуальное окружение
 ```
python -m venv env
```
+ активируем виртуальное окружение
```
source env/scripts/activate
```
 + устанавливаем зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
+ запускаем парсер
```
scrapy crawl pep
```


## Автор
[Боярчук Василий](https://github.com/Milkyaway13/)
