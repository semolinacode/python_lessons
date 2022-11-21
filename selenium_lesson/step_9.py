from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

options = Options()

# запуск в режиме демона (для проверки можно добавить принты)
# 1 способ
# options.add_argument('--headless')
# 2 способ
options.headless = True

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('https://google.com/')
print('страничка открылась')
time.sleep(10)
