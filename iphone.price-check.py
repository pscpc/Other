import requests
import time
from bs4 import BeautifulSoup

###############################################################################################
url="https://www.hepsiburada.com/iphone-12-c-80769001"
headers = {
    ""
    }
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
###############################################################################################



i64gb = soup.find_all('li', {'class':'productListContainer-item', 'id':'i1'}) 
for i64 in i64gb:
    i64_ismi = i64.find('h3', {'data-test-id':'product-card-name'}).get_text()
    i64_fiyati = i64.find('div', {'data-test-id':'price-current-price'}).get_text()

i128gb = soup.find_all('li', {'class':'productListContainer-item', 'id':'i0'}) 
for i128 in i128gb:
    i128_ismi = i128.find('h3', {'data-test-id':'product-card-name'}).get_text()
    i128_fiyati = i128.find('div', {'data-test-id':'price-current-price'}).get_text()

i256gb = soup.find_all('li', {'class':'productListContainer-item', 'id':'i2'}) 
for i256 in i256gb:
    i256_ismi = i256.find('h3', {'data-test-id':'product-card-name'}).get_text()
    i256_fiyati = i256.find('div', {'data-test-id':'price-current-price'}).get_text()


print("\n",i64_ismi,"  ",i64_fiyati)
print("\n",i128_ismi," ",i128_fiyati)
print("\n",i256_ismi," ",i256_fiyati)

time.sleep(50)


