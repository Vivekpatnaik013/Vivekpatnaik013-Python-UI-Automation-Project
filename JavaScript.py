import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service()
driver= webdriver.Chrome(service=service_obj)
chrOMEOptin=webdriver.ChromeOptions("headless")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.get_screenshot_as_file("homepage.png")
time.sleep(3)