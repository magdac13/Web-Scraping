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

html_text = requests.get('https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/warszawa?distanceRadius=0&market=ALL&locations=%5Bcities_6-26%5D&viewType=listing&lang=pl&searchingCriteria=sprzedaz&searchingCriteria=mieszkanie&searchingCriteria=cala-polska').text

soup = BeautifulSoup(html_text, 'lxml')
prices = soup.find_all('span', class_='css-s8wpzb e1brl80i1')
for price in prices:
    print(price.text)


#sellers = prices.find_all('p', class_='css-e80z7t e1dxhs6v4')
#for seller in sellers:
    #print(seller.text)
