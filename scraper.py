import requests
from bs4 import BeautifulSoup
import datetime

import html5lib


URL = "https://www.zillow.com/homedetails/15922-Woodingham-Dr-Detroit-MI-48238/88348158_zpid/"
KEY_URL = "https://iqunix.store/collections/f96/products/f96-coral-sea-wireless-mechanical-keyboard"
pelosi = "https://tradytics.com/senate-individual"

SAF_USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15"
EDGE_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'

headers = {"user-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'}

page_data = requests.get(URL, headers=headers)
keyquest = requests.get(KEY_URL, headers=headers)
housereq = requests.get(pelosi, headers=headers)

soup2 = BeautifulSoup(housereq.content, "html.parser")

soup = BeautifulSoup(keyquest.content, "html.parser")

classWoodingham = "hdp__sc-reo5z7-1 jdeidP"
classOtherHouse = "hdp__sc-reo5z7-1 jdeidP"

housepr = soup2.find(id="senate_market_table_wrapper")

print(housepr)

price = soup.find(id="ProductPrice-4141030539324")
price2 = soup.find('span', class_="money").get_text()

#print(scrapedPrice)
print(price2)

### alternate, more simple solution
# checking arduino prices
# our url we want to scrape
neweggURL = "https://www.newegg.com/arduino-a000066/p/N82E16813450001"

# the request to get the webpage's HTML content
neweggReq = requests.get(neweggURL, headers=headers)

# using bs4 to parse the html content
soupNewegg = BeautifulSoup(neweggReq.content, "html.parser")

# finding any dollar signs in the html (the first dollar sign more specifically)
findDollar = soupNewegg.find_all(text="$")

# find the parent div of the first dollar sign (usually the title dollar sign/price we see most prominently)
costParent = findDollar[0].parent

# picking out the text from the element we want to, in this case 'strong'
costTag = costParent.find("strong")

# just printing the cost for now when we run the script
print(f"Dollar cost of arduino: ${costTag.string}")

# maybe add datetime to auto email/text
# make sure to only send email/text when the price is below our threshold



