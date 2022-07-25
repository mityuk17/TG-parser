import requests
from bs4 import BeautifulSoup
counter = 0
ids = []
url = 'https://tlgrm.ru/channels/'
categories = ['news', 'blogs', 'tech', 'entertainment', 'economics', 'finance', 'crypto', 'education', 'music', 'language', 'business', 'psychology', 'marketing', 'career', 'video', 'books', 'fitness', 'travel', 'art', 'beauty', 'health', 'gaming', 'food', 'sales', 'quotes', 'handicraft', 'adult', 'other']
for category in categories:
    response = requests.get(url+category)
    soup = BeautifulSoup(response.text, 'lxml')
    id_list = soup.find_all('a', class_='channel-card__username')
    for id in id_list:
        ids.append(id.text.strip()[8:])
        counter += 1
    for i in range(4,41):
        response = requests.get(url+category+'?page='+str(i))
        soup = BeautifulSoup(response.text, 'lxml')
        id_list2 = soup.find_all('a', class_ = 'channel-card__username')
        for id in id_list2:
            ids.append(id.text.strip()[8:])
            counter +=1
print(ids)
print(counter)