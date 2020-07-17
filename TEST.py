import json
import concurrent.futures
import requests
import os
import decimal
from urllib.parse import urlencode
import hmac

main_path_data = os.path.abspath("./data")

a_file = open(main_path_data + "\\keys.json", "r")
json_object = json.load(a_file)
a_file.close()

a_file1 = open(main_path_data + "\\rools.json", "r")
rools = json.load(a_file1)
a_file1.close()

input_hot_key = 'a3d8ee85-e5a7-12a9-2da662675331e86d'
input_hot_api = '333ab864cc2c24bbce89130825cad32f'

input_live_key = 'gT5fA5uh2f3vbkYxprGU6UYmQxD7uQA4'
input_live_api = 'dV3dGBU6zC85WE53ezNBZSKRVTkA8hxG'

input_a_key = '4pz5GovZBktfF1mxYtwcAAedsZvwJ2x2XC9JEPrpB6PrZFFWVGmqWoGhQg8cMT662ppR1GfNt6p4'
input_a_api = '5z6uK74FTZ2EdHEKLsmmTwCWqrp8J5bt1qAHRQyvjqWYQ2n4Lj5cyqTdR4R8DJhvhyHCpyrme4G4QYwZ6kT7GGzy'


def alfa(val1, val2, price, amount):

    from time import time
    from urllib.parse import urlencode

    if val1 == 'USD' or val1 == 'USDT' or val2 == 'USD' or val2 == 'USDT':
        if val1 == 'USD' or val1 == 'USDT':
            direction = "buy"
            pass
        else:
            direction = "sell"
            pass
    elif val1 != 'USD' and val2 != 'USD' and val1 != 'USDT' and val2 != 'USDT':
        if val1 == 'BTC':
            direction = "buy"
            pass
        else:
            direction = "sell"
            pass


    tickers_all = ['BTC_USD', 'PZM_USD', 'ETH_USD', 'ETH_USDT', 'PZM_BTC', 'ETH_BTC']

    parametr1 = "{}_{}".format(val1, val2)
    parametr2 = "{}_{}".format(val2, val1)

    for i in tickers_all:
        if i == parametr1:
            para = i
            pass
        elif i == parametr2:
            para = i
            pass

    for i in rools['alfa']['amount_precision']:
        if para == i:

            # print('AMOUNT 1 ####', amount)

            d = int(rools['alfa']['amount_precision'][i])

            def custom_round(number, ndigits=d):
                return int(number * 10 ** ndigits) / 10.0 ** ndigits if ndigits else int(number)

            amount = custom_round(amount)
            # print('AMOUNT 3 ####', amount)
            pass
        else:
            pass
    for i in rools['alfa']['price_precision']:
        if para == i:
            d = rools['alfa']['price_precision'][i]
            def chop_to_n_decimals(x, n):

                tre = decimal.Decimal(repr(x))
                targetdigit = decimal.Decimal("1e%d" % -n)
                chopped = tre.quantize(targetdigit, decimal.ROUND_DOWN)
                return float(chopped)

            price = str(chop_to_n_decimals(float(price), d))
            pass
        else:
            pass

    input1 = input_a_key
    input2 = input_a_api

    if input1 != "Api key" and input2 != "Api secret":

        # print('NEW ORDER :', 'ALFA', '\n')
        # print('direction  :', direction)
        # print('para  :', para)
        # print('amount  :', amount)
        # print('price  :', price)

        order = {
            'type': direction,
            'pair': para,
            'amount': str(amount),
            'price': price
        }


        msg = input1 + urlencode(sorted(order.items(), key=lambda val: val[0]))
        sign = hmac.new(input2.encode(), msg.encode(), digestmod='sha256').hexdigest()

        return {
            'X-KEY': input1,
            'X-SIGN': sign,
            'X-NONCE': str(int(time() * 1000)),
        }, order
    else:
        return {},{}
