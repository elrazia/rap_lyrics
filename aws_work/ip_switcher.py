#!/usr/bin/env python

'''
Written to run in parallel with Tor. Script renews IP and shows new IP every 4 seconds.
Purpose is to avoid getting kicked off of a website while scraping large amounts of data
'''

from stem import Signal
from stem.control import Controller
import requests
import time

# change IP
def renew_connection():
	with Controller.from_port(port = 9051) as controller:
		controller.authenticate()
		controller.signal(Signal.NEWNYM)
# show IP
def request():
	proxies = {'http':'socks5://127.0.0.1:9050', 'https':'socks5://127.0.0.1:9050'}
	print requests.get('http://icanhazip.com',proxies=proxies).text.strip()


for _ in range(10):
	renew_connection()
	request()
	time.sleep(4)
