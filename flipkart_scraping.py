import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_3_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_3_0_na_na_na&as-pos=3&as-type=TRENDING&suggestionId=mobiles&requestId=ab97a93e-530d-451c-957b-ce07617c519c'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

proxy_servers = {
    'http': 'http://172.67.181.21:80',
    'http': 'http://172.67.185.198:80',
}

r = requests.get(url, headers=headers, proxies=proxy_servers, timeout=10)
print(r.status_code)
soup = BeautifulSoup(r.text, 'html.parser')

data = {'Phone Name': [], 'Phone Price': []}

for name in soup.find_all(class_='KzDlHZ'):
    nm = name.get_text()
    data['Phone Name'].append(nm)

for price in soup.find_all(class_='Nx9bqj _4b5DiR'):
    pr = price.get_text()
    data['Phone Price'].append(pr)

df = pd.DataFrame.from_dict(data)
df.to_excel("flipkart_scraping.xlsx", index=False)