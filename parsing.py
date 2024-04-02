import requests
import bs4
import lxml
from fake_headers import Headers
link = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'

def get_headers():
    return Headers(browser='chrome', os='win').generate()
response = requests.get(link, headers=get_headers())
html = response.text

main_soup = bs4.BeautifulSoup(html, features='lxml')

parent = main_soup.find('div', id='a11y-main-content')


children = parent.find_all('div', class_= 'serp-item serp-item_link')
for child in children:

    href = child.find('a', class_='bloko-link')['href']


    new_response = requests.get(href, headers=get_headers())
    new_html = new_response.text
    new_soup = bs4.BeautifulSoup(new_html, features='lxml')

    desc = new_soup.find('div', class_='g-user-content').text

    if 'Django' in desc or 'Flask' in desc:


        salary = new_soup.find('span', class_='bloko-header-section-2 bloko-header-section-2_lite').text


        company_tag = new_soup.find('a', 'bloko-link')
        company = company_tag.find('span', class_='bloko-header-section-2 bloko-header-section-2_lite').text

        print(href, salary, company)
