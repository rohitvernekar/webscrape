import requests
import re
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
    product_list = soup.findAll('li', {"class": re.compile("sresult lvresult")})
    first_product = product_list[0]
    title = first_product.find('h3', {"class": re.compile("lvtitle")}).text
    available_price = first_product.find('li', {"class": re.compile("lvprice prc")}).span.text
    shipping = first_product.find('li', {"class":re.compile("lvshipping")}).span.span.text
    title_url = first_product.find('h3', {"class": re.compile("lvtitle")}).a['href']
    thumbnail_url = first_product.find('div', {"class":"lvpicinner full-width picW"}).a["href"]
    import pdb;pdb.set_trace()
    if re.search('etrsWpr', first_product[2]):
        toprated_seller = True
    else:
        toprated_seller = False
    
    print title
    print available_price
    print shipping
    print  title_url
    print thumbnail_url
    print toprated_seller
    

        #with open('scraped_html', 'a') as fob:
        #     fob.write(row.prettify())
        #     fob.write("--------------------------------------------------------------------------------------------")    
