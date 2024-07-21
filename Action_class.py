import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service()
driver= webdriver.Chrome(service=service_obj)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
Action_Obj=ActionChains(driver)
webActionObject=driver.find_element(By.ID,"mousehover")
Action_Obj.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
time.sleep(5)
Action_Obj.context_click(webActionObject).perform()
Action_Obj.context_click(driver.find_element(By.XPATH,"//a[.='Reload']")).perform()
