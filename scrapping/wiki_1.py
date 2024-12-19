import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://ru.wikipedia.org/wiki/%D0%91%D1%83%D0%BB%D0%B3%D0%B0%D0%BA%D0%BE%D0%B2,_%D0%9C%D0%B8%D1%85%D0%B0%D0%B8%D0%BB_%D0%90%D1%84%D0%B0%D0%BD%D0%B0%D1%81%D1%8C%D0%B5%D0%B2%D0%B8%D1%87'
r_wiki = requests.get(url=url)
soup_wiki = BeautifulSoup(r_wiki.text, 'html.parser')

pars_wiki = soup_wiki.find_all('p')
texts_wiki = [text.get_text() for text in pars_wiki]

categories = {
    'Общая информация': ['русский писатель'],
    'Дата и место рождения': ['родился'],
    'Основные произведения': ['известные произведения'],
    'Образование': ['гимназию', 'образование'],
    'Личная жизнь': ['женился', 'брак']
}

data = { 'Категория': [], 'Информация': [] }

def categorize_text(text):
    for category, keywords in categories.items():
        if any(keyword in text.lower() for keyword in keywords):
            return category
    return 'Прочее'

for text in texts_wiki:
    category = categorize_text(text)
    data['Категория'].append(category)
    data['Информация'].append(text.strip())

df = pd.DataFrame(data)

df = df[df['Категория'] != 'Прочее']


df.head()
