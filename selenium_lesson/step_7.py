from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import pickle
from fake_useragent import UserAgent


options = Options()
options.add_argument(f"user-agent={UserAgent().random}")
options.add_argument('--disable-blink-features=AutomationControlled')

cookies_path = 'my_cookies.dat'
driver = webdriver.Chrome(
                        service=Service(ChromeDriverManager().install()), 
                        options=options
                        )

general_url = 'https://www.rambler.ru/'
driver.get(general_url)
time.sleep(5)

# засунем cookies в браузер:
with open(cookies_path, 'rb') as f:
    for cookie in pickle.load(f):
        driver.add_cookie(cookie)

time.sleep(2)
# обновим страницу:
driver.refresh()
time.sleep(5)

inbox_url = 'https://mail.rambler.ru/folder/INBOX/'
driver.get(inbox_url)

print('the end')
time.sleep(50)
