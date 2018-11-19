import requests
from bs4 import BeautifulSoup
from selenium import webdriver
url = 'https://www.chrisburkard.com'
w_url =requests.get(url)

driver = webdriver.Firefox()
driver.get('https://www.chrisburkard.com')
html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html.text,'html.parser')
print(len(sel_soup.findAll('img')))
images = []
for i in sel_soup.findAll('img'):
    print(i)
    src = i['src']
    images.append(src)