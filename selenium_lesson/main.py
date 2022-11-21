from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

import config

EXTENSION_PATH = f'/Users/riocrash/Library/Application Support/Google/Chrome/Default/Extensions/{config.EXTENSION_ID}/10.21.2_0.crx'
# nkbihfbeogaeaoehlefnkodbefgpgknn
options = Options()
options.add_extension(EXTENSION_PATH)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(10)

# print(driver.window_handles)
# print(driver.current_window_handle)

metamask_extension_handle = driver.window_handles[0]
general_handle = driver.window_handles[1]
# driver.switch_to.window(general_handle)
# driver.get_screenshot_as_file('./filename.png')
driver.switch_to.window(metamask_extension_handle)
# # driver.get_screenshot_as_file('./filename2.png')


driver.find_element(by=By.XPATH, value=('//*[@id="app-content"]/div/div[2]/div/div/div/button')).click()
driver.find_element(by=By.XPATH, value=('//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]')).click()
driver.find_element(by=By.XPATH, value=('//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button')).click()

inputs = driver.find_elements(by=By.CSS_SELECTOR, value='input')

for word, num in zip(config.SECRET_RECOVERY_PHRASE, range(len(config.SECRET_RECOVERY_PHRASE))):
    driver.find_element(by=By.ID, value=f'import-srp__srp-word-{num}').send_keys(word)
driver.find_element(by=By.XPATH, value=('//*[@id="password"]')).send_keys(config.NEW_PASSWORD)
driver.find_element(by=By.XPATH, value=('//*[@id="confirm-password"]')).send_keys(config.NEW_PASSWORD)

# галочка
driver.find_element(by=By.XPATH, value=('//*[@id="create-new-vault__terms-checkbox"]')).click()
# кнопка импорт
driver.find_element(by=By.XPATH, value=('//*[@id="app-content"]/div/div[2]/div/div/div[2]/form/button')).click()
# done button
driver.find_element(by=By.XPATH, value=('//*[@id="app-content"]/div/div[2]/div/div/button')).click()

# ---------------------------------------------------------------------------------------------------------------------------


# driver.execute_script("window.open('');")
driver.switch_to.window(general_handle)
# driver.get(f'chrome-extension://{config.EXTENSION_ID}/popup.html')
# time.sleep(20)

url = 'https://chainlist.org/chain/56'
driver.get(url)

# нажимаем на кнопку "подключить кошелек"
driver.find_element(by=By.XPATH, value=('//*[@id="__next"]/div[1]/main/div/div[2]/div[1]/button/span[1]/h5/p')).click()

mm_handle = driver.window_handles[2]

# print('------------------------')
# print(driver.window_handles)
# print()
# print(driver.current_window_handle)
driver.switch_to.window(mm_handle)

# нажимаем "далее"
driver.find_element(by=By.XPATH, value=('//*[@id="app-content"]/div/div[2]/div/div[3]/div[2]/button[2]')).click()
# нажимаем "подключиться"
driver.find_element(by=By.XPATH, value=('//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]')).click()


driver.switch_to.window(general_handle)
# нажимаем "add to metamask"
driver.find_element(by=By.XPATH, value=('//*[@id="__next"]/div[1]/main/div/div[2]/div[2]/button/span[1]')).click()

driver.switch_to.window(driver.window_handles[2])
# нажимаем "одобрить"
driver.find_element(by=By.XPATH, value=('//*[@id="app-content"]/div/div[2]/div/div[2]/div/button[2]')).click()
driver.find_element(by=By.XPATH, value=('//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/button[2]')).click()

time.sleep(60)