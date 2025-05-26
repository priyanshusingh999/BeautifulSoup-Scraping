import requests, random
import pandas as pd
from bs4 import BeautifulSoup

for i in range(1, 10):
    url = f"https://quotes.toscrape.com/page/{i}/"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    with open("more_proxies.txt") as red:
        lines = red.readlines()

    random_line = random.choice(lines)
    proxy = random_line.strip()

    r = requests.get(url, headers=headers, proxies={ 'http': proxy }, timeout=10)
    print(r.status_code)
    soup = BeautifulSoup(r.text, 'html.parser')
    html_content = soup.prettify()
    # with open(f'quotes{i}.html', 'w', encoding='utf-8') as f:
    #     f.write(str(html_content))

    data = {'Quotes': [], 'Author': []}

    for spans in soup.find_all('span', class_='text'):
        text = spans.get_text()
        # print(len(text), 'quotes')
        data['Quotes'].append(text)
    
    for spns in soup.find_all('small', class_='author'):
        msg = spns.get_text()
        # print(len(msg), 'author')
        data['Author'].append(msg)

    df = pd.DataFrame.from_dict(data)
    df.to_excel(f'multi{i}.xlsx', index=False)