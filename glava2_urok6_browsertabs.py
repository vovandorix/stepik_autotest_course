from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)
time.sleep(1)

button1=browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
button1.click()

first_window = browser.window_handles[0]
new_window = browser.window_handles[1]

browser.switch_to.window(new_window)

x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
y=calc(x)

input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
input1.send_keys(str(y))


button1 = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
button1.click()
    
time.sleep(15)
browser.quit()
