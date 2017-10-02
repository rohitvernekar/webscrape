import requests
from BeautifulSoup import BeautifulSoup
def get_html():
    response = requests.get('https://www.ebay.in/sch/Mobile-Phones-/15032/i.html')
    html = response.content
    return html


def get_soup(html):
    return BeautifulSoup(html)


def find_tag(soup, id_val):
    div_root_block = soup.findAll('div', attrs = {'id': id_val})
    return div_root_block
    
if __name__ == "__main__":
    html = get_html()
    soup = get_soup(html)
    root_block = find_tag(soup, 'ResultSetItems')
    for row in root_block:
        with open('scraped_html', 'a') as fob:
             fob.write(row.prettify())
             fob.write("--------------------------------------------------------------------------------------------")    
