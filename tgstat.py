import requests
from requests.auth import HTTPProxyAuth
from bs4 import BeautifulSoup
import random
proxies = {'https':'5.45.126.147:8085'}
auth = HTTPProxyAuth('mix1G83OFN7', 'xWNuDiTu')
categories = {'Telegram': 32, 'Бизнес и стартапы': 12, 'Блоги': 4, 'Букмекерство': 46, 'Видео и фильмы': 11, 'Даркнет': 55, 'Дизайн':34, 'Для взрослых': 8, 'Другое': 17, 'Еда и кулинария':3, 'Здоровье и Фитнес':45,
                  'Игры':44, 'Инстаграм': 47, 'Интерьер и строительство':53, 'Искусство':49, 'Картинки и фото': 7, 'Карьера': 23, 'Книги':15, 'Криптовалюты':22, 'Курсы и гайды': 48, 'Лингвистика': 21, 'Маркетинг, PR, реклама': 31,
                  'Медицина': 28, 'Мода и красота': 27, 'Музыка': 13, 'Новости и СМИ': 2, 'Образование': 5, 'Познавательное': 41, 'Политика':38, 'Право':50, 'Природа': 37, 'Продажи': 14, 'Психология':33, 'Путешествия':25,
                  'Религия':40, 'Рукоделие':26, 'Семья и дети': 36, 'Софт и приложения': 9, 'Спорт':20, 'Технологии': 1, 'Транспорт': 29, 'Цитаты': 16, 'Шок-контент':52,'Эзотерика':54, 'Экономика':10, 'Эротика':51, 'Юмор и развлечения':6}

def createpost_key(key, page):
    cookies = {
        '_tgstat_csrk': 'ea8bb475274bed9c45851dad32a2a837c814eb7c60b7067a3643c5faf90e8466a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22_tgstat_csrk%22%3Bi%3A1%3Bs%3A32%3A%227ZbdJo4PNpWctkya0y3gYdpLAejvFDhP%22%3B%7D',
        '_ym_d': '1653474392',
        '_ym_uid': '1642530875102218657',
        '_ym_isad': '2',
        '_ga': 'GA1.2.1320184407.1654270288',
        '_gid': 'GA1.2.371852041.1654270288',
        'amp_932404': 'Z3IO6VZbhnnYld1caToh09...1g4l9jlr8.1g4lblg58.0.0.0',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_tgstat_csrk=ea8bb475274bed9c45851dad32a2a837c814eb7c60b7067a3643c5faf90e8466a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22_tgstat_csrk%22%3Bi%3A1%3Bs%3A32%3A%227ZbdJo4PNpWctkya0y3gYdpLAejvFDhP%22%3B%7D; _ym_d=1653474392; _ym_uid=1642530875102218657; _ym_isad=2; _ga=GA1.2.1320184407.1654270288; _gid=GA1.2.371852041.1654270288; amp_932404=Z3IO6VZbhnnYld1caToh09...1g4l9jlr8.1g4lblg58.0.0.0',
        'Origin': 'https://tgstat.ru',
        'Referer': 'https://tgstat.ru/channels/search',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.70',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Opera GX";v="86"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        '_tgstat_csrk': '-JnBgNhLC4oTHUQTyH6C7DNsWtc65VyaUCTYR8bGOUTPw6PkkiQ_2l1tE3C8FfuNAxVpsGOBLNYRQbIxgIJRFA==',
        'view': 'card',
        'sort': 'participants',
        'q': key,
        'inAbout': [
            '0',
            '1',
        ],
        'categories': '',
        'countries': '',
        'languages': '',
        'channelType': '',
        'age': '0',
        'err': '0',
        'participantsCountFrom': '',
        'participantsCountTo': '',
        'avgReachFrom': '',
        'avgReachTo': '',
        'avgReach24From': '',
        'avgReach24To': '',
        'ciFrom': '',
        'ciTo': '',
        'isVerified': '0',
        'noRedLabel': '0',
        'noScam': '0',
        'noDead': '0',
        'page': str(page),
        'offset': str(page*30),
    }
    response = requests.post('https://tgstat.ru/channels/search', cookies=cookies, headers=headers, data=data, proxies= proxies, auth =auth)
    return(response.json()['html'])
