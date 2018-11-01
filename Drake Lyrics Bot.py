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

# **** Part 1 **** #  Select a Random Song
x=0
while x < 90:
    value = random.choice(range(0,90))
    song_to_chose = songs_list_clean[value]
    x +=1
r = requests.get(f'http://www.metrolyrics.com/{song_to_chose}.html').content
soup = BeautifulSoup(r, 'html.parser')
verse = soup.find_all("p",class_="verse")

# Remove Html Tags From Chosen Song
versez = []
verses = []
for tags in verse:
    versez.append(tags.text.strip())
    for lists in versez:
        verses.append(lists.replace('\n',' ').split(',')) #Replace Line Breaks From Versez To Nothing and split lines by commas

# **** Part 2 **** #  Selecting a Random Line

linez = []
for multiples in verses:
    for lines in multiples:
        linez.append(lines)
# Random Line
while x < len(linez):
    line_value = random.choice(range(0,len(linez)))
    x +=1
twitter.update_status(status=linez[line_value].upper())
