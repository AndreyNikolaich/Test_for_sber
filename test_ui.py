from selenium.webdriver.common.by import By
from selenium import webdriver


def test_dokhodcivo():
    wd = webdriver.Chrome()
    link = "https://google.com/"
    wd.get(link)
    wd.find_element(By.CSS_SELECTOR, '[class="gLFyf gsfi"]').send_keys('dokhodchivo.ru')
    wd.find_element(By.XPATH, '//div[3]/center/input').click()
    #site = "https://dokhodchivo.ru/"
    #for i in site:
    wd.find_element(By.LINK_TEXT, 'https://dokhodchivo.ru/').click()





