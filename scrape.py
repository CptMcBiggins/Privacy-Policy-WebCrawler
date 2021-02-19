#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

URL = 'https://bitly.com/pages/privacy'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('p')
print(results)
#presultz = results.p.string

#for hit in results:
	#presults = hit.find('p')
	#print(f"{presults}")
#policy_contact = results.find_all('a')['href']

#for hit in results:
#	link = hit.find('a')['href']

#print(f"{link}")

#for hit in policy:
    #link = hit.find('a')['href']
    #print(hit.text.strip())
    #print(f"Contact: {link}\n")

#policy_contactz = results.h2.string
#policy_contactzz = results.p.string

#print(policy_contactz)