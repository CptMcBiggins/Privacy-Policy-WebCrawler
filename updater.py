#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import re
import argparse
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date

parser = argparse.ArgumentParser(description='Privacy Policy Automation')
parser.add_argument('-u', help='Privacy Policy URL', required=True)
args = parser.parse_args()

URL = args.u
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1CWWDS-oerHMZA0JkJltDXB7ZfQvoYv785BirpO_xC6E/edit#gid=2066074964').sheet1

ppvalues = []
final_list = []

def main():
        active_cell = sheet.findall(URL)
        for i in active_cell:
                url_row = i.row
                row_str = str(url_row)

        active_row = 'AD' + row_str
        current_row = sheet.get(active_row)
        current_row_str = str(current_row)
        clean = current_row_str.replace("[","")
        clean1 = clean.replace("]","")
        clean2 = clean1.replace("'","")
        current_row_int = int(clean2)
        ppvalues.append(current_row_int)

        active_row = 'AE' + row_str
        current_row = sheet.get(active_row)
        current_row_str = str(current_row)
        clean = current_row_str.replace("[","")
        clean1 = clean.replace("]","")
        clean2 = clean1.replace("'","")
        current_row_int = int(clean2)
        ppvalues.append(current_row_int)

        active_row = 'AF' + row_str
        current_row = sheet.get(active_row)
        current_row_str = str(current_row)
        clean = current_row_str.replace("[","")
        clean1 = clean.replace("]","")
        clean2 = clean1.replace("'","")
        current_row_int = int(clean2)
        ppvalues.append(current_row_int)

        active_row = 'AG' + row_str
        current_row = sheet.get(active_row)
        current_row_str = str(current_row)
        clean = current_row_str.replace("[","")
        clean1 = clean.replace("]","")
        clean2 = clean1.replace("'","")
        current_row_int = int(clean2)
        ppvalues.append(current_row_int)

        active_row = 'AH' + row_str
        current_row = sheet.get(active_row)
        current_row_str = str(current_row)
        clean = current_row_str.replace("[","")
        clean1 = clean.replace("]","")
        clean2 = clean1.replace("'","")
        current_row_int = int(clean2)
        ppvalues.append(current_row_int)

        active_row = 'AI' + row_str
        current_row = sheet.get(active_row)
        current_row_str = str(current_row)
        clean = current_row_str.replace("[","")
        clean1 = clean.replace("]","")
        clean2 = clean1.replace("'","")
        current_row_int = int(clean2)
        ppvalues.append(current_row_int)

        active_row = 'AJ' + row_str
        current_row = sheet.get(active_row)
        current_row_str = str(current_row)
        clean = current_row_str.replace("[","")
        clean1 = clean.replace("]","")
        clean2 = clean1.replace("'","")
        current_row_int = int(clean2)
        ppvalues.append(current_row_int)

        active_row = 'N' + row_str
        current_row = sheet.get(active_row)
        current_row_str = str(current_row)
        clean = current_row_str.replace("[","")
        clean1 = clean.replace("]","")
        clean2 = clean1.replace("'","")
        clean3 = clean2.replace("%","")
        current_row_int = int(clean3)
        final_list.append(current_row_int)

        risk_score = sum(ppvalues)/7
        total = 100
        total_dec = round(risk_score/total, 2)
        total_number = total_dec*100
        final_list.append(total_number)
        pprp = "{0:.0%}".format(total_dec)

        today = date.today()
        date_today = today.strftime("%m/%d/%Y")
        m = int(date_today [:2])
        d = int(date_today [3:5])
        y = int(date_today [6:10])

        active_cell = sheet.findall(URL)
        for i in active_cell:
                url_row = i.row
                row_str = str(url_row)

        active_row = 'AS' + row_str
        current_row = sheet.get(active_row)
        current_row_str = str(current_row)
        clean = current_row_str.replace("[","")
        clean1 = clean.replace("]","")
        clean2 = clean1.replace("'","")

        form_date = clean2
        m1 = int(form_date [:2])
        d1 = int(form_date [3:5])
        y1 = int(form_date [6:10])

        d0 = date(y,m,d)
        d00 = date(y1,m1,d1)
        delta = d0 -d00
        delta_days = delta.days
        number_of_days = delta_days

        if number_of_days <= 180:
                time_score = 0
        elif number_of_days <= 365:
                time_score = 50
        elif number_of_days <= 545:
                time_score = 100
        elif number_of_days <= 730:
                time_score = 150
        elif number_of_days > 730:
                time_score = 200

        final_list.append(time_score)
        print(time_score)

        super_total = sum(final_list)/3
        super_dec = super_total/100
        super_per = "{0:.0%}".format(super_dec)

        if super_dec <= .20:
                grade = "A - The application has little risk and would generally recommend."
        elif super_dec <= .40:
                grade = "B - The application has some risk but would generally recommend."
        elif super_dec <= .60:
                grade = "C - The application has some risk and would recommend caution when using the application."
        elif super_dec <= .80:
                grade = "D - The application has serious risk with use and would recommend limited use of the application."
        elif super_dec <= 2:
                grade = "F - Would not recommend the application and would suggest using another application instead."

        active_row = 'AB' + row_str
        sheet.update(active_row, total_dec)
        active_row = 'O' + row_str
        sheet.update(active_row, pprp)
        active_row = 'M' + row_str
        sheet.update(active_row, super_per)
        active_row = 'L' + row_str
        sheet.update(active_row, grade)
        active_row = 'AT' + row_str
        sheet.update(active_row, number_of_days)
        active_row = 'AU' + row_str
        sheet.update(active_row, time_score)

main()
          