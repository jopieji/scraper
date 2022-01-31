import requests
from bs4 import BeautifulSoup

import html5lib


URL = "https://www.zillow.com/homedetails/15922-Woodingham-Dr-Detroit-MI-48238/88348158_zpid/"
KEY_URL = "https://iqunix.store/collections/f96/products/f96-coral-sea-wireless-mechanical-keyboard"

SAF_USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15"
EDGE_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'

headers = {"user-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'}

page_data = requests.get(URL, headers=headers)
keyquest = requests.get(KEY_URL, headers=headers)

soup = BeautifulSoup(keyquest.content, "html.parser")

#print(soup.prettify())

classWoodingham = "hdp__sc-reo5z7-1 jdeidP"
classOtherHouse = "hdp__sc-reo5z7-1 jdeidP"

#scrapedPrice = soup.find(id="gpt-ad-801499d4-80b9-4d0b-a056-6ffbd0b01b2b-config")

price = soup.find(id="ProductPrice-4141030539324")
price2 = soup.find('span', class_="money").get_text()

#print(scrapedPrice)
print(price2)

