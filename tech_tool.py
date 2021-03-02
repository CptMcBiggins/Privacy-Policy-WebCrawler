#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import re
import argparse
import gspread
from oauth2client.service_account import ServiceAccountCredentials

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

utlist = []
total_risk_score = []
final_list = []

def main():
        def u1():
                print("Running Usage Section 1 Evaluation")
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
                for i in active_cell:
                        url_row = i.row
                        row_str = str(url_row)
                
                choice_value_list = []
                active_row = 'F' + row_str
                current_row = sheet.get(active_row)
                current_row_str = str(current_row)
                for i in list1:
                        if i in current_row_str:
                                list_index = (list1.index(i))
                                index_value = list2[list_index]
                                choice_value_list.append(index_value)
                
                choices = len(choice_value_list)
                math = round(sum(choice_value_list)/choices, 2)

                utlist.append(math)
                actives_row = 'P' + row_str
                sheet.update(actives_row, math)
        u1()    

        def u2():
                print("Running Usage Section 2 Evaluation")
                a, e = "Teachers", 49
                b, f = "Students", 42
                c, g = "Non-Teaching Staff", 63
                d, h = "Parents", 20
                list1 = [a,b,c,d]
                list2 = [e,f,g,h]
                
                active_cell = sheet.findall(URL)
                for i in active_cell:
                        url_row = i.row
                        row_str = str(url_row)  

                choice_value_list = []
                active_row = 'G' + row_str
                current_row = sheet.get(active_row)
                current_row_str = str(current_row)
                for i in list1:
                        if i in current_row_str:
                                list_index = (list1.index(i))
                                index_value = list2[list_index]
                                choice_value_list.append(index_value)   

                choices = len(choice_value_list)
                math = round(sum(choice_value_list)/choices, 2)

                utlist.append(math)
                actives_row = 'Q' + row_str
                sheet.update(actives_row, math)
        u2()    

        def u3():
                print("Running Usage Section 3 Evaluation")
                a, d = "No account needed/access with class or invite code", 3
                b, e = "SSO Login with Google or Microsoft (i.e., school login)", 60
                c, f = "Separate account needed", 42
                list1 = [a,b,c]
                list2 = [d,e,f]
                
                active_cell = sheet.findall(URL)
                for i in active_cell:
                        url_row = i.row
                        row_str = str(url_row)  

                choice_value_list = []
                active_row = 'H' + row_str
                current_row = sheet.get(active_row)
                current_row_str = str(current_row)
                for i in list1:
                        if i in current_row_str:
                                list_index = (list1.index(i))
                                index_value = list2[list_index]
                                choice_value_list.append(index_value)   

                choices = len(choice_value_list)
                math = round(sum(choice_value_list)/choices, 2)

                utlist.append(math)
                actives_row = 'R' + row_str
                sheet.update(actives_row, math)
        u3()    

        def u4():
                print("Running Usage Section 4 Evaluation")
                a, e = "Primary (PK-2)", 35
                b, f = "Elementary (3-5)", 49
                c, g = "Middle School/Junior High (6-8)", 56
                d, h = "High School (9-12)", 72
                list1 = [a,b,c,d]
                list2 = [e,f,g,h]       

                active_cell = sheet.findall(URL)
                for i in active_cell:
                        url_row = i.row
                        row_str = str(url_row)  

                choice_value_list = []
                active_row = 'I' + row_str
                current_row = sheet.get(active_row)
                current_row_str = str(current_row)
                for i in list1:
                        if i in current_row_str:
                                list_index = (list1.index(i))
                                index_value = list2[list_index]
                                choice_value_list.append(index_value)   

                choices = len(choice_value_list)
                math = round(sum(choice_value_list)/choices, 2)

                utlist.append(math)
                actives_row = 'S' + row_str
                sheet.update(actives_row, math)
        u4()    

        def ut():
                print("Running Total Usage Evaluation")
                active_cell = sheet.findall(URL)
                for i in active_cell:
                        url_row = i.row
                        row_str = str(url_row)  

                utaverage = round(sum(utlist)/4, 2)
                utmaxav = 195.75
                utdec = round(utaverage/utmaxav, 2)
                final_list.append(utdec)
                utper = "{0:.0%}".format(utdec) 

                actives_row = 'T' + row_str
                sheet.update(actives_row, utaverage)
                actives_row = 'N' + row_str
                sheet.update(actives_row, utper)
        ut()

        def coppa():
                print("Running Privacy Policy COPPA Evaluation")
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
                medium = 50
                high = 100
                zero = 280

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

                active_row = 'U' + row_str
                pp_risk_str = 'AK' + row_str
                pp_risk_score = 'AD' + row_str
                sheet.update(active_row, listToStr)
                sheet.update(pp_risk_str, ppstr)
                sheet.update(pp_risk_score, pprs)
        coppa()

        def p1():
                print("Running Privacy Policy Section 1 Evaluation")
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
                medium = 50
                high = 100
                zero = 280

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
                
                active_row = 'V' + row_str
                pp_risk_str = 'AL' + row_str
                pp_risk_score = 'AE' + row_str
                sheet.update(active_row, listToStr)
                sheet.update(pp_risk_str, ppstr)
                sheet.update(pp_risk_score, pprs)
        p1()
        
        def p2():
                print("Running Privacy Policy Section 2 Evaluation")
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
                medium = 50
                high = 100
                zero = 280

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

                active_row = 'W' + row_str
                pp_risk_str = 'AM' + row_str
                pp_risk_score = 'AF' + row_str
                sheet.update(active_row, listToStr)
                sheet.update(pp_risk_str, ppstr)
                sheet.update(pp_risk_score, pprs)
        p2()

        def p3():
                print("Running Privacy Policy Section 3 Evaluation")
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
                medium = 50
                high = 100
                zero = 280

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

                active_row = 'X' + row_str
                pp_risk_str = 'AN' + row_str
                pp_risk_score = 'AG' + row_str
                sheet.update(active_row, listToStr)
                sheet.update(pp_risk_str, ppstr)
                sheet.update(pp_risk_score, pprs)
        p3()

        def p4():
                print("Running Privacy Policy Section 4 Evaluation")
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
                medium = 50
                high = 100
                zero = 280

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

                active_row = 'Y' + row_str
                pp_risk_str = 'AO' + row_str
                pp_risk_score = 'AH' + row_str
                sheet.update(active_row, listToStr)
                sheet.update(pp_risk_str, ppstr)
                sheet.update(pp_risk_score, pprs)
        p4()

        def p5():
                print("Running Privacy Policy Section 5 Evaluation")
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
                medium = 50
                high = 100
                zero = 280

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

                active_row = 'Z' + row_str
                pp_risk_str = 'AP' + row_str
                pp_risk_score = 'AI' + row_str
                sheet.update(active_row, listToStr)
                sheet.update(pp_risk_str, ppstr)
                sheet.update(pp_risk_score, pprs)
        p5()
        
        def contact():
                print("Running Privacy Policy Contact Evaluation")
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
                medium = 50
                high = 100
                zero = 280

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
        
                active_row = 'AA' + row_str
                pp_risk_str = 'AQ' + row_str
                pp_risk_score = 'AJ' + row_str
                sheet.update(active_row, clean)
                sheet.update(pp_risk_str, ppstr)
                sheet.update(pp_risk_score, pprs)
        contact()

        def rs():
                print("Running Privacy Policy Total Risk Evaluation")
                active_cell = sheet.findall(URL)
                for i in active_cell:
                        url_row = i.row
                        row_str = str(url_row)

                risk_score = sum(total_risk_score)/7
                total = 100
                total_dec = round(risk_score/total, 2)
                final_list.append(total_dec)
                pprp = "{0:.0%}".format(total_dec)

                super_total = sum(final_list)/2
                super_per = "{0:.0%}".format(super_total)

                if super_total <= .20:
                        grade = "A"
                elif super_total <= .40:
                        grade = "B"
                elif super_total <= .60:
                        grade = "C"
                elif super_total <= .80:
                        grade = "D"
                elif super_total <= 2:
                        grade = "F"

                active_row = 'AB' + row_str
                sheet.update(active_row, total_dec)
                active_row = 'O' + row_str
                sheet.update(active_row, pprp)
                active_row = 'M' + row_str
                sheet.update(active_row, super_per)
                active_row = 'L' + row_str
                sheet.update(active_row, grade)
        rs()
main()
print("Evaluation Finished!")
