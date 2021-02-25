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

def main():
	def coppa():
		results_list = []
		childp = soup.find_all('p', string = re.compile("child"))
		for i in childp:
			if i is not None:
				results = (i.text.strip())
				results_list.append(results)

		coppali = soup.find_all('li')
		for i in coppali:
			results = str(i.text.strip())
			if 'child' in results:
				results_list.append(results)	

		coppatd = soup.find_all('td')
		for i in coppatd:
			results = str(i.text.strip())
			if 'child' in results:
				results_list.append(results)	

		listToStr = ' '.join([str(i) for i in results_list])
		active_cell = sheet.findall(URL)
		for i in active_cell:
			url_row = i.row
			row_str = str(url_row)	

		active_row = 'G' + row_str
		sheet.update(active_row, listToStr)
	coppa()

	def p1():
		results_list = []
		collectp = soup.find_all('p', string = re.compile("collect"))
		for i in collectp:
			if i is not None:
				results = (i.text.strip())
				results_list.append(results)	

		p1li = soup.find_all('li')
		for i in p1li:
			results = str(i.text.strip())
			if 'collect' in results:
				results_list.append(results)	

		p1td = soup.find_all('td')
		for i in p1td:
			results = str(i.text.strip())
			if 'collect' in results:
				results_list.append(results)	

		listToStr = ' '.join([str(i) for i in results_list])
		active_cell = sheet.findall(URL)
		for i in active_cell:
			url_row = i.row
			row_str = str(url_row)	

		active_row = 'H' + row_str
		sheet.update(active_row, listToStr)
	p1()
	
	def p2():
		results_list = []
		usep = soup.find_all('p', string = re.compile("use "))
		for i in usep:
			if i is not None:
				results = (i.text.strip())
				results_list.append(results)	

		p2li = soup.find_all('li')
		for i in p2li:
			results = str(i.text.strip())
			if 'use ' in results:
				results_list.append(results)	

		p2td = soup.find_all('td')
		for i in p2td:
			results = str(i.text.strip())
			if 'use ' in results:
				results_list.append(results)	

		listToStr = ' '.join([str(i) for i in results_list])
		active_cell = sheet.findall(URL)
		for i in active_cell:
			url_row = i.row
			row_str = str(url_row)	

		active_row = 'I' + row_str
		sheet.update(active_row, listToStr)
	p2()

	def p3():
		results_list = []
		storep = soup.find_all('p', string = re.compile("store"))
		for i in storep:
			if i is not None:
				results = (i.text.strip())
				results_list.append(results)	

		p3li = soup.find_all('li')
		for i in p3li:
			results = str(i.text.strip())
			if 'store' in results:
				results_list.append(results)	

		p3td = soup.find_all('td')
		for i in p3td:
			results = str(i.text.strip())
			if 'store' in results:
				results_list.append(results)	

		listToStr = ' '.join([str(i) for i in results_list])
		active_cell = sheet.findall(URL)
		for i in active_cell:
			url_row = i.row
			row_str = str(url_row)	

		active_row = 'J' + row_str
		sheet.update(active_row, listToStr)
	p3()

	def p4():
		results_list = []
		protectp = soup.find_all('p', string = re.compile("protect"))
		for i in protectp:
			if i is not None:
				results = (i.text.strip())
				results_list.append(results)	

		p4li = soup.find_all('li')
		for i in p4li:
			results = str(i.text.strip())
			if 'protect' in results:
				results_list.append(results)	

		p4td = soup.find_all('td')
		for i in p4td:
			results = str(i.text.strip())
			if 'protect' in results:
				results_list.append(results)	

		listToStr = ' '.join([str(i) for i in results_list])
		active_cell = sheet.findall(URL)
		for i in active_cell:
			url_row = i.row
			row_str = str(url_row)	

		active_row = 'K' + row_str
		sheet.update(active_row, listToStr)
	p4()

	def p5():
		results_list = []
		sharep = soup.find_all('p', string = re.compile("share"))
		for i in sharep:
			if i is not None:
				results = (i.text.strip())
				results_list.append(results)

		thirdp = soup.find_all('p', string = re.compile("third part"))
		for i in thirdp:
			if i is not None:
				results = (i.text.strip())
				results_list.append(results)

		p5li = soup.find_all('li')
		for i in p5li:
			results = str(i.text.strip())
			if 'share' in results:
				results_list.append(results)
			if 'third part' in results:
				results_list.append(results)

		p5td = soup.find_all('td')
		for i in p5td:
			results = str(i.text.strip())
			if 'share' in results:
				results_list.append(results)
			if 'third part' in results:
				results_list.append(results)		

		listToStr = ' '.join([str(i) for i in results_list])
		active_cell = sheet.findall(URL)
		for i in active_cell:
			url_row = i.row
			row_str = str(url_row)	

		active_row = 'L' + row_str
		sheet.update(active_row, listToStr)
	p5()
	def contact():
		results_list = []
		for i in soup.find_all('a'):
			links = i.get('href')
			if 'mailto:' in links:
				results_list.append(links)
		
		listToStr = ' '.join([str(i) for i in results_list])
		active_cell = sheet.findall(URL)
		for i in active_cell:
			url_row = i.row
			row_str = str(url_row)
			
		active_row = 'M' + row_str
		sheet.update(active_row, listToStr)
	contact()
main()
