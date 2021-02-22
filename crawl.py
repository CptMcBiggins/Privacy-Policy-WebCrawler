#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import re
import argparse
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#parser = argparse.ArgumentParser(description='Privacy Policy Automation')
#parser.add_argument('-u', help='Privacy Policy URL', required=True)
#args = parser.parse_args()

#URL = args.u
URL = 'https://anchor.fm/privacy'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Test Sheet").sheet1

# To get and print contact links from privacy policy
def contact():

	for link in soup.find_all('a'):
	    links = link.get('href')
	    if 'mailto:' in links:
	    	g1 = str(links)

	active_cell = sheet.findall(URL)
	for itemz in active_cell:
		url_row = itemz.row
		row_str = str(url_row)

	active_row = 'I' + row_str
	sheet.update(active_row, g1)

# To get and print <p>&<li>&<td> tags
def coppa():
	childp = soup.find_all('p', string = re.compile("child"))
	for item in childp:
		if item is not None:
			g1 = (item.text.strip())
			if item is None:
				g1 = "None"
			return g1

	coppali = soup.find_all('li')
	for item in coppali:
		items = str(item.text.strip())
		if 'child' in items:
			g2 = str(items)
			if 'child' not in items: 
				g2 = "None"
			return g1
	
	coppatd = soup.find_all('td')
	for item in coppatd:
		items = str(item.text.strip())
		if 'child' in items:
			g3 = str(items)
			if 'child' not in items:
				g3 = "None"
			return g3

	g4 = g1 + g2 + g3
	active_cell = sheet.findall(URL)
	for itemz in active_cell:
		url_row = itemz.row
		row_str = str(url_row)

	active_row = 'C' + row_str
	sheet.update(active_row, g4)

def p1():
	collectp = soup.find_all('p', string = re.compile("collect"))
	for item in collectp:
		if item is not None:
			g1 = (item.text.strip())
			if item is None:
				g1 = "None"
			return g1

	p1li = soup.find_all('li')
	for item in p1li:
		items = str(item.text.strip())
		if 'collect' in items:
			g2 = str(items)
			if 'collect' not in items:
				g2 = "None"
			return g2	

	p1td = soup.find_all('td')
	for item in p1td:
		items = str(item.text.strip())
		if 'collect' in items:
			g3 = str(items)
			if 'collect' not in items:
				g3 = "None"
			return g3
	
	g4 = g1 + g2 + g3
	active_cell = sheet.findall(URL)
	for itemz in active_cell:
		url_row = itemz.row
		row_str = str(url_row)

	active_row = 'D' + row_str
	sheet.update(active_row, g4)

def p2():
	usep = soup.find_all('p', string = re.compile("use "))
	for item in usep:
		if item is not None:
			g1 = (item.text.strip())
			if item is None:
				g1 = "None"
			return g1

	p2li = soup.find_all('li')
	for item in p2li:
		items = str(item.text.strip())
		if 'use ' in items:
			g2 = str(items)
			if 'use ' not in items:
				g2 = "None"
			return g2

	p2td = soup.find_all('td')
	for item in p2td:
		items = str(item.text.strip())
		if 'use ' in items:
			g3 = str(items)
			if 'use ' not in items:
				g3 ="None"
			return g3

	g4 = g1 + g2 + g3
	active_cell = sheet.findall(URL)
	for itemz in active_cell:
		url_row = itemz.row
		row_str = str(url_row)

	active_row = 'E' + row_str
	sheet.update(active_row, g4)

def p3():
	storep = soup.find_all('p', string = re.compile("store"))
	for item in storep:
		if item is not None:
			g1 = (item.text.strip())
			if item is None:
				g1 = "None"
			return g1

	p3li = soup.find_all('li')
	for item in p3li:
		items = str(item.text.strip())
		if 'store' in items:
			g2 = str(items)
			if 'store' not in items:
				g2 = "None"
			return g2

	p3td = soup.find_all('td')
	for item in p3td:
		items = str(item.text.strip())
		if 'store' in items:
			g3 = str(items)
			if 'store' not in items:
				g3 = "None"
			return g3

	g4 = g1 + g2 + g3
	active_cell = sheet.findall(URL)
	for itemz in active_cell:
		url_row = itemz.row
		row_str = str(url_row)

	active_row = 'F' + row_str
	sheet.update(active_row, g4)

def p4():
	protectp = soup.find_all('p', string = re.compile("protect"))
	for item in protectp:
		if item is not None:
			g1 = (item.text.strip())
			if item is None:
				g1 = "None"
			return g1

	p4li = soup.find_all('li')
	for item in p4li:
		items = str(item.text.strip())
		if 'protect' in items:
			g2 = str(items)
			if 'protect' not in items:
				g2 = "None"
			return g2
	
	p4td = soup.find_all('td')
	for item in p4td:
		items = str(item.text.strip())
		if 'protect' in items:
			g3 = (items)
			if 'protect' not in items:
				g3 = "None"
			return g3

	g4 = g1 + g2 + g3
	active_cell = sheet.findall(URL)
	for itemz in active_cell:
		url_row = itemz.row
		row_str = str(url_row)

	active_row = 'G' + row_str
	sheet.update(active_row, g4)

def p5():
	sharep = soup.find_all('p', string = re.compile("share"))
	thirdp = soup.find_all('p', string = re.compile("third part"))
	for item in sharep:
		if item is not None:
			g1 = (item.text.strip())
			if item is None:
				g1 = "None"
				return g1
	for item in thirdp:
		if item is not None:
			g2 = (item.text.strip())
			if item is None:
				g2 = "None"
				return g2

	p5li = soup.find_all('li')
	for item in p5li:
		items = str(item.text.strip())
		if 'third part ' in items:
			g3 = str(items)
			if 'third part ' not in items:
				g3 = "None"
			return g3
		if 'share' in items:
			g4 = (items)
			if 'share' not in items:
				g4 = "None"
			return g4

	p5td = soup.find_all('td')
	for item in p5td:
		items = str(item.text.strip())
		if 'third part ' not in items:
			g5 = str(items)
			if 'third part ' not in items:
				g5 = "None"
			return g5
		if 'share' in items:
			g6 = str(items)
			if 'share' not in items:
				g6 = "None"
			return g6

	g7 = g1 + g2 + g3 + g4 + g5 + g6
	active_cell = sheet.findall(URL)
	for itemz in active_cell:
		url_row = itemz.row
		row_str = str(url_row)

	active_row = 'H' + row_str
	sheet.update(active_row, g7)

def main():
	return(contact(),coppa(),p1(),p2(),p3(),p4(),p5())
main()
