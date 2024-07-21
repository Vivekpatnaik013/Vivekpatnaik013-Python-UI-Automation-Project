import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service()
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='autosuggest']").send_keys("amb")
time.sleep(2)
countries=driver.find_elements(By.XPATH,"//a[@class='ui-corner-all']")
time.sleep(2)
for RequiredCountry in countries:
    if RequiredCountry.text =='Cambodia':
        RequiredCountry.click()

print(driver.find_element(By.XPATH,"//input[@id='autosuggest']").get_attribute('value'))

