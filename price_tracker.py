from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.flipkart.com/apple-iphone-13-starlight-128-gb/p/itmc9604f122ae7f?pid=MOBG6VF5ADKHKXFX&lid=LSTMOBG6VF5ADKHKXFXQGX7PK&marketplace=FLIPKART&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=b_1_1&otracker=clp_bannerads_1_23.bannerAdCard.BANNERADS_iPhone%2B13%2B-%2BEnglish%2B_mobile-phones-store_KBHC1UXU8IWQ&fm=organic&iid=7a020c93-6c36-4e1d-9d95-c47de0ed4688.MOBG6VF5ADKHKXFX.SEARCH&ppt=browse&ppn=browse&ssid=2gpftrazuo0000001682962629386")

# price=driver.find_element(By.CLASS_NAME,"_25b18c")
price2=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]')

# print(price2.text)
PRICE= price2.text.split("₹")

print(int((PRICE[1].replace(",",""))))

driver.quit()