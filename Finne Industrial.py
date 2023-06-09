from bs4 import BeautifulSoup
import requests
import pandas as pd

page_url = 'https://finne.pl/en/warehouses-search?region=warszawa'
page = requests.get(page_url)

# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())

list_all_span = soup.find_all('span')
# print(f'znalazłem {len(list_all_span)} linków')
# print(list_all_span[24])

prices_of_offices = soup.find_all("span", class_='Badge_badgeWrapper__vM5oj Badge_brand__jjXBM Badge_solid__3pK_I Badge_large__RbHnQ Badge_semiTransparent__YGQ_p Badge_transparent__Aqa8A')
# print(f'znalazłem {len(prices_of_offices)} linków')
# print(prices_of_offices[20])



price = []
for element in prices_of_offices:
    if "sqm" in element.text:
        price.append(element.text)

# print(prices)


addresses_of_offices = soup.find_all("h2", class_="PropertyListItemBox_contentTitle__SbYQX")
# print(f'znalazłem {len(addresses_of_offices)} linków')

cities_of_offices = soup.find_all("h2", class_="PropertyListItemBox_contentTitle__SbYQX")

address = []
for el in addresses_of_offices:
    address.append(el.text)

# print(addresses)

dictionary = dict(zip(address, price))
# print(dictionary)

# for key, value in dictionary.items():
    # print(key + ': ' + value + '\n')

df = pd.DataFrame(list(dictionary.items()), columns=['Address', 'Price'])
print(df)

