import re
import requests
from bs4 import BeautifulSoup
import mechanize
import html5lib
import urllib3

#requests.packages.urllib3.disable_warnings()
#scholar_no = raw_input("Please enter your username. ")

#semister = raw_input("Please input your password. ")
scholar_no = int(raw_input("Please Enter the starting scholar number:"))
scholar_no_end = int(raw_input("Please Enter the ending scholar number:"))
semister = '5'
URL = "http://dolphintechnologies.in/manit/results.html"    
#handle = requests.get("http://www.manit.ac.in/manitbpl/").text
while scholar_no<scholar_no_end : 
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.open(URL)    
	sch_no = str(scholar_no)
	br.select_form(nr=0)
	handle = open("Results/result_"+sch_no+".html",'w')
	br.form['scholar'] = sch_no
	br.form['semester'] = [semister,]
	print br.form
	# Login 
	br.submit() 
	handle.write(br.response().read())
	# print page title to confirm proper login
	print br.title()
	scholar_no=scholar_no+1
	#print br.response().read()
	#print br.read()

soup = BeautifulSoup(open("result.html"))
print soup.prettify()
#soup = BeautifulSoup(handle, 'html.parser')
#print soup.p['style17']
#print tag['style17']
#for link in soup.find_all('span'):
	#print link.get('class').text
#tag = soup.span
#print type(tag)
#print soup.body.div


para = re.findall(r'*:*',soup)
print para
