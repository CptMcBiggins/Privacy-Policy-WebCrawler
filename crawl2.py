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

utlist = []

def u1():
	a, l = "Collaboration (student-student, student-teacher, teacher-teacher)", 28
	b, m = "Communication (audio/video, presentation tools, social media-like)", 18
	c, n = "Creativity (art, books)", 9
	d, o = "Critical Thinking (organizers, mindmaps)", 9
	e, p = "Diverse Learners and Accommodations", 28
	f, q = "Effective Integration (flipped classrooms, interactive lessons, etc.)", 40
	g, r = "Feedback and Assessment", 12
	h, s = "Gamification (make it fun - introduction, review, center/station)", 25
	zz, t = "Productivity /Efficiency Tools (make the job easier/more efficient)", 48
	j, u = "Remote/Distance Learning", 63
	k, v = "Student Engagement", 12
	list1 = [a,b,c,d,e,f,g,h,zz,j,k]
	list2 = [l,m,n,o,p,q,r,s,t,u,v]

	active_cell = sheet.findall(URL)
	for itemz in active_cell:
		url_row = itemz.row
		row_str = str(url_row)
	
	choice_value_list = []
	active_row = 'C' + row_str
	current_row = sheet.get(active_row)
	current_row_str = str(current_row)
	for item in list1:
		if item in current_row_str:
			list_index = (list1.index(item))
			index_value = list2[list_index]
			choice_value_list.append(index_value)
	
	choices = len(choice_value_list)
	weight = round(.91*choices, 2)
	if choices > 1:
		math = sum(choice_value_list)*weight/choices
	else:
		math = choice_value_list[0]

	utlist.append(math)
	actives_row = 'N' + row_str
	sheet.update(actives_row, math)
u1()

def u2():
	a, e = "Teachers", 49
	b, f = "Students", 42
	c, g = "Non-Teaching Staff", 63
	d, h = "Parents", 20
	list1 = [a,b,c,d]
	list2 = [e,f,g,h]
	
	active_cell = sheet.findall(URL)
	for itemz in active_cell:
		url_row = itemz.row
		row_str = str(url_row)

	choice_value_list = []
	active_row = 'D' + row_str
	current_row = sheet.get(active_row)
	current_row_str = str(current_row)
	for item in list1:
		if item in current_row_str:
			list_index = (list1.index(item))
			index_value = list2[list_index]
			choice_value_list.append(index_value)

	choices = len(choice_value_list)
	weight = round(1.22*choices, 2)
	if choices > 1:
		math = sum(choice_value_list)*weight/choices
	else:
		math = choice_value_list[0]

	utlist.append(math)
	actives_row = 'O' + row_str
	sheet.update(actives_row, math)
u2()

def u3():
	a, d = "No account needed/access with class or invite code", 3
	b, e = "SSO Login with Google or Microsoft (i.e., school login)", 60
	c, f = "Separate account needed", 42
	list1 = [a,b,c]
	list2 = [d,e,f]
	
	active_cell = sheet.findall(URL)
	for itemz in active_cell:
		url_row = itemz.row
		row_str = str(url_row)

	choice_value_list = []
	active_row = 'E' + row_str
	current_row = sheet.get(active_row)
	current_row_str = str(current_row)
	for item in list1:
		if item in current_row_str:
			list_index = (list1.index(item))
			index_value = list2[list_index]
			choice_value_list.append(index_value)

	choices = len(choice_value_list)
	weight = round(1.24*choices, 2)
	if choices > 1:
		math = sum(choice_value_list)*weight/choices
	else:
		math = choice_value_list[0]

	utlist.append(math)
	actives_row = 'P' + row_str
	sheet.update(actives_row, math)
u3()

def u4():
	a, e = "Primary (PK-2)", 35
	b, f = "Elementary (3-5)", 49
	c, g = "Middle School/Junior High (6-8)", 56
	d, h = "High School (9-12)", 72
	list1 = [a,b,c,d]
	list2 = [e,f,g,h]

	active_cell = sheet.findall(URL)
	for itemz in active_cell:
		url_row = itemz.row
		row_str = str(url_row)

	choice_value_list = []
	active_row = 'F' + row_str
	current_row = sheet.get(active_row)
	current_row_str = str(current_row)
	for item in list1:
		if item in current_row_str:
			list_index = (list1.index(item))
			index_value = list2[list_index]
			choice_value_list.append(index_value)

	choices = len(choice_value_list)
	weight = round(1.13*choices, 2)
	if choices > 1:
		math = sum(choice_value_list)*weight/choices
	else:
		math = choice_value_list[0]

	utlist.append(math)
	actives_row = 'Q' + row_str
	sheet.update(actives_row, math)
u4()

def ut():
	active_cell = sheet.findall(URL)
	for itemz in active_cell:
		url_row = itemz.row
		row_str = str(url_row)

	utaverage = sum(utlist)/4
	utmaxav = 211.94
	utdec = round(utaverage/utmaxav, 2)
	utper = "{0:.0%}".format(utdec)

	actives_row = 'R' + row_str
	sheet.update(actives_row, utaverage)
	actives_row = 'S' + row_str
	sheet.update(actives_row, utper)
ut()




