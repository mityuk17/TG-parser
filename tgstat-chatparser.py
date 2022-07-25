# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
categories = {'Блоги': 'blogs', 'Новости и СМИ': 'news', 'Юмор и развлечения': 'entertainment', 'Технологии': 'tech', 'Экономика': 'economics', 'Бизнес и стартапы': 'business', 'Криптовалюты': 'crypto', 'Путешествия': 'travels', 'Маркетинг, PR, реклама': 'marketing', 'Психология': 'psychology', 'Дизайн': 'design', 'Политика': 'politics', 'Искусство': 'art', 'Право': 'law', 'Образование': 'education', 'Книги': 'books', 'Лингвистика': 'language', 'Карьера': 'career', 'Познавательное': 'edutainment', 'Курсы и гайды': 'courses', 'Спорт': 'sport', 'Мода и красота': 'beauty', 'Медицина': 'medicine', 'Здоровье и Фитнес': 'health', 'Картинки и фото': 'pics', 'Софт и приложения': 'apps', 'Видео и фильмы': 'video', 'Музыка': 'music', 'Игры': 'games', 'Еда и кулинария': 'food', 'Цитаты': 'quotes', 'Рукоделие': 'handmade', 'Семья и дети': 'babies', 'Природа': 'nature', 'Интерьер и строительство': 'construction', 'Telegram': 'telegram', 'Инстаграм': 'instagram', 'Продажи': 'sales', 'Транспорт': 'transport', 'Религия': 'religion', 'Эзотерика': 'esoterics', 'Даркнет': 'darknet', 'Букмекерство': 'gambling', 'Шок-контент': 'shock', 'Эротика': 'erotica', 'Для взрослых': 'adult', 'Другое': 'other'}
sort_types = ['members','members_t', 'members_y','members_7d','members_30d','msgs', 'mau']
regions = {'Алтайский край': 'altai-region', 'Амурская область': 'amur-region', 'Архангельская область': 'arkhangelsk-region', 'Астраханская область': 'astrakhan-region', 'Белгородская область': 'belgorod-region', 'Брянская область': 'bryansk-region', 'Владимирская область': 'vladimir-region', 'Волгоградская область': 'volgograd-region', 'Вологодская область': 'vologda-region', 'Воронежская область': 'voronezh-region', 'Забайкальский край': 'zabaikal-region', 'Ивановская область': 'ivanovo-region', 'Иркутская область': 'irkutsk-region', 'Кабардино-Балкарская Республика': 'kbr-region', 'Калининградская область': 'kaliningrad-region', 'Калужская область': 'kaluga-region', 'Камчатский край': 'kamchatka-region', 'Карачаево-Черкесская республика': 'kchr-region', 'Кемеровская область': 'kemerovo-region', 'Кировская область': 'kirov-region', 'Костромская область': 'kostroma-region', 'Краснодарский край': 'krasnodar-region', 'Красноярский край': 'krasnoyarsk-region', 'Курганская область': 'kurgan-region', 'Курская область': 'kursk-region', 'Липецкая область': 'lipetsk-region', 'Магаданская область': 'magadan-region', 'Москва': 'moscow', 'Московская область': 'moscow-region', 'Мурманская область': 'murmansk-region', 'Нижегородская область': 'nn-region', 'Новгородская область': 'novgorod-region', 'Новосибирская область': 'novosibirsk-region', 'Омская область': 'omsk-region', 'Оренбургская область': 'orenburg-region', 'Орловская область': 'orlov-region', 'Пензенская область': 'penza-region', 'Пермский край': 'perm-region', 'Приморский край': 'primorsk-region', 'Псковская область': 'pskov-region', 'Республика Адыгея': 'adigea-region', 'Республика Алтай': 'altai', 'Республика Башкортостан': 'bashkiria-region', 'Республика Бурятия': 'buratia-region', 'Республика Дагестан': 'dagestan-region', 'Республика Ингушетия': 'ingushetia-region', 'Республика Калмыкия': 'kalmikia-region', 'Республика Коми': 'komi-region', 'Республика Крым': 'crimea', 'Республика Марий Эл': 'maryel-region', 'Республика Мордовия': 'mordovia-region', 'Республика Саха (Якутия)': 'yakutia-region', 'Республика Северная Осетия - Алания': 'alania-region', 'Республика Татарстан': 'tatarstan-region', 'Республика Тыва': 'tiva-region', 'Республика Хакасия': 'hakasia-region', 'Ростовская область': 'rostov-region', 'Рязанская область': 'ryazan-region', 'Самарская область': 'samara-region', 'Санкт-Петербург': 'spb', 'Саратовская область': 'saratov-region', 'Сахалинская область': 'sakhalin-region', 'Свердловская область': 'ekb-region', 'Смоленская область': 'smolensk-region', 'Ставропольский край': 'stavropol-region', 'Тамбовская область': 'tambov-region', 'Тверская область': 'tver-region', 'Томская область': 'tomsk-region', 'Тульская область': 'tula-region', 'Тюменская область': 'tyumen-region', 'Удмуртская Республика': 'udmurtia-region', 'Ульяновская область': 'ulyanovsk-region', 'Хабаровский край': 'khabarovsk-region', 'Ханты-Мансийский автономный округ - Югра': 'hmao-region', 'Челябинская область': 'chel-region', 'Чеченская Республика': 'chechnya-region', 'Чувашская Республика': 'chuvashia-region', 'Чукотский автономный округ': 'chukotka-region', 'Ямало-Ненецкий автономный округ': 'yamal-region', 'Ярославская область': 'yaroslavl-region'}

