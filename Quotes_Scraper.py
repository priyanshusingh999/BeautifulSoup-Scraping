import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, headers=headers, timeout=10)
soup = BeautifulSoup(r.text, 'html.parser')
html_content = soup.prettify()
with open('Quotes_Scraper.html', 'w', encoding='utf-8') as f:
    f.write(str(html_content))

data = {'Author':[], 'Quotes': []}

for quotes in soup.find_all(class_='text'):
    all_quotes = quotes.get_text()
    data['Quotes'].append(all_quotes)

for author in soup.find_all(class_='author'):
    all_author = author.get_text()
    data['Author'].append(all_author)

df = pd.DataFrame.from_dict(data)
df.to_excel("Quotes_Scraper.xlsx", index=False)