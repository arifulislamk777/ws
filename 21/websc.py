
import requests
from bs4 import BeautifulSoup

base_url = 'https://appsecus2018.sched.com/directory/attendees?iframe=no&w=100%&sidebar=yes&bg=no'

yelp_r = requests.get(base_url)
yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
businesses = yelp_soup.findAll('div', {'class': 'sched-container-people'})
# file_path = 'yelp-{loc}-2'.format(loc=businesses)
# with open(file_path, "a") as textfile:
businesses = yelp_soup.findAll('h2')
for biz in businesses:
        title = biz.findAll('a')[0].text
        print(title)
        address = biz.findAll('div')[0].text
        print(address)
        # second_line = ''
        # first_line = ''
        # try:
        #     address = biz.findAll('div',{'class': 'sched-event-details-position'})[0].contents
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
        #     phone = biz.findAll('div', {'class': 'sched-event-details-position'})[0].getText().strip("\n\t\r")
        # except:
        #     phone = None
        # print(phone)
                # page_line = "{title}\n {address_1} \n {address_2} \n {phone}\n\n".format(
                #     title=title,
                #     address_1=first_line,
                #     address_2=second_line,
                #     phone=phone
                # )
                # textfile.write(page_line)




