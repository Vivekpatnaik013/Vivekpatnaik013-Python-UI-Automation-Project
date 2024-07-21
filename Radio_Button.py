import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service()
driver= webdriver.Chrome(service=service_obj)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
driver.maximize_window()
checkBoxes = driver.find_elements(By.XPATH,"//div[@class='right-align']/fieldset/label/input")
print(len(checkBoxes))

for checkbox in checkBoxes:

    print(checkbox.text)
    if checkbox.get_attribute("id") == "checkBoxOption3":

        checkbox.click()
        assert checkbox.is_selected()
        break


