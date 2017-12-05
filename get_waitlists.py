from bs4 import BeautifulSoup

def get_waitlists(code):
	soup = BeautifulSoup(code, "html.parser")
	spans = soup.find_all('span', attrs={'id':''})
	
	for span in spans:
    	print span.string