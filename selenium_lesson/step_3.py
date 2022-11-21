from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from fake_useragent import UserAgent
import time


options = Options()

options.add_argument(f"user-agent={UserAgent().random}")
# options.add_argument(f"user-agent=hello")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options,
                          )

driver.get('https://www.whatsmyua.info/')
time.sleep(10)
