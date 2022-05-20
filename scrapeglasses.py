from proxycrawl import ScraperAPI

api = ScraperAPI({'token': 'rlPfwxzqQAkX0OH25JNXpg'})

targetURL = 'https://www.yelp.com/search?find_desc=Coffee+Shop&find_loc=New+York%2C+NY%2C+United+States'

response = api.get(targetURL, {'autoparse': 'true'})

if response['status_code'] == 200:
    print(response['body'])


"""from proxycrawl import ScraperAPI

api = ScraperAPI({'token': 'USER_TOKEN'})

URL = 'https://www.google.com/search?q='
KW = input('Please Enter Your City Name: ').lower()

targetURL = URL + KW.replace(' ', '-') + '-weather'

response = api.get(targetURL, {'autoparse': 'true'})

if response['status_code'] == 200:
    print(response['body'])"""

"""from autoscraper import AutoScraper
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests

#Install Driver
driver = webdriver.Chrome(ChromeDriverManager().install())

url='https://ereditaeyewear.com/collections/chopard-optical'"""

"""url = 'https://ereditaeyewear.com/collections/chopard-optical/products/chopard-vchf55'

wanted_list = ['CHOPARD', 'VCHF55', '$1,161.30s', 'MEN', 'METAL', 'RECTANGLE', '0300-Gold 0300', '08FF-Grey Gold 08Ff', '08FF-Grey Gold 08Ff', '56/18/145', 'https://cdn.shopify.com/s/files/1/0541/2467/5232/products/VCHF55GOLD_b045ee06-0d73-46c3-8951-aedc7fabfccc_700x.jpg?v=1636083265']

scraper = AutoScraper()
scraper.build(url, wanted_list)
scraper.get_result_similar('https://ereditaeyewear.com/collections/chopard/products/chopard-vchf56', grouped=True)

# Give it a file path
scraper.save('glasses')
scraper.load('glasses')"""
