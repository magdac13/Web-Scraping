import time

from bs4 import BeautifulSoup
import requests

#with open('movies.html', 'r') as html_file:
    #content = html_file.read()

    #soup = BeautifulSoup(content, 'lxml')
    #courses_html_tags = soup.find_all('p')
    #for course in courses_html_tags:
        #print(course.text)

    #soup = BeautifulSoup(content, 'lxml')
    #course_cards = soup.find_all('div', class_='card')
    # class_ żeby nie nachodziło na nazwę class

    #for course in course_cards:
        #course_name = course.h5.text
        #course_price = course.a.text
        #print(course_price)


# Pobieranie treści html strony Otodom:

page_url = 'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/warszawa?distanceRadius=0&market=ALL&locations=%5Bcities_6-26%5D&viewType=listing&lang=pl&searchingCriteria=sprzedaz&searchingCriteria=mieszkanie&searchingCriteria=cala-polska'
page = requests.get(page_url)

# Możemy wydrukować zawartość HTML strony za pomocą właściwości content:

# print(page.content)

# Tworzenie klasy BeautifulSoup:

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify()) # ładniejszy sposób na wyświetlenie


# możemy użyć metody find_all, która znajdzie wszystkie wystąpienia tagu na stronie
list_all_span = soup.find_all('span')
print(f'znalazłem {len(list_all_span)} linków')
print(list_all_span[24])


prices_of_flats = soup.find_all("span", class_='css-s8wpzb e1brl80i1')
print(f'znalazłem {len(prices_of_flats)} linków')

prices = []
for element in prices_of_flats:
    if element.text.endswith("zł"):
        prices.append(element.text)

print(prices)


def find_price_per_m():

    strong = soup.find_all("strong")
    for element in strong:
        if element.text.endswith("zł/m²"):
            print(element.text)


print(find_price_per_m())


soup = BeautifulSoup(html_text, 'lxml')
prices = soup.find_all('span', class_='css-s8wpzb e1brl80i1')
for price in prices:
    print(price.text)


#sellers = prices.find_all('p', class_='css-e80z7t e1dxhs6v4')
#for seller in sellers:
    #print(seller.text)