def live(val1, val2, price, amount):
    #####  direction  (buy  / sell)
    if val1 == 'USD' or val1 == 'USDT' or val2 == 'USD' or val2 == 'USDT':
        if val1 == 'USD' or val1 == 'USDT':
            direction = "buy"
            pass
        else:
            direction = "sell"
            pass
    elif val1 != 'USD' and val2 != 'USD' and val1 != 'USDT' and val2 != 'USDT':
        if val1 == 'BTC':
            direction = "buy"
            pass
        else:
            direction = "sell"
            pass

    tickers_all = ['BTC/USD', 'PZM/USD', 'PZM/USDT', 'ETH/USD', 'ETH/USDT', 'PZM/BTC', 'ETH/BTC']

    parametr1 = "{}/{}".format(val1, val2)
    parametr2 = "{}/{}".format(val2, val1)

    for i in tickers_all:
        if i == parametr1:
            para = i
            pass
        elif i == parametr2:
            para = i
            pass

    for i in rools['live']['amount_precision']:
        if para == i:
            print('AMOUNT  ####', amount)
            d = int(rools['live']['amount_precision'][i])
            def custom_round(number, ndigits=d):
                return int(number * 10 ** ndigits) / 10.0 ** ndigits if ndigits else int(number)

            amount = custom_round(amount)
            print('AMOUNT  ####', amount)
            pass
        else:
            pass
    for i in rools['live']['price_precision']:
        if para == i:
            print('PRICE  ####', price)

            d = rools['live']['price_precision'][i]
            def chop_to_n_decimals(x, n):

                tre = decimal.Decimal(repr(x))
                targetdigit = decimal.Decimal("1e%d" % -n)
                chopped = tre.quantize(targetdigit, decimal.ROUND_DOWN)
                return float(chopped)

            price = chop_to_n_decimals(float(price), d)
            # def custom_round(number, ndigits=d):
            #     return int(number * 10 ** ndigits) / 10.0 ** ndigits if ndigits else int(number)
            #
            # price = custom_round(float(price))
            print('PRICE  ####', price)
            pass
        else:
            pass

    input1 = input_live_key
    input2 = input_live_api


    order = {
        'currencyPair': para,
        'quantity': str(amount),
        'price': price
    }
    # order2 = urlencode(sorted(order.items(), key=lambda val: val[0]))


    msg = urlencode(sorted(order.items(), key=lambda val: val[0]))
    sign = hmac.new(input2.encode(), msg=msg.encode(), digestmod='sha256').hexdigest().upper()

    if direction == 'sell':
        url = 'https://api.livecoin.net/exchange/selllimit'
    else:
        url = 'https://api.livecoin.net/exchange/buylimit'

    return {
        'Api-key': input1,
        'Sign': sign,
        "Content-type": "application/x-www-form-urlencoded"
    }, order, url
def hot(val1, val2, price, amount):
    import hashlib
    if val1 == 'USD' or val1 == 'USDT' or val2 == 'USD' or val2 == 'USDT':
      if val1 == 'USD' or val1 == 'USDT':
          direction = 2
          pass
      else:
          direction = 1
          pass
    elif val1 != 'USD' and val2 != 'USD' and val1 != 'USDT' and val2 != 'USDT':
      if val1 == 'BTC':
          direction = 2
          pass
      else:
          direction = 1
          pass

    tickers_all = ['BTC/USD', 'BTC/USDT', 'PZM/USDT', 'ETH/USD', 'ETH/USDT', 'PZM/BTC', 'ETH/BTC']

    parametr1 = "{}/{}".format(val1, val2)
    parametr2 = "{}/{}".format(val2, val1)

    for i in tickers_all:
        if i == parametr1:
          para = i
          pass
        elif i == parametr2:
          para = i
          pass

    for i in rools['hot']['amount_precision']:
        if para == i:
            print('AMOUNT 1 ####', amount)

            d = int(rools['hot']['amount_precision'][i])

            def custom_round(number, ndigits=d):
                return int(number * 10 ** ndigits) / 10.0 ** ndigits if ndigits else int(number)

            amount = custom_round(float(amount))
            print('AMOUNT 3 ####', amount)

            pass
        else:
            pass
    for i in rools['hot']['price_precision']:
        if para == i:

            print('PRICE  before ####', price)
            d = rools['hot']['price_precision'][i]

            def chop_to_n_decimals(x, n):

                tre = decimal.Decimal(repr(x))
                targetdigit = decimal.Decimal("1e%d" % -n)
                chopped = tre.quantize(targetdigit, decimal.ROUND_DOWN)
                return float(chopped)

            price = str(chop_to_n_decimals(float(price), d))
            print('PRICE after ####', price)
            pass
        else:
            pass

    input1 = input_hot_key
    input2 = input_hot_api


    if input1 != "Api key" and input2 != "Api secret":
      # Свой класс исключений
      class ScriptError(Exception):
          pass

      class ScriptQuitCondition(Exception):
          pass

      print('\n', 'NEW ORDER :', 'HOT', '\n')
      print('direction  :', direction)
      print('para  :', para)
      print('amount  :', amount)
      print('price  :', price)

      msg = "amount={}&api_key={}&isfee=0&market={}&price={}&side={}&secret_key={}".format(
          amount, input1, para, price, direction, input2)


      sign = hashlib.md5(msg.encode()).hexdigest().upper()
      url = 'https://api.hotbit.io/api/v1/order.put_limit?amount={}&api_key={}&isfee=0&market={}&price={}&side={}&sign={}'.format(amount, input1, para, price, direction,sign)


      return url
    else:
      return ''


    ####################################################################################















