from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service()
call= webdriver.Chrome(service=service_obj)
call.get("https://www.qatarairways.com/en-in/homepage")
sleep(2)
call.find_element(By.LINK_TEXT,"Agree").click()
sleep(2)
call.find_element(By.LINK_TEXT,"Book a flight").click()
sleep(2)
call.find_element(By.ID,'bw-from').send_keys("Bhu")
sleep(2)
states=call.find_elements(By.CSS_SELECTOR,"div[class='tt-suggestion tt-selectable flyCity'] strong")
print(len(states))
for state in states:
    if state.text == "BBI":
        state.click()
        break

sleep(5)
call.find_element(By.ID,'bw-to').send_keys("Mum")
call.find_elements(By.CSS_SELECTOR, "div[class='tt-suggestion tt-selectable flyCity'] strong")
sleep(2)
Tostates=call.find_elements(By.CSS_SELECTOR,"div[class='tt-suggestion tt-selectable flyCity'] strong")
print(len(Tostates))
for states in Tostates:
    if states.text=="Mumbai":
        states.click()
        break
call.find_element(By.CSS_SELECTOR,"button[class='submitbutton flightsearh-btn']").click()
sleep(5)









sleep(2)
call.find_element(By.ID,"submitbutton flightsearh-btn").click()
sleep(5)



