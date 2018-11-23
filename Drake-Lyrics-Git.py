import requests
from bs4 import BeautifulSoup
import numpy as np
import random
from twython import Twython
import re
import time

# Define twitter api variables
app_key = 'API-Key'
app_secret = 'API-Secret-Key'
oauth_token = 'Access Token'
oauth_token_secret = 'Access Token Secret'

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

#Request to get the page where all the songs with lyrics are found (page1)
r_song = requests.get('http://www.metrolyrics.com/drake-lyrics.html').content
soup_song = BeautifulSoup(r_song, 'html.parser')

# Get a List of Only Drake Songs In Appropriate Html Format
songs_1 = soup_song.find_all('td')
song_list_dirty = re.findall('(searcht........................................)',str(list(songs_1)))

# Clean Html Format & Add -drake To The End
print(f'Before Cleaning:{song_list_dirty[0:1]}')
songs_list_clean = [song_title.split('-drake',1)[0].replace('searcht:','') +
'-drake' for song_title in song_list_dirty]
print(f'After Cleaning: {songs_list_clean[0:2]}')
print(f'The Number of songs on the first page of MetroLyris: {len(songs_list_clean)}')



while True:
    dirty_verse = []
    clean_verse = []
    linez = []
    # ****** Part 1 ******* #
    #Select a random Drake song from MetroLyris
    value = random.choice(np.arange(0,len(songs_list_clean)))
    song_to_chose = songs_list_clean[value]
    r = requests.get(f'http://www.metrolyrics.com/{song_to_chose}.html').content
    soup = BeautifulSoup(r, 'html.parser')
    verse = soup.find_all("p",class_='verse')
    #Remove Html Tags From Chosen Song
    for tags in verse:
        dirty_verse.append(tags.text.strip())
        #Dirty_verse is Now a List of Lists with a Drake Verse
        for lists in dirty_verse:
            clean_verse.append(lists.replace('\n',' ').split(','))
            #Replace Line Breaks From Dirty_verse To Empty & Clean Stuff Up
            for multiples in clean_verse:
                #Break Up The List of Lists into 1 List with individual Lines
                for lines in multiples:
                    linez.append(lines)


    # ****** Part 2 ******* #
    #Select a random line from verse of corresponding song
    #Generate a random number based on the number of lines in the verse
    line_value = random.choice(np.arange(1,len(linez)))
    line_to_print = linez[line_value]
    twitter.update_status(status=line_to_print.upper())
    time.sleep(2000)
