import os
from selenium import webdriver
import time
import numpy as np
from bs4 import BeautifulSoup as bf
import pickle
import requests
from stem import Signal
from stem.control import Controller

def renew_connection():
    with Controller.from_port(port = 9051) as controller:  
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

with open('second_urls.pkl', 'rb') as handle:
    song_list2 = pickle.load(handle)

# Scrape Lyrics
artists2 = []
dates2 = []
songs2 = []
titles2 = []

for i in xrange(len(song_list2)):
    print str(i) + '/' + str(len(song_list2)) + ' ' + song_list2[i]
    print len(artists2), len(dates2), len(songs2), len(titles2)
    # renew
    renew_connection()
    print (requests.get('http://icanhazip.com', proxies={'http':'socks5://127.0.0.1:9050', 'https':'socks5://127.0.0.1:9050'})).content
    # vary time between requests so as to not get kicked off
    time.sleep(np.random.exponential(5, 1))
    data = bf(requests.get(song_list2[i]).text)
    
    try:
        # artist info (if multiple artists, append list. else append list of solo artist)
        if len(data.find('span', class_="song_info-info").text.encode('ascii','replace').replace('\n','')) > 0:
            artists2.append([data.find('a', class_="song_header-primary_info-primary_artist").text.encode('ascii','replace') , 
                             data.find('span', class_="song_info-info").text.encode('ascii','replace').replace('\n','')])
        else:
            artists2.append([data.find('a', class_="song_header-primary_info-primary_artist").text.encode('ascii','replace')])
        
        # date info
        dates2.append(data.find('release-date').text.encode('ascii','replace').replace('\n','')[12:])
        
        # lyrics info
        song = ''
        for i in xrange(2, len(data.findAll('a', class_='referent'))):
            song += data.findAll('a', class_='referent')[i].text.encode('ascii','replace').replace(u'\n','. ').replace(u'n\u2019t','nt')
            song += '. '
        import unicodedata
        song = unicodedata.normalize('NFKD', song).encode('ascii', 'ignore')
        songs2.append(song)
        
        # title info
        titles2.append(u''.join(data.find('h1', class_="song_header-primary_info-title").text).encode('utf-8').strip())
    except:
        pass

# Make Corpus
second_corpus = {}
for i in xrange(len(songs2)):
    j = {}
    j['artist'] = artists2[i]
    j['date'] = dates2[i]
    j['lyrics'] = songs2[i]
    second_corpus[titles2[i]] = j

# Pickle
with open('rap_corpus2.pkl', 'wb') as handle:
    pickle.dump(second_corpus, handle)