def post_region(region, page):
    cookies = {
        '_tgstat_csrk': 'f2234d2c4e26bcb7442b60ff1be2eabd7ea876e0eae3b2b48c8043c3a5a0d9a4a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22_tgstat_csrk%22%3Bi%3A1%3Bs%3A32%3A%22A3_qhRWhTWRTOxc92ofPDmvdWOeMf2Xo%22%3B%7D',
        '_ym_uid': '165694006025449038',
        '_ym_d': '1656940060',
        '_ym_isad': '2',
    }

    headers = {
        'authority': 'tgstat.ru',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_tgstat_csrk=f2234d2c4e26bcb7442b60ff1be2eabd7ea876e0eae3b2b48c8043c3a5a0d9a4a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22_tgstat_csrk%22%3Bi%3A1%3Bs%3A32%3A%22A3_qhRWhTWRTOxc92ofPDmvdWOeMf2Xo%22%3B%7D; _ym_uid=165694006025449038; _ym_d=1656940060; _ym_isad=2',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0NTMyNzEiLCJhcCI6IjMyODAxMDQxNyIsImlkIjoiYjAxMDE2ZGZjMzYwN2EyZSIsInRyIjoiYTdlNDU4YjlhZjk0OWY2M2NmYzgwNGZmNTVlNjY1NGEiLCJ0aSI6MTY1Njk0MTM4MzQ4M319',
        'origin': 'https://tgstat.ru',
        'referer': f'https://tgstat.ru/tag/{region}',
        'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-a7e458b9af949f63cfc804ff55e6654a-b01016dfc3607a2e-01',
        'tracestate': '3453271@nr=0-1-3453271-328010417-b01016dfc3607a2e----1656941383483',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.65',
        'x-newrelic-id': 'VwICUlRUCRADVVhXDwYAU1I=',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        '_tgstat_csrk': 'lWKo4tkPrV9F_bFO6n2EE-76mE5EZiSgJi6xGXk_n6fUUfeTsV36NxGq4xqlBecq3JX-HgALUsRxYdRUHw3HyA==',
        'peerType': 'chat',
        'sortChannel': 'members',
        'sortChat': 'members',
        'categoryId': '0',
        'page': f'{page}',
        'offset': f'{int(page)*30}',
    }

    response = requests.post(f'https://tgstat.ru/tag/{region}/items', cookies=cookies, headers=headers, data=data)
    return response.json()['html']
def parse_region(region):
    ss = []
    for i in range(10):
        response = post_region(region, str(i))
        response = BeautifulSoup(response, features='lxml')
        qq = response.find_all('a', class_ = 'text-body')
        for i in qq:
            ss.append(i.get('href').split('/')[-1])
    fpub = open(f'open{region}.txt', 'w')
    fprivate = open(f'private{region}.txt', 'w')
    for i in ss:
        if i[0:2] == 'id':
            fprivate.write(f'\n{i}')
        else:
            fpub.write(f'\n{i}')
    fpub.close()
    fprivate.close()
    return ss
def post_cat_s(category, sort):
    headers = {
        'authority': 'tgstat.ru',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'referer': 'https://tgstat.ru/ratings/chats',
        'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.75',
    }
    response = requests.get(f'https://tgstat.ru/ratings/chats/{category}?sort={sort}',headers= headers)
    soup = BeautifulSoup(response.text, features='lxml')
    return soup
def parse_category(category):
    ss = []
    for i in sort_types:
        response = post_cat_s(category,i)
        qq = response.find_all('div', class_ = 'col col-12 col-sm-5 col-md-5 col-lg-4')
        for i in qq:
            try:
                q = i.find('a')
                link = (q.get('href').split('/')[-2])
                if link not in ss:
                    ss.append(link)
            except AttributeError:
                pass
    fpub = open(f'open{category}.txt','w')
    fprivate = open(f'private{category}.txt', 'w')
    for i in ss:
        if i[0] != "@":
            fprivate.write(f'\nhttps://t.me/joinchat/{i}')
        else:
            fpub.write(f'\n{i}')
    fpub.close()
    fprivate.close()
    return ss
while True:
    ans = input('Введите 1 для поиска по категориям, 2 для поиска по регионамм:')
    if ans == '1':
        for i in categories:
            print(i)
        a = input('Введите название категории из списка:')
        print(parse_category(categories[a]))
    elif ans =='2':
        for i in regions:
            print(i)
        a = input('Введите название региона из списка:')
        print(parse_region(regions[a]))