# pip install selenium

from selenium import webdriver


# driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path='/Users/riocrash/Downloads/chromdriver')
# driver = webdriver.Chrome(executable_path='./chromedriver')

driver.get("http://selenium.dev")

input('Нажмите Enter чтобы завершить программу')
driver.quit()
