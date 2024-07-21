import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service()
driver= webdriver.Chrome(service=service_obj)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
RadioButtons=driver.find_elements(By.XPATH,"//div[@class='left-align']/fieldset/label/input")
for RadioButton in RadioButtons:
    if RadioButton.get_attribute("value")=="radio1":
        RadioButton.click()
        assert RadioButton.is_selected()
        break