#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import re

URL = 'https://anchor.fm/privacy'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# To get and print contact links from privacy policy
def contact():

	for link in soup.find_all('a'):
	    links = link.get('href')
	    if 'mailto:' in links:
	    	return(links)

# To get and print <p></p> tags with the word children in them
def children():
	childrenz = soup.find_all('p', string=re.compile("children"))
	for item in childrenz:
		return(item.text.strip())

# To get and print <p></p> tags with the word collect in them
def collect():
	collectz = soup.find_all('p', string=re.compile("collect"))
	for item in collectz:
		return(item.text.strip())

# To get and print <p></p> tags with the word share in them
def share():
	sharez = soup.find_all('p', string=re.compile("share"))
	for item in sharez:
		return item.text.strip()

# To get and print <p></p> tags with the words third party in them
def party():
	partyz = soup.find_all('p', string=re.compile("third party"))
	for item in partyz:
		return item.text.strip()

# To get and print <p></p> tags with the words third parties in them
def parties():
	partyzz = soup.find_all('p', string=re.compile("third parties"))
	for item in partyzz:
		return item.text.strip()

# To get and print <p></p> tags with the word protect in them
def protect():
	protectz = soup.find_all('p', string=re.compile("protect"))
	for item in protectz:
		return(item.text.strip())

def main():
	print(share())
main()