"""
Script scrapes html from RapGenius for portion of song links in pickle, utilizing Crawlera credentials to switch IP address
between each request, and writes html to a file in "songs" directory
"""

import pickle
import requests
from requests.auth import HTTPProxyAuth

with open('final_song_links.pkl', 'rb') as handle:
    final_song_links = pickle.load(handle)

# Credentials from crawlera. Used to switch IPs between requests
proxy_host = "proxy.crawlera.com"
proxy_port = "8010"
proxy_auth = HTTPProxyAuth("aa5b6b9d3364479faa46615c8a84aa86", "")
proxies = {"https": "https://{}:{}/".format(proxy_host, proxy_port)}

# Scrape html from song links. Write file to "songs" directory
count = 1
for link in final_song_links[:28177]:
   
    #print progress through list.
    print str(count) + ' / 28177'
    var = str(link.split('.com/')[1]) + '.html'
    try:
        response = requests.get(link, proxies=proxies, auth=proxy_auth, verify='crawlera-ca.crt')
        page_content = response.text.encode('ascii','ignore')
        with open('songs/'+var, 'w') as doc:
            doc.write(page_content)
        print 'Success!'
    except:
        print 'Failure!'
        pass
    count += 1