def kurs_al(birka, val1, val2, rate1, val2_vol, val3, val4, rate2, val3_vol):
    out = dict()
    CONNECTIONS = 100
    TIMEOUT = 3


    if birka == 1:
        PARAMS_alfa = alfa(val1, val2, rate1, val2_vol)
        PARAMS_live = live(val3, val4, rate2, val3_vol)
    else:
        PARAMS_live = live(val1, val2, rate1, val2_vol)
        PARAMS_alfa = alfa(val3, val4, rate2, val3_vol)


    a_order = PARAMS_alfa[1]
    a_sign = PARAMS_alfa[0]
    l_order = PARAMS_live[1]
    l_sign = PARAMS_live[0]
    url_l = PARAMS_live[2]

    urls = [
        url_l,
        'https://btc-alpha.com/api/v1/order/'
    ]

    def load_url(url, timeout, a_sign, a_order, l_sign,l_order):
        if 'alpha.com/api/v1/order' in f'**{url}**':
            ans = requests.post(url, data=a_order, headers=a_sign, timeout=timeout)
            ans = ans.json()
            if 'error' in ans and ans['error']:
                return 'alfa', ans['error']
            else:
                return 'alfa', ans['oid']
        elif 'hotbit.io/api/v1/order' in f'**{url}**':
            ans = requests.get(url, timeout=timeout)
            ans = ans.json()
            if 'error' in ans and ans['error']:
                return 'hot', ans['error']['message']
            else:
                return 'hot', ans['result']['id']
        elif 'api.livecoin.net/exchange' in f'**{url}**':
            ans = requests.post(url, data=l_order, headers=l_sign, timeout=timeout)
            ans = ans.json()
            if ans['success'] == False:
                return 'live', ans['exception']
            else:
                return 'live', ans['orderId']
        else:
            return

    with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
        future_to_url = (executor.submit(load_url, url, TIMEOUT, a_sign, a_order, l_sign,l_order) for url in urls)

        for future in concurrent.futures.as_completed(future_to_url):
            try:
                data = future.result()
                print('22 : ', data)
            except Exception as exc:
                data = str(type(exc))
                print('33 : ', data)
            finally:
                out.update({data[0]:data[1]})

    return out

def kurs_ah(birka, val1, val2, rate1, val2_vol, val3, val4, rate2, val3_vol):
    out = dict()
    CONNECTIONS = 100
    TIMEOUT = 3

    if birka == 1:
        PARAMS_alfa = alfa(val1, val2, rate1, val2_vol)
        PARAMS_hot = hot(val3, val4, rate2, val3_vol)
    else:
        PARAMS_hot = hot(val1, val2, rate1, val2_vol)
        PARAMS_alfa = alfa(val3, val4, rate2, val3_vol)

    a_order = PARAMS_alfa[1]
    a_sign = PARAMS_alfa[0]

    urls = [
        PARAMS_hot,
        'https://btc-alpha.com/api/v1/order/'
    ]


    def load_url(url, timeout, a_sign, a_order):
        if 'alpha.com/api/v1/order' in f'**{url}**':
            ans = requests.post(url, data=a_order, headers=a_sign, timeout=timeout)
            ans = ans.json()
            if 'error' in ans and ans['error']:
                return 'alfa', ans['error']
            else:
                return 'alfa', ans['oid']
        elif 'hotbit.io/api/v1/order' in f'**{url}**':
            ans = requests.get(url, timeout=timeout)
            ans = ans.json()
            if 'error' in ans and ans['error']:
                return 'hot', ans['error']['message']
            else:
                return 'hot', ans['result']['id']
        else:
            return

    with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
        future_to_url = (executor.submit(load_url, url, TIMEOUT, a_sign, a_order) for url in urls)

        for future in concurrent.futures.as_completed(future_to_url):
            try:
                data = future.result()
                print('22 : ', data)
            except Exception as exc:
                data = str(type(exc))
                print('33 : ', data)
            finally:
                out.update({data[0]:data[1]})

    return out

