import requests
from  datetime import datetime as date

BASE_URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
NOW = date.now()
VALUTE_CODES = {'1': 'RUB', '2': 'EUR', '3': 'USD', '4': 'GEL'}


def greeting() -> str:
    return f""""Конвертер валют по курсу ЦБ РФ на
    текущую дату : {NOW.strftime("%d %b %Y")}" 
    
Коды Валют 1:RUB, 2:EUR, 3:USD, 4:GEL 
"""


def exchange_from_rub () -> str:
    while True:
        to_valute = VALUTE_CODES.get(input('Куда перевод? (Код) : '), False)
        if to_valute == False or to_valute == 'RUB':
            print("Некорректный ввод. Попробуйте еще")
        else:
            exchange_sum = (input('Какую сумму перевести?(Рублей) : '))
            if exchange_sum.isdigit() and int(exchange_sum) > 0:
                return "%.2f" % (int(exchange_sum) / get_valute_rate_value(to_valute)) + to_valute
            else:
                print("Некорректный ввод. Попробуйте еще")



def exchange_to_rub (code_valute:str) -> str:
    while True:
        exchange_sum = input(f'Перевод возможен только в рубли, введите сумму в {code_valute} : ')
        if exchange_sum.isdigit() and int(exchange_sum) > 0:
            return "%.2f" % (int(exchange_sum) * get_valute_rate_value(code_valute)) + 'RUB'
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



