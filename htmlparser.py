from bs4 import BeautifulSoup
import re

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


#para = re.findall(r'<span>(.*?)</span>',soup)
#rint para
