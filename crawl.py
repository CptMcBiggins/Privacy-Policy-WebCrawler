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
	    	print(links)

# To get and print <p> tags with child or children in them
def children():
	childrenz = soup.find_all('p', string=re.compile("children"))
	childz = soup.find_all('p', string=re.compile("child"))
	for item in childrenz:
		print(item.text.strip())
	for items in childz:
		print(items.text.strip())

# To get and print <p></p> tags with the word collect in them
def collect():
	collectz = soup.find_all('p', string=re.compile("collect"))
	for item in collectz:
		print(item.text.strip())

# To get and print <p></p> tags with the word share in them
def share():
	sharez = soup.find_all('p', string=re.compile("share"))
	for item in sharez:
		print(item.text.strip())

# To get and print <p> tags with the words third party or parties in them
def party():
	partyz = soup.find_all('p', string=re.compile("third party"))
	partyzz = soup.find_all('p', string=re.compile("third parties"))
	for item in partyz:
		print(item.text.strip())
	for items in partyzz:
		print(items.text.strip())

# To get and print <p></p> tags with the word protect in them
def protect():
	protectz = soup.find_all('p', string=re.compile("protect"))
	for item in protectz:
		print(item.text.strip())

def main():
	return(contact(),children(),collect(),share(),party(),protect())
main()