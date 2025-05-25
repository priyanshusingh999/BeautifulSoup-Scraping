import requests, os, random
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

with open("more_proxies.txt") as red:
    lines = red.readlines()

random_line = random.choice(lines)
proxy = random_line.strip()

r = requests.get(url, headers=headers, proxies={ 'http': proxy }, timeout=10)
print(r.status_code)
soup = BeautifulSoup(r.text, 'html.parser')
html_content = soup.prettify()

with open('imdb.html', 'w', encoding='utf-8') as f:
    f.write(str(html_content))

data = {'Movie Name': [], 'Year of Release': [], 'Rating': []}

h3_tags = soup.select('ul h3.ipc-title__text')
for name in h3_tags:
    text = name.get_text()
    data['Movie Name'].append(text)

details = soup.find_all('div', class_='sc-4b408797-7 fUdAcX cli-title-metadata')
for det in details:
    x = det.find_all('span', class_='sc-4b408797-8 iurwGb cli-title-metadata-item')
    texts = [span.get_text(strip=True) for span in x]
    n = ' '.join(texts)
    data['Year of Release'].append(n)

for rating in soup.find_all('span', class_='ipc-rating-star--rating'):
    rat = rating.get_text()
    # print(rat)
    data['Rating'].append(rat)

df = pd.DataFrame.from_dict(data)
df.to_excel('imdb.xlsx', index=False)