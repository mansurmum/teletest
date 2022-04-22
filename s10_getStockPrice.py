import requests
from bs4 import BeautifulSoup

# 종목코드 리스트
stocks = {'카카오':{'code':'035720'}, '하나머티리얼즈':{'code':'166090'}, '유진테크':{'code':'084370'}}

def setPrice(stocks):
    for _key, _value in stocks.items():
        url = 'https://finance.naver.com/item/main.nhn?code=' + _value['code']

        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        today = soup.select_one('#chart_area > div.rate_info > div')
        price = today.select_one('.blind')
        stocks[_key]['price']= price.get_text()
    return stocks


if __name__ == '__main__':
    stocks=setPrice(stocks)
    print(stocks)