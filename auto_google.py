from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
time.sleep(1)
driver.get("http://www.google.com")
assert "Google" in driver.title

elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("wellax.care")
elem.send_keys(Keys.RETURN)
time.sleep(20)
assert "No results found." not  in  driver.page.page_source
driver.close()
