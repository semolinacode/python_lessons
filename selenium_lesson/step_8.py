from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

import time
# импортируем для нескольких окон
from multiprocessing import Pool

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# открытие нескольких браузеров сразу:
def selenium_start(url):
    try:
        driver.get(url)
        time.sleep(3)
        driver.get_screenshot_as_file(url.split('//')[1].split('.')[0] + '.png')
    except Exception as err:
        print(err)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    p = Pool(processes=3)
    urls = ['https://vk.com/feed', 'https://google.com/', 'https://github.com/']
    p.map(selenium_start, urls)
