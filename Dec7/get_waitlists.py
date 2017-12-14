from bs4 import BeautifulSoup
import json

def get_waitlists(code, course):

	# Parsing HTML from requested class
	soup = BeautifulSoup(code, "html.parser")

	# Create list to store information
	class_data = []

	# Obtain class data 
	for td in soup.findAll('td',{'class':'brdr'}):
		text = td.text

		# Taking care of special characters
		if "\n" in text:
			text = text.replace("\n", "")

		if "\t" in text:
			text = text.replace("\t", "")

		# Adding data to list
		text = text.strip()
		class_data.append(text)
		
	# Get rid of empty strings within
	class_data = list(filter(None, class_data))

	# Fill JSON file with data if there's a waitlist
	if class_data:
		course_json = course + ".json"
		classFile = open(course_json, 'w')
		json.dump(class_data, classFile)
		classFile.close()

''' Might actually not need this...
 	# Remove line break that contains the waitlist
	# information for data extraction
	for br in soup.findAll('br'):
		br.extract()

	# Getting full Waitlist string
	for span in soup.findAll('span'):
		st = span.text

		# Obtaining waitlist count
		if "Waitlist(" in st:

			count = st[st.find("(")+1:st.find(")")]
			print count
'''