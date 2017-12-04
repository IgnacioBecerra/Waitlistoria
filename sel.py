from selenium import webdriver
from selenium.webdriver.chrome.options import Options 

chrome_options = Options()  
chrome_options.add_argument("--headless")  
br = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:/Users/PokeDanny10/Desktop/VN/chromedriver.exe')  
br.get("https://act.ucsd.edu/scheduleOfClasses/scheduleOfClassesStudent.htm")

# Clicks on courses tab
tabButton = br.find_element_by_xpath('//*[@id="tabs"]/ul/li[4]/a')
tabButton.click()

# Types search terms for a course
element = br.find_element_by_id('courses')
element.clear()
element.send_keys("CSE 100")

# Submits form
element = br.find_element_by_xpath('//*[@id="socFacSubmit"]')
element.click()

print br.page_source
