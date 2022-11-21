from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# from selenium import webdriver
from seleniumwire import webdriver
from fake_useragent import UserAgent

import time
# импортируем для работы с cookies
import pickle
# импортируем для нескольких окон
from multiprocessing import Pool


options = Options()

# запуск в режиме демона (для проверки можно добавить принты)
# 1 сп
# options.add_argument('--headless')
# 2 сп
# options.headless = True

# change useragent
options.add_argument(f"user-agent={UserAgent().random}")

# отключаем webrdiver-mode:
options.add_argument('--disable-blink-features=AutomationControlled')

# set proxy (без авторизации)
# options.add_argument(f"--proxy-server=138.138.13.38:8000")

# прокси с авторизацией и без привязки к своему ip
# pip install selenium-wire
login = 'TVNfPJ'
password = 'gEdNA1'
proxy_options = {
    'proxy': {
        # протокол: 
        'http': f'http://{login}:{password}@163.198.233.185:8000',
        'https': f'https://{login}:{password}@163.198.233.185:8000',
    }
}
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options,
                          seleniumwire_options=proxy_options
                          )

# cookies_path = 'my_cookies.dat'
# показать на примере rambler

# выгрузим cookies в файл:
# with open(cookies_path, 'wb') as f:
#     pickle.dump(driver.get_cookies(), f)

# засунем cookies в браузер:
# with open(cookies_path, 'rb') as f:
#     for cookie in pickle.load(f):
#         driver.add_cookie(cookie)
# time.sleep(2)
# обновим страницу:
# driver.refresh()


driver.get('https://www.whatsmyua.info/')
time.sleep(5)
driver.get('https://2ip.ru')
time.sleep(5)
driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
time.sleep(30)


# # открытие нескольких браузеров сразу:
# def selenium_start(url):
#     try:
#         driver.get(url)
#         time.sleep(3)
#         driver.get_screenshot_as_file(url.split('//')[1].split('.')[0] + '.png')
#     except Exception as err:
#         print(err)
#     finally:
#         driver.close()
#         driver.quit()


# if __name__ == '__main__':
#     p = Pool(processes=3)
#     urls = ['https://vk.com/feed', 'https://google.com/', 'https://github.com/crashnosok']
#     p.map(selenium_start, urls)