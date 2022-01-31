import requests
from bs4 import BeautifulSoup


URL = "https://www.zillow.com/homedetails/15922-Woodingham-Dr-Detroit-MI-48238/88348158_zpid/"

SAF_USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15"
EDGE_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'

headers = {"user-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'}

page_data = requests.get(URL, headers=headers)
pd2 = requests.get("https://www.amazon.com/Edifier-R1280DB-Bluetooth-Bookshelf-Speakers/dp/B0719C132V/ref=sr_1_1_sspa?crid=2H6HZXNSMNO3U&keywords=bookshelf%2Bspeakers&qid=1643599646&sprefix=bookshelf%2Bspeaker%2Caps%2C88&sr=8-1-spons&smid=A23AS8PFN4IRUQ&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTlJSVEhaNERDSFpCJmVuY3J5cHRlZElkPUEwMzYyNzM5MkhWNVY2OUtaUk9WQyZlbmNyeXB0ZWRBZElkPUEwNzYzNTM2MkRHSUpTQlNSUlhURSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1", headers=headers)
#print(page_data.status_code)
#print(pd2.text)
#print(pd2)

soup = BeautifulSoup(page_data.text, "html.parser")

classWoodingham = "hdp__sc-reo5z7-1 jdeidP"
classOtherHouse = "hdp__sc-reo5z7-1 jdeidP"

scrapedPrice = soup.find(id="gpt-ad-801499d4-80b9-4d0b-a056-6ffbd0b01b2b-config")

price = soup.find('span', {"class": "a-price-whole"})

print(scrapedPrice)
print(price)

