# Web Scraper with Notification System
### Jake Opie

---

### Overview
This application implements a web scraper via a command line interface. The scraper keeps track of what URLs the user
has stored in their application using pickle, a module that converts Python data structures (or plain text) into binary
for usage across multiple runs. The application stores the name of each item, its URL, and the user's desired trigger
price for notifications. When scraping each URL/webpage, the user can be sent a notification via Twilio SMS when the item's
price is below their trigger price.

I started this project with the intention of scraping house prices on Zillow, and would implement Twilio SMS 
to send me text messages whenever a house was below my price limit. 

Unfortunately, Zillow doesn't allow scrapers, so I couldn't realize this project's full potential/intended use case.

Instead of hitting this wall and giving up on this idea, I decided to implement the web scraping with notifications
application using Newegg URLs. Newegg doesn't block web scrapers, and its many vendors are in fierce competition,
so I felt it was the perfect site to check for price updates (especially given the state of chip inventory in 2022).

### Technology
The technologies I used are Python and the Twilio SMS API.

### Configuring this Application for Yourself
First, start off by making a Twilio account. Once this is done, setup is extremely easy!
https://www.twilio.com/

There are only three environment variables you need to put in a config.py file on your system after you clone this
repository. TWILIO_SID stores your Twilio SID, and TWILIO_AUTH stores your auth token. Make sure to keep these
private! Next, put your phone number (that you want notifications sent to) in a variable named MY_NUM, and 
lastly, your Twilio from phone number in TWILIO_NUM.

Once this is all done, your app should work perfectly!

---
### Future Plans
In the future, I'd like to add restock notifications. Graphics cards are at a premium right now, and getting text alerts for
restocks can help out a lot of hobbyists and professionals to get the gear they need!

---

Feel free to reach out to me with any issues or questions.
