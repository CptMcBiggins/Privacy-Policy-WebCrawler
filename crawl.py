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
	
	total_risk_score = []

	def coppa():
		results_list = []
		
		coppap = soup.find_all('p')
		for i in coppap:
			results = str(i.text.strip())
			if 'child' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)

		coppali = soup.find_all('li')
		for i in coppali:
			results = str(i.text.strip())
			if 'child' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)

		coppatd = soup.find_all('td')
		for i in coppatd:
			results = str(i.text.strip())
			if 'child' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)

		coppasp = soup.find_all('span')
		for i in coppasp:
			results = str(i.text.strip())
			if 'child' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)

		clean_list = []
		for i in results_list:
			if i not in clean_list:
				clean_list.append(i)
		
		str_rs = []
		str_r = []
		
		low = 0
		medium = 30
		high = 50
		zero = 100

		if len(clean_list) == 0:
			str_rs.append(zero)
			str_r.append("Unacceptable Risk")
			total_risk_score.append(zero)
		elif len(clean_list) <= 15:
			str_rs.append(low)
			str_r.append("Low Risk")
			total_risk_score.append(low)
		elif len(clean_list) <= 30:
			str_rs.append(medium)
			str_r.append("Medium Risk")
			total_risk_score.append(medium)
		elif len(clean_list) > 30:
			str_rs.append(high)
			str_r.append("High Risk")
			total_risk_score.append(high)

		ppstr = ' '.join([str(i) for i in str_r])
		pprisk = [str(i) for i in str_rs]
		pprs = int("".join(pprisk))

		listToStr = ' '.join([str(i) for i in clean_list])
		active_cell = sheet.findall(URL)
		for i in active_cell:
			url_row = i.row
			row_str = str(url_row)	

		active_row = 'G' + row_str
		pp_risk_str = 'T' + row_str
		pp_risk_score = 'U' + row_str
		sheet.update(active_row, listToStr)
		sheet.update(pp_risk_str, ppstr)
		sheet.update(pp_risk_score, pprs)
	coppa()

	def p1():
		results_list = []

		p1p = soup.find_all('p')
		for i in p1p:
			results = str(i.text.strip())
			if 'collect' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)	

		p1li = soup.find_all('li')
		for i in p1li:
			results = str(i.text.strip())
			if 'collect' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)	

		p1td = soup.find_all('td')
		for i in p1td:
			results = str(i.text.strip())
			if 'collect' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)

		p1sp = soup.find_all('span')
		for i in p1sp:
			results = str(i.text.strip())
			if 'collect' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)

		clean_list = []
		for i in results_list:
			if i not in clean_list:
				clean_list.append(i)

		str_rs = []
		str_r = []
		
		low = 0
		medium = 30
		high = 50
		zero = 100

		if len(clean_list) == 0:
			str_rs.append(zero)
			str_r.append("Unacceptable Risk")
			total_risk_score.append(zero)
		elif len(clean_list) <= 15:
			str_rs.append(low)
			str_r.append("Low Risk")
			total_risk_score.append(low)
		elif len(clean_list) <= 30:
			str_rs.append(medium)
			str_r.append("Medium Risk")
			total_risk_score.append(medium)
		elif len(clean_list) > 30:
			str_rs.append(high)
			str_r.append("High Risk")
			total_risk_score.append(high)
		
		ppstr = ' '.join([str(i) for i in str_r])
		pprisk = [str(i) for i in str_rs]
		pprs = int("".join(pprisk))

		listToStr = ' '.join([str(i) for i in clean_list])
		active_cell = sheet.findall(URL)
		for i in active_cell:
			url_row = i.row
			row_str = str(url_row)	
		
		active_row = 'H' + row_str
		pp_risk_str = 'V' + row_str
		pp_risk_score = 'W' + row_str
		sheet.update(active_row, listToStr)
		sheet.update(pp_risk_str, ppstr)
		sheet.update(pp_risk_score, pprs)
	p1()
	
	def p2():
		results_list = []
		
		p2p = soup.find_all('p')
		for i in p2p:
			results = str(i.text.strip())
			if ' use ' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)

		p2li = soup.find_all('li')
		for i in p2li:
			results = str(i.text.strip())
			if ' use ' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)	

		p2td = soup.find_all('td')
		for i in p2td:
			results = str(i.text.strip())
			if ' use ' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)

		p2sp = soup.find_all('span')
		for i in p2sp:
			results = str(i.text.strip())
			if ' use ' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)

		clean_list = []
		for i in results_list:
			if i not in clean_list:
				clean_list.append(i)


		str_rs = []
		str_r = []
		
		low = 0
		medium = 30
		high = 50
		zero = 100

		if len(clean_list) == 0:
			str_rs.append(zero)
			str_r.append("Unacceptable Risk")
			total_risk_score.append(zero)
		elif len(clean_list) <= 15:
			str_rs.append(low)
			str_r.append("Low Risk")
			total_risk_score.append(low)
		elif len(clean_list) <= 30:
			str_rs.append(medium)
			str_r.append("Medium Risk")
			total_risk_score.append(medium)
		elif len(clean_list) > 30:
			str_rs.append(high)
			str_r.append("High Risk")
			total_risk_score.append(high)
		
		ppstr = ' '.join([str(i) for i in str_r])
		pprisk = [str(i) for i in str_rs]
		pprs = int("".join(pprisk))

		listToStr = ' '.join([str(i) for i in clean_list])
		active_cell = sheet.findall(URL)
		for i in active_cell:
			url_row = i.row
			row_str = str(url_row)	

		active_row = 'I' + row_str
		pp_risk_str = 'X' + row_str
		pp_risk_score = 'Y' + row_str
		sheet.update(active_row, listToStr)
		sheet.update(pp_risk_str, ppstr)
		sheet.update(pp_risk_score, pprs)
	p2()

	def p3():
		results_list = []
		
		p3p = soup.find_all('p')
		for i in p3p:
			results = str(i.text.strip())
			if 'store' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)	

		p3li = soup.find_all('li')
		for i in p3li:
			results = str(i.text.strip())
			if 'store' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)	

		p3td = soup.find_all('td')
		for i in p3td:
			results = str(i.text.strip())
			if 'store' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)

		p3sp = soup.find_all('span')
		for i in p3sp:
			results = str(i.text.strip())
			if 'store' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)

		clean_list = []
		for i in results_list:
			if i not in clean_list:
				clean_list.append(i)

		str_rs = []
		str_r = []
		
		low = 0
		medium = 30
		high = 50
		zero = 100

		if len(clean_list) == 0:
			str_rs.append(zero)
			str_r.append("Unacceptable Risk")
			total_risk_score.append(zero)
		elif len(clean_list) <= 15:
			str_rs.append(low)
			str_r.append("Low Risk")
			total_risk_score.append(low)
		elif len(clean_list) <= 30:
			str_rs.append(medium)
			str_r.append("Medium Risk")
			total_risk_score.append(medium)
		elif len(clean_list) > 30:
			str_rs.append(high)
			str_r.append("High Risk")
			total_risk_score.append(high)
		
		ppstr = ' '.join([str(i) for i in str_r])
		pprisk = [str(i) for i in str_rs]
		pprs = int("".join(pprisk))

		listToStr = ' '.join([str(i) for i in clean_list])
		active_cell = sheet.findall(URL)
		for i in active_cell:
			url_row = i.row
			row_str = str(url_row)	

		active_row = 'J' + row_str
		pp_risk_str = 'Z' + row_str
		pp_risk_score = 'AA' + row_str
		sheet.update(active_row, listToStr)
		sheet.update(pp_risk_str, ppstr)
		sheet.update(pp_risk_score, pprs)
	p3()

	def p4():
		results_list = []
		
		p4p = soup.find_all('p')
		for i in p4p:
			results = str(i.text.strip())
			if 'protect' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)

		p4li = soup.find_all('li')
		for i in p4li:
			results = str(i.text.strip())
			if 'protect' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)	

		p4td = soup.find_all('td')
		for i in p4td:
			results = str(i.text.strip())
			if 'protect' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)

		p4sp = soup.find_all('span')
		for i in p4sp:
			results = str(i.text.strip())
			if 'protect' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)

		clean_list = []
		for i in results_list:
			if i not in clean_list:
				clean_list.append(i)

		str_rs = []
		str_r = []
		
		low = 0
		medium = 30
		high = 50
		zero = 100

		if len(clean_list) == 0:
			str_rs.append(zero)
			str_r.append("Unacceptable Risk")
			total_risk_score.append(zero)
		elif len(clean_list) <= 15:
			str_rs.append(low)
			str_r.append("Low Risk")
			total_risk_score.append(low)
		elif len(clean_list) <= 30:
			str_rs.append(medium)
			str_r.append("Medium Risk")
			total_risk_score.append(medium)
		elif len(clean_list) > 30:
			str_rs.append(high)
			str_r.append("High Risk")
			total_risk_score.append(high)
		
		ppstr = ' '.join([str(i) for i in str_r])
		pprisk = [str(i) for i in str_rs]
		pprs = int("".join(pprisk))

		listToStr = ' '.join([str(i) for i in clean_list])
		active_cell = sheet.findall(URL)
		for i in active_cell:
			url_row = i.row
			row_str = str(url_row)	

		active_row = 'K' + row_str
		pp_risk_str = 'AB' + row_str
		pp_risk_score = 'AC' + row_str
		sheet.update(active_row, listToStr)
		sheet.update(pp_risk_str, ppstr)
		sheet.update(pp_risk_score, pprs)
	p4()

	def p5():
		results_list = []
		p5p = soup.find_all('p')
		for i in p5p:
			results = str(i.text.strip())
			if 'share' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)
			if 'third part' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)

		p5li = soup.find_all('li')
		for i in p5li:
			results = str(i.text.strip())
			if 'share' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)
			if 'third part' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)

		p5td = soup.find_all('td')
		for i in p5td:
			results = str(i.text.strip())
			if 'share' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)
			if 'third part' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)

		p5sp = soup.find_all('span')
		for i in p5sp:
			results = str(i.text.strip())
			if 'share' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)
			if 'third part' in results:
				clean = str(results.replace("\n",","))
				super_clean = re.sub("[  ] ", "", clean)
				results_list.append(super_clean)
		
		clean_list = []
		for i in results_list:
			if i not in clean_list:
				clean_list.append(i)

		str_rs = []
		str_r = []
		
		low = 0
		medium = 30
		high = 50
		zero = 100

		if len(clean_list) == 0:
			str_rs.append(zero)
			str_r.append("Unacceptable Risk")
			total_risk_score.append(zero)
		elif len(clean_list) <= 15:
			str_rs.append(low)
			str_r.append("Low Risk")
			total_risk_score.append(low)
		elif len(clean_list) <= 30:
			str_rs.append(medium)
			str_r.append("Medium Risk")
			total_risk_score.append(medium)
		elif len(clean_list) > 30:
			str_rs.append(high)
			str_r.append("High Risk")
			total_risk_score.append(high)
		
		ppstr = ' '.join([str(i) for i in str_r])
		pprisk = [str(i) for i in str_rs]
		pprs = int("".join(pprisk))

		listToStr = ' --- '.join([str(i) for i in clean_list])
		active_cell = sheet.findall(URL)
		for i in active_cell:
			url_row = i.row
			row_str = str(url_row)	

		active_row = 'L' + row_str
		pp_risk_str = 'AD' + row_str
		pp_risk_score = 'AE' + row_str
		sheet.update(active_row, listToStr)
		sheet.update(pp_risk_str, ppstr)
		sheet.update(pp_risk_score, pprs)
	p5()
	
	def contact():
		contact_list = []
		link = soup.find_all('a')
		for i in link:
			links = i.get('href')
			email_links = str(links)
			if 'mailto:' in email_links:
				contact_list.append(email_links)
	
		email_list = []
		for i in contact_list:
			if i not in email_list:
				email_list.append(i)

		str_rs = []
		str_r = []
		
		low = 0
		medium = 30
		high = 50
		zero = 100

		if len(email_list) == 0:
			str_rs.append(zero)
			str_r.append("Unacceptable Risk")
			total_risk_score.append(zero)
		elif len(email_list) <= 15:
			str_rs.append(low)
			str_r.append("Low Risk")
			total_risk_score.append(low)
		elif len(email_list) <= 30:
			str_rs.append(medium)
			str_r.append("Medium Risk")
			total_risk_score.append(medium)
		elif len(email_list) > 30:
			str_rs.append(high)
			str_r.append("High Risk")
			total_risk_score.append(high)
		
		ppstr = ' '.join([str(i) for i in str_r])
		pprisk = [str(i) for i in str_rs]
		pprs = int("".join(pprisk))
	
		listToStr = ', '.join([str(i) for i in email_list])
		clean = str(listToStr.replace("mailto:", ""))
		active_cell = sheet.findall(URL)
		for i in active_cell:
			url_row = i.row
			row_str = str(url_row)	
	
		active_row = 'M' + row_str
		pp_risk_str = 'AF' + row_str
		pp_risk_score = 'AG' + row_str
		sheet.update(active_row, clean)
		sheet.update(pp_risk_str, ppstr)
		sheet.update(pp_risk_score, pprs)
	contact()

	def rs():
		active_cell = sheet.findall(URL)
		for i in active_cell:
			url_row = i.row
			row_str = str(url_row)	

		risk_score = sum(total_risk_score)/7
		total = 100
		total_dec = round(risk_score/total, 2)
		pprp = "{0:.0%}".format(total_dec)

		active_row = 'AH' + row_str
		sheet.update(active_row, total_dec)
		active_row = 'AI' + row_str
		sheet.update(active_row, pprp)
	rs()
main()
