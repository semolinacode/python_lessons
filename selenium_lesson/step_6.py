from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pickle
from fake_useragent import UserAgent

from config import rambler_login, rambler_passwd


options = Options()
options.add_argument(f"user-agent={UserAgent().random}")
options.add_argument('--disable-blink-features=AutomationControlled')

cookies_path = 'my_cookies.dat'
driver = webdriver.Chrome(
                        service=Service(ChromeDriverManager().install()), 
                        options=options
                        )

url = 'https://id.rambler.ru/login-20/login?rname=head&session=false&back=https%3A%2F%2Fwww.rambler.ru%2F&param=iframe&iframeOrigin=https%3A%2F%2Fwww.rambler.ru'
driver.get(url)
time.sleep(3)
driver.find_element(by=By.XPATH, value=('//*[@id="login"]')).send_keys(rambler_login)
time.sleep(3)
driver.find_element(by=By.XPATH, value=('//*[@id="password"]')).send_keys(rambler_passwd)
time.sleep(1)
driver.find_element(by=By.XPATH, value=('//*[@id="__next"]/div/div/div[2]/div/div/div/div[1]/form/button/span')).click()
# время на ввод капчи
time.sleep(50)

inbox_url = 'https://mail.rambler.ru/folder/INBOX/'
driver.get(inbox_url)

# выгрузим cookies в файл:
with open(cookies_path, 'wb') as f:
    pickle.dump(driver.get_cookies(), f)
