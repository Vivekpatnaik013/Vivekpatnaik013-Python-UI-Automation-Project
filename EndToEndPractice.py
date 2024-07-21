from datetime import time
from select import select
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Action_class import service_obj

cdservice_obj=Service()
driver= webdriver.hrome(service=service_obj)
driver.implicitly_wait(6)
driverget("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH,"//a[.='Shop']").click()
ProductList=driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in ProductList:

    result=product.find_element(By.XPATH,"div/h4/a")
    if(result.text=="Nokia Edge"):
        product.find_element(By.XPATH,"div/button").click()
driver.find_element(By.XPATH,"//a[contains(@class,'btn-primary')]").click()
driver.find_element(By.XPATH,"(//button[@class='btn btn-success'])[1]").click()
driver.find_element(By.ID,"country").send_keys("India")
driver.find_element(By.XPATH,"//div[@class='suggestions']/ul/li/a").click()
time.sleep(5)
driver.find_element(By.XPATH,"//div/label[@for='checkbox2']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
text=driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']")
print(text.text)
assert text.text.__contains__("Success! Thank you! Your order will be delivered in next few weeks :-).")
time.sleep(2)

driver.close()






