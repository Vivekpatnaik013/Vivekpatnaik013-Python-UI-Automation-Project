from datetime import time
from select import select

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service()
driver= webdriver.Chrome(service=service_obj)

driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
assert driver.current_url,"Successfully opened"
driver.find_element(By.NAME ,"email").send_keys("vivekpatnaik@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()

dropDown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropDown.select_by_index(1)
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message=driver.find_element(By.CLASS_NAME,'alert-success').text
print(message)
assert "Success! The Form has been submitted successfully!" in message
driver.find_element(By.XPATH,"//input[@class='btn btn-success']").click()
driver.find_element(By.XPATH,"(//input[@name='name'])[2]").send_keys('hello vviek')




