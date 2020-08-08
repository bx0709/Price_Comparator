import re
import requests
from bs4 import BeautifulSoup

def get_local_price(model_number):

    a=requests.get("https://www.amitbookdepot.com/.php?keyword="+model_number).text
    soup=BeautifulSoup(a,'html.parser')
    extract=soup.find('html')

    avail_check=extract.find_all('div',class_='count-pagination')

    if 'No record' in avail_check[0].string:
        return str(0)
    else:
        a=extract.find_all('span',class_ = 'PricesalesPrice')
        return a[0].string