def kurs_hl(birka, val1, val2, rate1, val2_vol, val3, val4, rate2, val3_vol):
    out = dict()
    CONNECTIONS = 100
    TIMEOUT = 3

    if birka == 1:
        PARAMS_hot = hot(val1, val2, rate1, val2_vol)
        PARAMS_live = live(val3, val4, rate2, val3_vol)
    else:
        PARAMS_live = live(val1, val2, rate1, val2_vol)
        PARAMS_hot = hot(val3, val4, rate2, val3_vol)

    l_order = PARAMS_live[1]
    l_sign = PARAMS_live[0]
    url_l = PARAMS_live[2]

    urls = [
        PARAMS_hot,
        url_l
    ]

    def load_url(url, timeout, l_sign,l_order):
        if 'hotbit.io/api/v1/order' in f'**{url}**':
            ans = requests.get(url, timeout=timeout)
            ans = ans.json()
            if 'error' in ans and ans['error']:
                return 'hot', ans['error']['message']
            else:
                return 'hot', ans['result']['id']
        elif 'api.livecoin.net/exchange' in f'**{url}**':
            ans = requests.post(url, data=l_order, headers=l_sign, timeout=timeout)
            ans = ans.json()
            if ans['success'] == False:
                return 'live', ans['exception']
            else:
                return 'live', ans['orderId']
        else:
            return

    with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
        future_to_url = (executor.submit(load_url, url, TIMEOUT, l_sign,l_order) for url in urls)

        for future in concurrent.futures.as_completed(future_to_url):
            try:
                data = future.result()
                # print('22 : ', data)
            except Exception as exc:
                data = str(type(exc))
                # print('33 : ', data)
            finally:
                out.update({data[0]:data[1]})

    return out


if birga_1 == 'alfa' and birga_2 == 'live':
    if val2 != 'USD' and val2 != 'USDT':

        repons = kurs_al(1, val1, val2, rate1, val2_vol, val3, val4, rate2, val3_vol)
        dictionary2 = json.dumps(repons)
        dictionary = json.loads(dictionary2)

        reponse_b1 = dictionary['alfa']
        reponse_b2 = dictionary['live']


        all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                reponse_b1, reponse_b2, regims)
        break
    else:

        repons = kurs_al(1, val1, val2, rate1, val1_vol, val3, val4, rate2, val4_vol)
        dictionary2 = json.dumps(repons)
        dictionary = json.loads(dictionary2)

        reponse_b1 = dictionary['alfa']
        reponse_b2 = dictionary['live']

        # reponse_b1 = alfa(val1, val2, rate1, val1_vol)
        # reponse_b2 = live(val3, val4, rate2, val4_vol)
        all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                reponse_b1, reponse_b2, regims)
        break
elif birga_1 == 'live' and birga_2 == 'alfa':
    if val2 != 'USD' and val2 != 'USDT':

        repons = kurs_al(2, val1, val2, rate1, val2_vol, val3, val4, rate2, val3_vol)
        dictionary2 = json.dumps(repons)
        dictionary = json.loads(dictionary2)

        reponse_b1 = dictionary['live']
        reponse_b2 = dictionary['alfa']

        all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                reponse_b1, reponse_b2, regims)
        break
    else:

        repons = kurs_al(2, val1, val2, rate1, val1_vol, val3, val4, rate2, val4_vol)
        dictionary2 = json.dumps(repons)
        dictionary = json.loads(dictionary2)

        reponse_b1 = dictionary['live']
        reponse_b2 = dictionary['alfa']
        # reponse_b1 = live(val1, val2, rate1, val1_vol)
        # reponse_b2 = alfa(val3, val4, rate2, val4_vol)
        all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                reponse_b1, reponse_b2, regims)
        break
