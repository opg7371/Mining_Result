import re
import requests
from bs4 import BeautifulSoup
import mechanize
import html5lib
import urllib3

#requests.packages.urllib3.disable_warnings()
handle = open('result.html','w')
#scholar_no = raw_input("Please enter your username. ")
#semister = raw_input("Please input your password. ")
scholar_no='131114001'
semister = '5'
URL = "http://dolphintechnologies.in/manit/results.html"    
#handle = requests.get("http://www.manit.ac.in/manitbpl/").text
br = mechanize.Browser()
br.set_handle_robots(False)
br.open(URL)    
br.select_form(nr=0)

br.form['scholar'] = scholar_no
br.form['semester'] = [semister,]
print br.form
# Login 
br.submit() 
handle.write(br.response().read())
# print page title to confirm proper login
print br.title()
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


para = re.findall(r'<span>(.*?)</span>',soup)
print para
