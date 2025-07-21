import json
import time
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.yad2.co.il/realestate/forsale?page=2')
input()
script = driver.find_element(By.ID, "__NEXT_DATA__")
# data = json.loads(script.text)

# print(data)

# print(script.get_attribute('innerHTML'))
data = json.loads(script.get_attribute('innerHTML'))
with open('data.json', mode='w')as file:
    json.dump(data, file, indent=2)
# pprint(data)

flats = list(filter(lambda x: x['queryKey'][0] == 'realestate-forsale-feed',data['props']['pageProps']['dehydratedState']['queries']))[0]['state']['data']

print(flats)
