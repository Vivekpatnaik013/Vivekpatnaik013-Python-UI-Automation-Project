import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service()
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(6)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//input[@type='search']").click()
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("um")
time.sleep(2)
List_OfProduct=driver.find_elements(By.XPATH,"//div[@class='product']")
for product in List_OfProduct:
    product.find_element(By.XPATH,"//div/button[.='ADD TO CART']").click()
    time.sleep(1)
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
#time.sleep(1)
driver.find_element(By.XPATH,"//button[.='PROCEED TO CHECKOUT']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//input[@placeholder='Enter promo code']").click()
driver.find_element(By.XPATH,"//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()
print(driver.find_element(By.XPATH,"//span[.='Code applied ..!']").text)
#time.sleep(5)
Listprice =driver .find_elements(By.XPATH,"//table//tbody/tr/td[5]")

sum=0
for price in Listprice:
    sum=sum+ int(price.text )

print("Total price after discount  is :",sum)
