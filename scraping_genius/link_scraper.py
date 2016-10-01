"""
Searches artists on RapGenius and scrapes links for ~200 songs per artist. Links are written to pickle
"""

from selenium import webdriver
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bf
import time
import os
import pickle

"""
Artist list copied from: https://en.wikipedia.org/wiki/List_of_hip_hop_musicians
List copied to "rappers.csv" file
"""

# Create list of artists from csv file via pandas
artist_frame = pd.read_csv('/Users/El-Razi/Downloads/rappers.csv', header=None, names=['Artist'])
artist_list = [artist for artist in artist_frame['Artist']]

# Selenium setup
chromedriver = "/Users/El-Razi/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver


"""
Open Chrome, navigate to RapGenius, search for a rapper, pagedown 20 times (~200 songs), append all song links from html to a list of lists [artist1,[songs],artist2,[songs],...]
"""

songlinks_by_artist = []
count = 1
driver = webdriver.Chrome(chromedriver)
for artist in artist_list:
    
    # tracking position in for loop
    print str(count) + ' of ' + str(len(artist_list)), artist
    
    # RapGenius search
    driver.get('http://genius.com/search?q=' + artist.replace(' ','+'))
    
    # autoscroll (wait random amount of time between requests, so as not to get banned by RapGenius)
    for i in range(20):
        time.sleep(np.random.exponential(5, 1))
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except:
            continue
    song_sourcecode = bf(driver.page_source)
    song_link_list = []
    
    # parse html for song links, append to "song_link_list", add artist and songlinks to "songlinks_by_artist"
    for link in data.find_all('li', class_ = 'search_result'):
        song_link_list.append(str(link.a.get('href')))
    songlinks_by_artist.append([artist, song_link_list])
    
    count += 1
    print 'Number of songs collected: %s' % (len(song_link_list))
driver.close()

with open('songlinks_by_artist.pkl', 'wb') as handle:
    pickle.dump(songlinks_by_artist, handle)

# Collapse list of lists into list containing only song URLs
song_master_list = sum([j for i,j in songlinks_by_artist],[])

# Create match set of artists to check URLs against (legitimate song URLs will match)
artist_match_set = [artist.split()[0] for artist in artist_list]

# Need to separate RapGenius blog posts from actual lyrics. Filtering out links which do not match lyric format
final_song_links = filter(lambda x: x.split('m/')[1].split('-')[0] in artist_match_set, song_master_list)

with open('final_song_links.pkl', 'wb') as handle:
    pickle.dump(final_song_links, handle)
