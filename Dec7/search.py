from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from get_waitlists import get_waitlists


def search(course):

	chrome_options = Options()  
	chrome_options.add_argument("--headless")  
	br = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'./chromedriver.exe')  
	br.get("https://act.ucsd.edu/scheduleOfClasses/scheduleOfClassesStudent.htm")

	# Clicks on courses tab
	tabButton = br.find_element_by_xpath('//*[@id="tabs"]/ul/li[4]/a')
	tabButton.click()

	# Types search terms for a course
	element = br.find_element_by_id('courses')
	element.clear()
	element.send_keys(course)

	# Submits form
	element = br.find_element_by_xpath('//*[@id="socFacSubmit"]')
	element.click()

	get_waitlists(br.page_source, course)

