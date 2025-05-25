import requests, os
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.amazon.in/s?k=iphone&crid=3IL0YKSL56VTT&sprefix=iphone%2Caps%2C318&ref=nb_sb_noss_2"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
proxy_servers = {
    'http': 'http://172.67.181.21:80',
    'http': 'http://172.67.185.198:80',
}
r = requests.get(url, headers=headers, proxies=proxy_servers, timeout=10)
print(r.status_code)
soup = BeautifulSoup(r.text, "html.parser")

data = {'IPhone':[], 'price':[]}

for h2_tag in soup.find_all('h2'):
    name = h2_tag.get('aria-label')
    if name != None:
        if name == 'iPhone 16e 128 GB: Built for Apple Intelligence, A18 Chip, Supersized Battery Life, 48MP Fusion. Camera, 15.40 cm (6.1″) Super Retina XDR Display; Black':
            continue
        data['IPhone'].append(name)

for price in soup.find_all(class_='a-price-whole'):
    prc = price.get_text()
    data['price'].append(prc)

df = pd.DataFrame.from_dict(data)
df.to_excel("amazon_scraping.xlsx", index=False)
