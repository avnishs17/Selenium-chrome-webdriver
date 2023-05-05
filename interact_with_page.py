from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.CSS_SELECTOR,"#articlecount a")
# print(article_count.text)
# article_count.click()

# portals = driver.find_element(By.LINK_TEXT,"Talk")
# portals.click()

search=driver.find_element(By.NAME,"search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.quit()
