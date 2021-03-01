import requests
import json

cache = {}


def check_cache(cache, currency):
    print('Checking the cache...')
    if currency.lower() not in cache:
        print('Sorry, but it is not in the cache!')
        add_cache(currency.lower(), parse_dict)
        print('You received ' + str(round(money /
                                          parse_dict[currency.lower()]['inverseRate'], 2)) + ' ' + currency + '.')
    else:
        print('Oh! It is in the cache!')
        print('You received ' + str(round((money / cache[currency.lower()]), 2)) + ' ' + currency + '.')


def add_cache(currency, dict):
    cache[currency] = dict[currency.lower()]['inverseRate']


def check_input(str):
    if '.' in str:
        return float(str)
    else:
        return int(str)


def parse_currency(currency):
    r = requests.get('http://www.floatrates.com/daily/' + str(currency.lower()) + '.json')
    return json.loads(r.text)


currency = str(input())
parse_dict = parse_currency(currency)
if currency.lower() != 'usd':
    add_cache('usd', parse_dict)
if currency.lower() != 'eur':
    add_cache('eur', parse_dict)
while True:
    currency_w_u_w = str(input())
    if currency_w_u_w == '':
        quit()
    else:
        money = check_input(str(input()))
        check_cache(cache, currency_w_u_w)
