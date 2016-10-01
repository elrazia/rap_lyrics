"""
Script written to parse through html files in "songs" directory and pull artist, date, title, and lyrics from each song.
Corpus is formatted as a dictionary of dictionaries (for MongoDB).
"""

from bs4 import BeautifulSoup as bf
import os
import pickle

artists = []
dates = []
songs = []
titles = []
rap_corpus = {}
count = 0

for filename in os.listdir('/Users/El-Razi/ds/metis/git/rap_lyrics/songs/'):
    count += 1
    
    if count%1000==0:
        with open('corpus.pkl', 'wb') as handle:
            pickle.dump(rap_corpus, handle)
    with open('/Users/El-Razi/ds/metis/git/rap_lyrics/songs/' + filename) as f:
        data = bf(f,'lxml')
    print str(count) + ' / ' + str(len(os.listdir('/Users/El-Razi/ds/metis/git/rap_lyrics/songs/')))
    
    try:

        # artist info (if multiple artists, append list. else append list of solo artist)
        if len(data.find('span', class_="song_info-info").text.encode('ascii','replace').replace('\n','')) > 0:
            artists.append([data.find('a', class_="song_header-primary_info-primary_artist").text.encode('ascii','replace') , 
                            data.find('span', class_="song_info-info").text.encode('ascii','replace').replace('\n','')])
        else:
            artists.append([data.find('a', class_="song_header-primary_info-primary_artist").text.encode('ascii','replace')])

        # date info
        dates.append(data.find('release-date').text.encode('ascii','replace').replace('\n','')[12:])

        # lyrics info
        song = ''
        for i in xrange(2, len(data.findAll('a', class_='referent'))):
            song += data.findAll('a', class_='referent')[i].text.encode('ascii','replace').replace(u'\n','. ').replace(u'n\u2019t','nt')
            song += '. '
        import unicodedata
        song = unicodedata.normalize('NFKD', song).encode('ascii', 'ignore')
        songs.append(song)

        # title info
        titles.append(u''.join(data.find('h1', class_="song_header-primary_info-title").text).encode('utf-8').strip())
        print 'success'
        
        # if above successful, add to corpus
        j = {}
        j['artist'] = artists[-1]
        j['date'] = dates[-1]
        j['lyrics'] = songs[-1]
        rap_corpus[titles[-1]] = j
        
    except:
        print 'failure'
        pass

with open('corpus.pkl', 'wb') as handle:
            pickle.dump(rap_corpus, handle)
