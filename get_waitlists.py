from bs4 import BeautifulSoup


def get_waitlists(code):

	soup = BeautifulSoup(code, "html.parser")

	#print (soup.prettify())
	spans = soup.findAll('br')

	for span in spans:
		span.extract()

	print "PRINT STUFF"

	for a in soup.findAll('span'):
		st = a.text

		# Print only if line has parentheses
		if has_paren(st) == True and "Waitlist" in st:

			text = st[st.find("(")+1:st.find(")")]
			print text

		
# 
def has_paren(str):

	count = 0

	for i in str:
		if i == "(":
			count += 1
		elif i == ")":
			count += 1
	
	if count == 0:
		return False
	else:
		return True