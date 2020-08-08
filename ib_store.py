import re
import requests
from bs4 import BeautifulSoup

def get_online_price(model_number):

    a=requests.get("https://www.indiabookstore.net/isbn/"+model_number).text
    soup=BeautifulSoup(a,'html.parser')
    links=soup.find('html')
    a=links.find_all('a',class_ = 'bookPageBuyLink')
    if a==[]:
        return str(0)
    else:
        return a[0].string,a[1].string
