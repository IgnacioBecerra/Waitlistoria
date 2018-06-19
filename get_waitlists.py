from bs4 import BeautifulSoup
import json

def get_waitlists(code, course):

	# Parsing HTML from requested class
	soup = BeautifulSoup(code, "html.parser")

	# Create list to store information
	class_data = []

	class_data.append(course)

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


	classFile.write('[{"name": ' + '"' + course + '", "sections": [{')
	sectionBool = False
	roomBool = False
	daysBool = False
	timeBool = False
	buildBool = False
	roomBool = False
	waitBool = False
	idBool = False
	profBool = False
	cancelBool = False
	lectureBool = True

	for i, w in enumerate(class_data):
		if i == 0:
			continue
		if w == "FI":
			break

		# Reset booleans if cancelled
		if w == "Cancelled":
			sectionBool = False
			roomBool = False
			daysBool = False
			timeBool = False
			buildBool = False
			roomBool = False
			waitBool = False
			idBool = False
			classFile.write("}")
			cancelBool = True
			lectureBool = False
			continue

		if w == "SE":
			if idBool == False:
				class_data[i] = '"type": "Seminar"'
			else:
				class_data[i] = ', "type": "Seminar"'
			sectionBool = False
			roomBool = False
			daysBool = False
			timeBool = False
			buildBool = False
			roomBool = False
			waitBool = False
			profBool = False
			lectureBool = False

		# Set lecture boolean to skip some categories
		elif w == "LE":
			if idBool == False:
				class_data[i] = '"type": "Lecture"'
			else:
				class_data[i] = ', "type": "Lecture"'
			sectionBool = False
			roomBool = False
			daysBool = False
			timeBool = False
			roomBool = False
			waitBool = False
			profBool = False
			lectureBool = True
			buildBool = False

		elif w == "DI":
			if idBool == False:
				class_data[i] = '"type": "Discussion"'
			else:
				class_data[i] = ', "type": "Discussion"'
			lectureBool = False
			sectionBool = False
			roomBool = False
			daysBool = False
			timeBool = False
			roomBool = False
			waitBool = False
			profBool = False
			buildBool = False

		# Section ID code requirements
		elif w.isdigit() and len(w) == 6 and idBool == False:
			if cancelBool == True or lectureBool == True:
				classFile.write(", {")
				cancelBool = False
			class_data[i] = '"sectionID": ' + '"' + w + '"'
			idBool = True
		
		elif len(w) == 3 and sectionBool == False:
			class_data[i] = ', "section": ' + '"' + w + '"'
			sectionBool = True

		elif daysBool == False:
			class_data[i] = ', "Days": ' + '"' + w + '"'
			daysBool = True
		
		elif timeBool == False:
			class_data[i] = ', "Time": ' + '"' + w + '"'
			timeBool = True

		elif buildBool == False:
			class_data[i] = ', "Building": ' + '"' + w + '"'
			buildBool = True
		
		elif roomBool == False:
			class_data[i] = ', "Room": ' + '"' + w + '"'
			roomBool = True

		# If reading a lecture, reset for next JSON category
		elif profBool == False:
			classFile.write(', "Instructor": ' + '"' + w + '"')
			if lectureBool == True:
				sectionBool = False
				roomBool = False
				daysBool = False
				timeBool = False
				roomBool = False
				waitBool = False
				profBool = False
				buildBool = False
				classFile.write("}")
			
			else:
				profBool = True
			continue
		
		elif waitBool == False:

			# Extract actual numbers if class is full
			if "FULL" in w:
				count = w[w.find("(")+1:w.find(")")]
				class_data[i] = ', "Waitlist": ' + '"' + count + '"'
			else:
				class_data[i] = ', "Available Seats": ' + '"' + w +'"'
			waitBool = True
		else:
			class_data[i] = ', "Seat Limit": ' + '"' + w + '"}'
			cancelBool = True
			idBool = False

		classFile.write(class_data[i])

	# Fill JSON file with data
	#json.dump(class_data, classFile)
	classFile.write("]}]")
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