from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.python.org/")

event_times=driver.find_elements(By.CSS_SELECTOR,".event-widget time")

event_name = driver.find_elements(By.CSS_SELECTOR,".event-widget li a ")

events={}
for n in range(len(event_times)):
	events[n]={
		"time":event_times[n].text,
		"name":event_name[n].text,
	}

print(events)
driver.quit()
