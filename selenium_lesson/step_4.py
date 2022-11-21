from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
# from selenium import webdriver
from seleniumwire import webdriver
from fake_useragent import UserAgent

from config import proxy_login, proxy_passwd

options = Options()
options.add_argument(f"user-agent={UserAgent().random}")

# set proxy (без авторизации)
# options.add_argument(f"--proxy-server={ip}:{port}")

# прокси с авторизацией и без привязки к своему ip
proxy_options = {
    'proxy': {
        # протокол: 
        'http': f'http://{proxy_login}:{proxy_passwd}@163.198.233.185:8000',
        'https': f'https://{proxy_login}:{proxy_passwd}@163.198.233.185:8000',
    }
}
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options,
                          seleniumwire_options=proxy_options
                          )

driver.get('https://2ip.ru')
time.sleep(10)
