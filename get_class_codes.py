import mechanize
import sys
from urllib.request import urlopen
import sys
from bs4 import BeautifulSoup

br = mechanize.Browser()

#br.set_all_readonly(False)    # allow everything to be written to
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3'),
('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]

br.open('http://ucsd.edu/catalog/front/courses.html')

for link in br.links():
	if "/courses/" in link.url:

		page = br.follow_link(link)
		url = urlopen(page.url)
		soup = BeautifulSoup(url, "html.parser")

	#print link.text, link.url
