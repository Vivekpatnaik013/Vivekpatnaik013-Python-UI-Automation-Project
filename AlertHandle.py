import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service()
driver= webdriver.Chrome(service=service_obj)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
driver .find_element(By.CSS_SELECTOR,"#name").click()
driver .find_element(By.CSS_SELECTOR,"#name").send_keys("Vivek")
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
AlertObject=driver.switch_to.alert
print(AlertObject.text)
assert "Vivek" in AlertObject.text
time.sleep(4)
AlertObject.accept()

