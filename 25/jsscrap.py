import requests
from bs4 import BeautifulSoup
from selenium import webdriver
url = 'https://www.chrisburkard.com'
w_url =requests.get(url)
url_soup = BeautifulSoup(w_url.text,'html.parser')

print(url_soup.findAll("img"))



driver = webdriver.Firefox()
driver.get(url)
html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html.text,'html.parser')
print(len(sel_soup.findAll('img')))
images = []
for i in sel_soup.findAll('img'):
    print(i)
    src = i['src']
    images.append(src)