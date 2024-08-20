import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(""))

driver.get('http://127.0.0.1:5001/users/4')

my_data = driver.find_element(By.ID, 'user')
# driver.find_element(By.CLASS_NAME, value='er8xn').click()
# driver.find_element(By.CLASS_NAME, value='er8xn').send_keys("hello")
# driver.find_element(By.CLASS_NAME, value="blockInner")

time.sleep(100)
print(my_data)