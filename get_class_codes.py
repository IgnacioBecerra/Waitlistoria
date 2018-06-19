import mechanize
import sys
import json
from bs4 import BeautifulSoup

br = mechanize.Browser()

br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3'),
('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]

br.open('http://ucsd.edu/catalog/front/courses.html')

codes = []
codesFile = open("class_codes.json", 'w')

for link in br.links():
	if "/courses/" in link.url:

		page = br.follow_link(link)

		soup = BeautifulSoup(page.read(), "html.parser")

		for text in soup.findAll("a"):
			
			if text.has_attr('name'):
				codes.append(text['name'])

json.dump(codes, codesFile)
codesFile.close()

