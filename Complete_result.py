import nlkt   
from urllib import urlopen
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

