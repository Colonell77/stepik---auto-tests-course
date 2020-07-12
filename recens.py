from selenium import webdriver
import time
# from selenium.webdriver.support.ui import Select
import math
# import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

browser.find_element_by_id('book').click()
x = browser.find_element_by_id('input_value').text
result = math.log(abs(12*math.sin(int(x))))
browser.find_element_by_id('answer').send_keys(str(result))
browser.find_element_by_id('solve').click()
time.sleep(600)
