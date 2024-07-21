from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service()
call= webdriver.Chrome(service=service_obj)
call.get("https://www.youtube.com/")
call.find_element(By.ID,"search-icon-legacy").click()
call.find_element(By.NAME,"search_query").click()
call.find_element(By.NAME,"search_query").send_keys("Bolly")

call.find_element(By.ID,"search-icon-legacy").click()
sleep(2)
call.find_element(By.CLASS_NAME,"style-scope ytd-video-renderer").click()
call.maximize_window()
sleep(10)





