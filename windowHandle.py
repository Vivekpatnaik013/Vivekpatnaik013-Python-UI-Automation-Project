import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service()
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
time.sleep(4)
openWindows= driver.window_handles
driver.switch_to.window(openWindows[1])
headline=driver.find_element(By.TAG_NAME,"h3")
print(headline.text)
driver.switch_to.window(openWindows[0])
headline=driver.find_element(By.TAG_NAME,"h3")
print(headline.text)


