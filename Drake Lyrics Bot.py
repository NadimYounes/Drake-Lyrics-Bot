import requests
from bs4 import BeautifulSoup
import numpy as np
import random
from twython import Twython


# Define twitter api variables
app_key = "APP_KEY""
app_secret = "APP_SECRET""
oauth_token = "OAUTH_TOKEN""
oauth_token_secret = "OAUTH_TOKEN_SECRET"

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)



# Get HTML Content using requests and BS
r = requests.get('http://www.metrolyrics.com/headlines-lyrics-drake.html').content
soup = BeautifulSoup(r, 'html.parser')


# Isolate verses from the verse class
verse = soup.find_all("p",class_="verse")
print(f'The number of verses in Headlines: {len(verse)}')


# Remove Html tags from Headlines
versez = []
verses = []
for tags in verse:
    versez.append(tags.text.strip())
    for i in versez:
        verses.append(i.replace('\n',' ').split(',')) #replace line breaks from versesz to just empty

x=0
while x < 54:
    y = random.choice(range(0,55))
    z = random.choice(range(0,3))
    x +=1

twitter.update_status(status= verses[y][z].upper())
