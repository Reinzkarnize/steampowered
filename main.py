import os
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://store.steampowered.com/search/?'
name = input('Seach games: ')
params = {
    'term': name
}


def get_data(link):
    print('sending  request to' + link + '...')
    r = requests.get(link, params=params)
    return r.text


def parse(data):
    print('scrape element...')
    result = []
    soup = BeautifulSoup(data, 'html.parser')
    content = soup.find('div', attrs={'id': 'search_resultsRows'})
    games = content.findAll('a')

    for game in games:
        link = game['href']
        names = game.find('span', attrs={'class': 'title'}).text
        release = game.find('div', attrs={'class': 'col search_released responsive_secondrow'}).text

        if release == '':
            release = 'None'

        try:
            price = game.find('div', attrs={'class': 'col search_price responsive_secondrow'}).text.strip()
        except AttributeError:
            prices = game.find('div',
                               attrs={'class': 'col search_price discounted responsive_secondrow'}).text.strip().split(
                'Rp')
            price = 'Rp' + prices[2]
        if price == '':
            price = 'unknown'
        data_dict = {
            'Title': names,
            'Price': price,
            'Url': link,
            'Release date': release
        }
        result.append(data_dict)

    return result


def output(datas, filename):
    print('Writing result into files...')
    try:
        os.mkdir('result')
    except FileExistsError:
        pass
    df = pd.DataFrame(datas)
    df.to_json(f'result/{filename}.json', orient='records')
    df.to_excel(f'result/{filename}.xlsx', index=False)
    df.to_csv(f'result/{filename}.csv', index=False)


if __name__ == '__main__':
    req = get_data(url)
    results = parse(req)
    output(results, name)
