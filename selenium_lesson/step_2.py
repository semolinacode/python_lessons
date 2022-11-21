from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from config import login, passwd


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)

url = 'https://github.com/'
driver.get(url)
driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/div/div[2]/div/div/div[2]/a').click()
driver.find_element(by=By.XPATH, value='//*[@id="login_field"]').send_keys(login)
driver.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys(passwd)
driver.find_element(by=By.XPATH, value='//*[@id="login"]/div[4]/form/div/input[11]').click()




# driver.find_element(by=By.XPATH, value=('/html/body/div[1]/header/div/div[2]/div/div/div[2]/a')).click()
# driver.find_element(by=By.XPATH, value=('//*[@id="password"]')).send_keys(passwd)
# driver.find_element(by=By.XPATH, value=('//*[@id="login_field"]')).send_keys(login) 
# obj1 = driver.find_element(by=By.XPATH, value=('//*[@id="login"]/div[4]/form/div/input[11]')).click()
time.sleep(30)
