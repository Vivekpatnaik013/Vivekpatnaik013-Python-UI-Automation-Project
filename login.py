from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service()
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(20)
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
print(driver.current_url)
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.XPATH ,"(//div/input[@type='password'])[1]").send_keys('Hello@12345')
driver.find_element(By.ID ,"confirmPassword").send_keys('Hello@12345')
driver.find_element(By.XPATH,"//button[.='Save New Password']").submit()