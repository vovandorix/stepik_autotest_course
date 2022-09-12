from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
####
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
####

link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.get(link)
time.sleep(1)

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
needprice= WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'),'100'))
button1=browser.find_element(By.CSS_SELECTOR, 'button#book')
button1.click()

x=browser.find_element(By.CSS_SELECTOR, '#input_value').text
y=calc(x)

input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
input1.send_keys(str(y))

button2 = browser.find_element(By.CSS_SELECTOR, 'button#solve')
button2.click()
    
    


time.sleep(15)
browser.quit()

