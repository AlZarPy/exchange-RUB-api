import requests
from  datetime import datetime as d

BASE_URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
NOW = d.now()
VALUTE_CODES = {'1': 'RUB', '2': 'EUR', '3': 'USD', '4': 'GEL'}


def greeting() -> str:
    return f""""Конвертер валют по курсу ЦБ РФ на
    текущую дату : {NOW.strftime("%d %b %Y")}" 
    
Коды Валют 1:RUB, 2:EUR, 3:USD, 4:GEL 
"""


def exchange_from_rub () -> str:
    while True:
        to_valute = VALUTE_CODES.get(input('Куда перевод? (Код) : '))
        if to_valute is None or to_valute == 'RUB':
            print("Некорректный ввод. Попробуйте еще")
            continue
        exchange_sum = (input('Какую сумму перевести?(Рублей) : '))
        if not exchange_sum.isdigit() and int(exchange_sum) <= 0:
            print("Некорректный ввод. Попробуйте еще")
            continue
        result = int(exchange_sum) / get_valute_rate_value(to_valute)
        return f"{result:.2f} {to_valute}"





def exchange_to_rub (code_valute:str) -> str:
    while True:
        exchange_sum = input(f'Перевод возможен только в рубли, введите сумму в {code_valute} : ')
        if exchange_sum.isdigit() and int(exchange_sum) > 0:
            result = int(exchange_sum) * get_valute_rate_value(code_valute)
            return f"{result:.2f} RUB"
        else:
            print("Некорректный ввод. Попробуйте еще")


def get_valute_rate_value(code_valute:str) -> float:
    response = requests.get(url=BASE_URL)
    response.raise_for_status()
    data = response.json()
    return data['Valute'][code_valute]['Value']



if __name__ == '__main__':
    print(greeting())
    while True:
        code_valute = VALUTE_CODES.get(input('Из какой валюты перевод? (Код): '), False)
        if code_valute == False :
            print("Некорректный ввод. Попробуйте еще")
        elif code_valute == 'RUB':
            print(exchange_from_rub())
            break
        else:
            print(exchange_to_rub(code_valute))
            break



