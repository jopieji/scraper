import requests
from bs4 import BeautifulSoup
import pickle

# zillow, realtor.com, and redfin all block scrapers from looking into their site's html content
# probably because they want ad revenue

# I want to eventually have command line arguments for adding urls to a list of urls and then being able to scrape a particular page for an item's 
# price based on command line input. So long as the HTML structure is consistent, this should work just fine
# finally, we can send an email or text (using Twilio) to our end user when we find a price below the lower bound they enter into the command line

# currently, my focus is making this app more user friendly. I will get a full MVP up before trying to implement a GUI

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
scrape = False

# base test URL
neweggURL = "https://www.newegg.com/arduino-a000066/p/N82E16813450001"

# array of URLs
# TODO: Maybe make this into a dictionary
# have the indicies be the keys, then have a list of the name, limit price, and URL as the values
# TODO: Use input checking to make sure the URLs are from Newegg
neweggURLArray = [
"https://www.newegg.com/arduino-a000066/p/N82E16813450001", 
"https://www.newegg.com/g-skill-16gb-288-pin-ddr4-sdram/p/N82E16820231941",
"https://www.newegg.com/p/2S7-01JX-00003",
"https://www.newegg.com/p/3D0-002J-00045"
]

# dict of item names for print statement 
# TODO: I am not storing this data/updating it when user adds new items/names/prices
# TODO: Include Prices in this dictionary
urlItemNameDict = {
    0: "Arduino Base Unit",
    1: "G-Skill RAM 16 GB",
    2: "Arduino Mechanical Arm",
    3: "MicroPython Board"
}

# need to phase this out. use pickle for everything for consistency
sampleurlItemNameDict = {
    0: ["https://www.newegg.com/arduino-a000066/p/N82E16813450001", "Arduino Base Unit", 25],
    1: ["https://www.newegg.com/g-skill-16gb-288-pin-ddr4-sdram/p/N82E16820231941", "G-Skill RAM 16 GB", 59],
    2: ["https://www.newegg.com/p/2S7-01JX-00003", "Arduino Mechanical Arm", 20], 
    3: ["https://www.newegg.com/p/3D0-002J-00045", "MicroPython Board", 15]
}

def prompt():
    appOption = int(input("\nWould you like to \n(1) scrape \n(2) add a url \n(3) delete a url \n(4) edit a limit price \n(5) View Current URLs\n(6) Exit\n\n"))
    return appOption

# pickle object storage for url dict
def pickleDictDataAdd(dataToStore):
    with open("urlDict.pickle", "wb") as f:
        pickle.dump(sampleurlItemNameDict, f)

# function to add items to data dict
def addDictItem():
    index = len(pickleDictDataRetrieve().keys())
    listToAdd = []
    url = input("Enter a URL to add:\n")
    name = input("What is the item called?\n")
    limitPrice = input("What is the limit price you want scrape for?\n")
    listToAdd.append(url)
    listToAdd.append(name)
    listToAdd.append(int(limitPrice))
    sampleurlItemNameDict.update({index: listToAdd})
    # might be inefficient
    pickleDictDataAdd(sampleurlItemNameDict)

# retreive pickled dict data to print options to choose from and retrieve urls
# no need for this right now; wasn't working to print
# might work now if I use correct looping syntax for dictionary
def pickleDictDataRetrieve():
    with open("urlDict.pickle", "rb") as f:
        return pickle.load(f)
    

# pickle object storage for url array
# maintains edits after user inputs and deletes items
def pickleDataAdd(toStore):
    with open("urlArr.pickle", "wb") as f:
        pickle.dump(toStore, f) 

# retrieves pickled array data to print options to choose from
def pickleDataRetreive():
    with open("urlArr.pickle", "rb") as f:
        arr_toPrint = pickle.load(f)
    return arr_toPrint

# function that prints the urls in a neat format
# might need alter this to handle dictionary data so the URLs can be named by the end user; also include limit prices for each item
def printUrls():
    for k, v in sampleurlItemNameDict.items():
        print(f"{k + 1}: {v[1]} Price: {v[2]}")

def printUrlsWithPickleObject():
    print()
    for key, val in pickleDictDataRetrieve().items():
        print(f"{key + 1}: {val[1]} Price: {val[2]}")

def updateLocalDict():
    with open("urlDict.pickle", "rb") as f:
        x = pickle.load(f)
    sampleurlItemNameDict.update(x)

def deleteItem():
    printUrlsWithPickleObject()
    print()
    keyToRemove = int(input("What item do you want to delete? (use number):\n"))
    update = pickleDataRetreive()
    update.pop(keyToRemove - 1)
    pickleDictDataAdd(update)
    print("Success! URL Removed")

    

# might want to change this to a function so we can do more than 1 action in a single run
# works fine but kinda off code.
while noExit:
    #pickleDictDataAdd(sampleurlItemNameDict)
    switch = prompt()
    if switch == 1:
            scrape = True
    elif switch == 2:
        addDictItem()
        print("URL sucessfully added!")
    elif switch == 3:
        # TODO: "Add the logic here to print urls and delete by index"
        deleteItem()
    elif switch == 4:
        # TODO: "Similar logic to above, but able to change the limit price for notifications"
        break
    elif switch == 5:
        printUrlsWithPickleObject()
    elif switch == 6:
        noExit = False
        break
    # TODO: Maybe make this into a function that is called when (1) selected
    while scrape:
        # TODO: Add logic to scrape all elements in sequence
        urlIndex = int(input("What URL would you like to scrape?\n")) - 1
        # TODO: Add print urls function (with numbers)
        # TODO: Put full scrape sequence in a function
        # the request to get the webpage's HTML content 
        urlArray = sampleurlItemNameDict.get(urlIndex)     
        neweggReq = requests.get(urlArray[0], headers=headers)
        # using bs4 to parse the html content
        soupNewegg = BeautifulSoup(neweggReq.content, "html.parser")
        # finding any dollar signs in the html (the first dollar sign more specifically)
        findDollar = soupNewegg.find_all(text="$")
        # find the parent div of the first dollar sign (usually the title dollar sign/price we see most prominently)
        costParent = findDollar[0].parent
        # picking out the text from the element we want to, in this case 'strong'
        costTag = costParent.find("strong")
        # just printing the cost for now when we run the script // change this to send notifications if int(costTag) < limit
        print(f"\nDollar cost of {urlArray[1]}: ${costTag.string}")
        if urlArray[2] > int(costTag.string):
            print("Low price alert!")
        else:
            print("Price above threshold. Check back later!")
        scrape = False
        print("\n" + "="*55)


# maybe add datetime to auto email/text
# make sure to only send email/text when the price is below our threshold

