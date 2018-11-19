import requests
from bs4 import BeautifulSoup

base_url = 'https://www.toptal.com/developers/san-francisco/scala'

url = base_url
yelp_r = requests.get(url)
yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
businesses = yelp_soup.findAll('div', {'class': 'skill_talent_item-main'})
for biz in businesses:
    title = biz.findAll('a', {'class': 'skill_talent_item-name'})
    print(title)

