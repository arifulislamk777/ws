
import requests
from bs4 import BeautifulSoup

base_url = 'https://clutch.co/ca/web-designers?page='


current_page = 0

while current_page <201:
    print(current_page)
    url = base_url + str(current_page)
    yelp_r = requests.get(url)
    yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
    businesses = yelp_soup.findAll('section', {'class': 'main-content-wrapper'})
    file_path = 'yelp-{loc}-2'.format(loc=current_page)
    with open(file_path, "a") as textfile:
        businesses = yelp_soup.findAll('h3', {'class': 'company-name'})
        for biz in businesses:
            title = biz.findAll('a', {'target': '_blank'})[0].text
            print(title)

            new_address = biz.findAll('li', {'class':'website-link website-link-a'})
            print (new_address.get('href'))
            # second_line = ''
            # first_line = ''
            # try:
            #     new_address = biz.findAll('li', {'class': 'website-link website-link-a'})[0]
            #     address = new_address.findAll('href')[0]
            #     for item in address:
            #         if "br" in str(item):
            #             second_line += item.getText().strip("\n\t\r")
            #         else:
            #             first_line = item.strip("\n\t\r")
            #     print(first_line)
            #     print(second_line)
            # except:
            #     pass
            # print('\n')
            # try:
            #     phone = biz.findAll('i', {'class': 'item __color6a'})[0].getText().strip("\n\t\r")
            # except:
            #     phone=None
            # print(phone)
            # page_line = "{title}\n {address_1} \n {address_2} \n {phone}\n\n".format(
            #     title=title,
            #     address_1=first_line,
            #     address_2=second_line,
            #     phone=phone
            # )
            # textfile.write(page_line)
    current_page +=1




# work with Django
# obj = SomeModel()
# obj.title = title
# obj.line_1= first_line
# obj.save()
























