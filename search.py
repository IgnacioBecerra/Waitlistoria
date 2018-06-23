from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from get_waitlists import get_waitlists
import time
import json

def search(course):

	# Clicks on courses tab
	tabButton = br.find_element_by_xpath('//*[@id="tabs"]/ul/li[4]/a')
	tabButton.click()

	# Types search terms for a course
	element = br.find_element_by_xpath('//*[@id="courses"]')
	element.clear()
	element.send_keys(course)

	# Submits form
	element = br.find_element_by_xpath('//*[@id="socFacSubmit"]')
	element.click()

	element = br.find_element_by_xpath('//*[@id="socDisplayCVO"]/div[2]')

	if "No Result Found." not in element.text:
		get_waitlists(br.page_source, course)
	else:
		print("no" + course)

	br.get("https://act.ucsd.edu/scheduleOfClasses/scheduleOfClassesStudent.htm")


chrome_options = Options()  
chrome_options.add_argument("--headless")  
br = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'./chromedriver.exe')  
br.get("https://act.ucsd.edu/scheduleOfClasses/scheduleOfClassesStudent.htm")

# Chooses quarter
#element = br.find_element_by_xpath('//*[@id="selectedTerm"]/option[6]').click()

with open('./class_codes.json') as f:
    data = json.load(f)

#for c in data:
search("CSE8a")

br.quit()




	