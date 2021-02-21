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

# To get and print <p>&<li> tags
def coppa():
	childp = soup.find_all('p', string=re.compile("child"))
	for items in childp:
		print(items.text.strip())

	coppali = soup.find_all('li')
	for item in coppali:
		items = str(item.text.strip())
		if 'child' in items:
			print(items)

def p1():
	collectp = soup.find_all('p', string=re.compile("collect"))
	for item in collectp:
		print(item.text.strip())

	p1li = soup.find_all('li')
	for item in p1li:
		items = str(item.text.strip())
		if 'collect' in items:
			print(items)

def p2():
	usep = soup.find_all('p', string = re.compile("use "))
	for item in usep:
		print(item.text.strip())

	p2li = soup.find_all('li')
	for item in p2li:
		items = str(item.text.strip())
		if 'use ' in items:
			print(items)

def p3():
	storep = soup.find_all('p', string = re.compile("store"))
	for item in storep:
		print(item.text.strip())

	p3li = soup.find_all('li')
	for item in p3li:
		items = str(item.text.strip())
		if 'store' in items:
			print(items)

def p4():
	protectp = soup.find_all('p', string=re.compile("protect"))
	for item in protectp:
		print(item.text.strip())

	p4li = soup.find_all('li')
	for item in p4li:
		items = str(item.text.strip())
		if 'protect' in items:
			print(items)

def p5():
	sharep = soup.find_all('p', string=re.compile("share"))
	thirdp = soup.find_all('p', string=re.compile("third part"))
	for item in sharep:
		print(item.text.strip())
	for item in thirdp:
		print(item.text.strip())

	p5li = soup.find_all('li')
	for item in p5li:
		items = str(item.text.strip())
		if 'third part' in items:
			print(items)
		if 'share' in items:
			print(items)

def main():
	return(contact(),coppa(),p1(),p2(),p3(),p4(),p5())
main()
