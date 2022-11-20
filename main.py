import requests
from bs4 import BeautifulSoup
import lxml
import fake_useragent


user = fake_useragent.UserAgent().random

headers = {'user-agent': user}

session= requests.Session()

page= int(input('Input page '))
url_input = input('Input URL categories ')
for j in range(1, page+1):
    url = f'{url_input}p-{j}'
    # url = 'https://hard.rozetka.com.ua/ua/monitors/c80089'
    response = session.get(url, headers-headers)

    soup = BeautifulSoup (response.text, "lxml")


#https://hard.rozetka.com.ua/ua/monitors/c80089/



    all_product = soup.find('ul', class_='catalog-grid ng-star-inserted')
    print(all_product)
    # product_list = all_product.find('div', class_='catalog-grid-cell catalog-grid_cell_type_slin ng-star-inserted')
    # print(product_list)

    # for i in range(len(product_list)):
        #product = product_list[i].find('a', class="goods-tile_heading ng-star-inserted').text
        #url product = product list[i].find("a", "href": "https://hard.rozetka.com.ua/ua/samsung_lc27g75tesixci/p253529003/"}}
        #try:
            #new_price = product list[i].find('div', class ='ng-star-inserted').text
            #with open('myproduct.txt', '', encoding="UTF-8') as file:" \
                #"file.write(f(product) New price (new_price} \n")
#except AttributeError: