import requests
from bs4 import BeautifulSoup
import pickle

# zillow, realtor.com, and redfin all block scrapers from looking into their site's html content
# probably because they want ad revenue

# I want to eventually have command line arguments for adding urls to a list of urls and then being able to scrape a particular page for an item's 
# price based on command line input. So long as the HTML structure is consistent, this should work just fine
# finally, we can send an email or text (using Twilio) to our end user when we find a price below the lower bound they enter into the command line

KEY_URL = "https://iqunix.store/collections/f96/products/f96-coral-sea-wireless-mechanical-keyboard"

"""
SAF_USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15"
EDGE_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'
"""
headers = {"user-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'}

# checking newegg prices
# on whatever url user has stored and selects

# initialize while loop conditions
noExit = True
app = False

# base test URL
neweggURL = "https://www.newegg.com/arduino-a000066/p/N82E16813450001"

# array of URLs
neweggURLArray = [
"https://www.newegg.com/arduino-a000066/p/N82E16813450001", 
"https://www.newegg.com/g-skill-16gb-288-pin-ddr4-sdram/p/N82E16820231941",
"https://www.newegg.com/p/2S7-01JX-00003",
"https://www.newegg.com/p/3D0-002J-00045"
]

# dict of item names for print statement 
urlItemNameDict = {
    0: "Arduino Base Unit",
    1: "G-Skill RAM 16 GB",
    2: "Arduino Mechanical Arm",
    3: "MicroPython Board"
}

def prompt():
    appOption = int(input("\nWould you like to \n(1) scrape \n(2) add a url \n(3) delete a url \n(4) edit a limit price \n(5) exit\n"))
    return appOption

# pickle object storage for url array
# maintains edits after user inputs and deletes items
def pickleDataAdd(toStore):
    with open("urlArr.pickle", "wb") as f:
        pickle.dump(toStore, f) 

def pickleDataRetreive():
    with open("urlArr.pickle", "rb") as f:
        arr_toPrint = pickle.load(f)
    return arr_toPrint

# might want to change this to a function so we can do more than 1 action in a single run
# works fine but kinda off code.
while noExit:
    switch = prompt()
    if switch == 1:
            app = True
    elif switch == 2:
        urlToEnter = input("Paste in your url: ")
        # can i add a tester to make sure its a valid URL? Maybe use regex, or just check the first 'x' characters to be https://www.newegg.com/""
        neweggURLArray.append(urlToEnter)
        # using pickle to store the new array
        pickleData(neweggURLArray)
        print("URL sucessfully added!")
    elif switch == 3:
        # TODO: "Add the logic here to print urls and delete by index"
        break
    elif switch == 4:
        # TODO: "Similar logic to above, but able to change the limit price for notifications"
        break
    elif switch == 5:
        noExit = False
        break
    while app:
        # TODO: Add logic to choose what element we want to scrape for, or add logic to scrape every val in neweggURLArray
        urlIndex = int(input("What URL would you like to scrape?\n")) - 1
        # TODO: Add print urls function (with numbers )
        # the request to get the webpage's HTML content        
        neweggReq = requests.get(neweggURLArray[urlIndex], headers=headers)
        # using bs4 to parse the html content
        soupNewegg = BeautifulSoup(neweggReq.content, "html.parser")
        # finding any dollar signs in the html (the first dollar sign more specifically)
        findDollar = soupNewegg.find_all(text="$")
        # find the parent div of the first dollar sign (usually the title dollar sign/price we see most prominently)
        costParent = findDollar[0].parent
        # picking out the text from the element we want to, in this case 'strong'
        costTag = costParent.find("strong")
        # just printing the cost for now when we run the script // change this to send notifications if int(costTag) < limit
        print(f"Dollar cost of {urlItemNameDict.get(urlIndex)}: ${costTag.string}")
        app = False


# maybe add datetime to auto email/text
# make sure to only send email/text when the price is below our threshold

