def create_post_category(category, page):
    cookies = {
        '_tgstat_csrk': 'ea8bb475274bed9c45851dad32a2a837c814eb7c60b7067a3643c5faf90e8466a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22_tgstat_csrk%22%3Bi%3A1%3Bs%3A32%3A%227ZbdJo4PNpWctkya0y3gYdpLAejvFDhP%22%3B%7D',
        '_ym_d': '1653474392',
        '_ym_uid': '1642530875102218657',
        '_ym_isad': '2',
        '_ga': 'GA1.2.1320184407.1654270288',
        '_gid': 'GA1.2.371852041.1654270288',
        'amp_932404': 'Z3IO6VZbhnnYld1caToh09...1g4msl5qg.1g4mt96ms.0.0.0',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_tgstat_csrk=ea8bb475274bed9c45851dad32a2a837c814eb7c60b7067a3643c5faf90e8466a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22_tgstat_csrk%22%3Bi%3A1%3Bs%3A32%3A%227ZbdJo4PNpWctkya0y3gYdpLAejvFDhP%22%3B%7D; _ym_d=1653474392; _ym_uid=1642530875102218657; _ym_isad=2; _ga=GA1.2.1320184407.1654270288; _gid=GA1.2.371852041.1654270288; amp_932404=Z3IO6VZbhnnYld1caToh09...1g4msl5qg.1g4mt96ms.0.0.0',
        'Origin': 'https://tgstat.ru',
        'Referer': 'https://tgstat.ru/channels/search',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.70',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Opera GX";v="86"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        '_tgstat_csrk': 'nJpOerRSS_2yZYmXjQeCUYlvl4ATnET_-4mqK6Xr7Q6rwCwe_j1_rfwV3vT5bPswuRak50r4NLO67MBd46-FXg==',
        'q': '',
        'inAbout': '0',
        'categories': '',
        'categories[]': str(category),
        'countries': '',
        'languages': '',
        'channelType': '',
        'age': '0',
        'err': '0',
        'participantsCountFrom': '',
        'participantsCountTo': '',
        'avgReachFrom': '',
        'avgReachTo': '',
        'avgReach24From': '',
        'avgReach24To': '',
        'ciFrom': '',
        'ciTo': '',
        'isVerified': '0',
        'noRedLabel': [
            '0',
            '1',
        ],
        'noScam': [
            '0',
            '1',
        ],
        'noDead': [
            '0',
            '1',
        ],
        'page': str(page),
        'offset': str(page*30),
    }
    response = requests.post('https://tgstat.ru/channels/search', cookies=cookies, headers=headers, data=data, proxies= proxies, auth = auth)
    return (response.json()['html'])
def get_links(response):
    response = BeautifulSoup(response, features= 'lxml')
    qq = response.find_all('a', class_ ='text-body')
    dd = []
    for i in qq:
        dd.append('t.me/'+(i.get('href')).split('/')[-1][1:])
    return(dd)
def get_all_links_by_keyword(keyword):
    ss = []
    counter = 0
    while True:
        try:
            response = createpost_key(keyword, counter)
            ss += get_links(response)
            counter +=1
        except KeyError:
            break
    f = open(keyword + '.txt', 'w')
    f.write("\n".join(ss))
    f.close()
    print(ss)
    print(len(ss))
    return(ss)
def get_all_links_by_categories(category):
    ss = []
    counter = 0
    while True:
        try:
            response = create_post_category(categories[category], counter)
            ss += get_links(response)
            counter +=1
        except KeyError:
            break
    f = open(category+'.txt', 'w')
    f.write("\n".join(ss))
    f.close()
    print(ss)
    print(len(ss))
    return(ss)
while True:
    print('Введите "1" для поиска по ключевому слову.\nВведите "2" для поиска по категории:')
    choice = input()
    if choice == "1":
        while True:
            print('Введите "1" для поиска по одному ключевому слову.\nВведите "2" для поиска по ключевым словам из keywords.txt:')
            choice = input()
            if choice == '1':
                print('Введите ключевое слово:')
                keyword = input()
                get_all_links_by_keyword(keyword)
                break
            elif choice == '2':
                file1 = open("keywords.txt", "r", encoding="utf-8")
                while True:
                    line = file1.readline()
                    if not line:
                        break
                    keyword = line.strip()
                    get_all_links_by_keyword(keyword)
                file1.close()
                break
    elif choice == "2":
        for i in categories:
            print(i)
        print('Напишите название одной из представленных выше категорий, по которой будет осуществляться поиск:')
        while True:
            category = input()
            if category in categories:
                get_all_links_by_categories(category)
                break
            else:
                print('Неверно введено название категории.')