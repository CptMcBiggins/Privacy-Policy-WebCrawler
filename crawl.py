#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import re
import argparse

#parser = argparse.ArgumentParser(description='Privacy Policy Automation')
#parser.add_argument('-u', help='Privacy Policy URL', required=True)
#args = parser.parse_args()

#URL = args.u
URL = ''
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# To get and print contact links from privacy policy
def contact():

	for link in soup.find_all('a'):
	    links = link.get('href')
	    if 'mailto:' in links:
	    	print(links)

# To get and print <p> tags with child or child in them
def coppa():
	child = soup.find_all('p', string=re.compile("child"))
	for items in child:
		print(items.text.strip())

# To get and print <p></p> tags with the word collect in them
def p1():
	collect = soup.find_all('p', string=re.compile("collect"))
	for item in collect:
		print(item.text.strip())

# To get and print <p></p> tags with the word protect in them
def p4():
	protect = soup.find_all('p', string=re.compile("protect"))
	for item in protect:
		print(item.text.strip())

# To get and print <p></p> tags with the word share in them
def p5():
	share = soup.find_all('p', string=re.compile("share"))
	party = soup.find_all('p', string=re.compile("third part"))
	for item in share:
		print(item.text.strip())
	for item in party:
		print(item.text.strip())

# To get and print <li></li> tags	
	third = soup.find_all('li')
	for item in third:
		items = str(item.text.strip())
		if 'third part' in items:
			print(items)


def main():
	return(contact(),coppa(),p1(),p4(),p5())
main()