elif birga_1 == 'alfa' and birga_2 == 'hot':
    if val2 != 'USD' and val2 != 'USDT':

        repons = kurs_ah(1, val1, val2, rate1, val2_vol, val3, val4, rate2, val3_vol)
        dictionary2 = json.dumps(repons)
        dictionary = json.loads(dictionary2)

        reponse_b1 = dictionary['alfa']
        reponse_b2 = dictionary['hot']

        # reponse_b1 = alfa(val1, val2, rate1, val2_vol)
        # reponse_b2 = hot(val3, val4, rate2, val3_vol)
        all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                reponse_b1, reponse_b2, regims)
        break
    else:

        repons = kurs_ah(1, val1, val2, rate1, val1_vol, val3, val4, rate2, val4_vol)
        dictionary2 = json.dumps(repons)
        dictionary = json.loads(dictionary2)

        reponse_b1 = dictionary['alfa']
        reponse_b2 = dictionary['hot']
        # reponse_b1 = alfa(val1, val2, rate1, val1_vol)
        # reponse_b2 = hot(val3, val4, rate2, val4_vol)
        all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                reponse_b1, reponse_b2, regims)
        break
elif birga_1 == 'hot' and birga_2 == 'alfa':
    if val2 != 'USD' and val2 != 'USDT':


        repons = kurs_ah(2, val1, val2, rate1, val2_vol, val3, val4, rate2, val3_vol)
        dictionary2 = json.dumps(repons)
        dictionary = json.loads(dictionary2)

        reponse_b1 = dictionary['hot']
        reponse_b2 = dictionary['alfa']

        # reponse_b1 = hot(val1, val2, rate1, val2_vol)
        # reponse_b2 = alfa(val3, val4, rate2, val3_vol)
        all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                reponse_b1, reponse_b2, regims)
        break
    else:
        repons = kurs_ah(2, val1, val2, rate1, val1_vol, val3, val4, rate2, val4_vol)
        dictionary2 = json.dumps(repons)
        dictionary = json.loads(dictionary2)

        reponse_b1 = dictionary['hot']
        reponse_b2 = dictionary['alfa']
        # reponse_b1 = hot(val1, val2, rate1, val1_vol)
        # reponse_b2 = alfa(val3, val4, rate2, val4_vol)
        all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                reponse_b1, reponse_b2, regims)
        break
elif birga_1 == 'hot' and birga_2 == 'live':
    if val2 != 'USD' or 'USDT':

        repons = kurs_hl(1, val1, val2, rate1, val2_vol, val3, val4, rate2, val3_vol)
        dictionary2 = json.dumps(repons)
        dictionary = json.loads(dictionary2)

        reponse_b1 = dictionary['hot']
        reponse_b2 = dictionary['live']


        # reponse_b1 = hot(val1, val2, rate1, val2_vol)
        # reponse_b2 = live(val3, val4, rate2, val3_vol)
        all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                reponse_b1, reponse_b2, regims)
        break
    else:

        repons = kurs_hl(1, val1, val2, rate1, val1_vol, val3, val4, rate2, val4_vol)
        dictionary2 = json.dumps(repons)
        dictionary = json.loads(dictionary2)

        reponse_b1 = dictionary['hot']
        reponse_b2 = dictionary['live']
        # reponse_b1 = hot(val1, val2, rate1, val1_vol)
        # reponse_b2 = live(val3, val4, rate2, val4_vol)
        all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                reponse_b1, reponse_b2, regims)
        break
elif birga_1 == 'live' and birga_2 == 'hot':
    if val2 != 'USD' and val2 != 'USDT':

        repons = kurs_hl(2, val1, val2, rate1, val2_vol, val3, val4, rate2, val3_vol)
        dictionary2 = json.dumps(repons)
        dictionary = json.loads(dictionary2)

        reponse_b1 = dictionary['live']
        reponse_b2 = dictionary['hot']


        # reponse_b1 = live(val1, val2, rate1, val2_vol)
        # reponse_b2 = hot(val3, val4, rate2, val3_vol)
        all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                reponse_b1, reponse_b2, regims)
        break
    else:

        repons = kurs_hl(2, val1, val2, rate1, val1_vol, val3, val4, rate2, val4_vol)
        dictionary2 = json.dumps(repons)
        dictionary = json.loads(dictionary2)

        reponse_b1 = dictionary['live']
        reponse_b2 = dictionary['hot']

        # reponse_b1 = live(val1, val2, rate1, val1_vol)
        # reponse_b2 = hot(val3, val4, rate2, val4_vol)
        all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
                reponse_b1, reponse_b2, regims)
        break
else:
    all_csv(birga_1, birga_2, rate1, rate2, val1, val2, val4, val1_vol, val2_vol, val4_vol,
            "No Such Command", "No Such Command", regims)
    break