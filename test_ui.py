from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


def test_dokhodcivo():
    wd = webdriver.Chrome()
    wd.maximize_window()
    wd.implicitly_wait(10)
    link = "https://google.com/"
    wd.get(link)
    wd.find_element(By.CSS_SELECTOR, '[class="gLFyf gsfi"]').send_keys('dokhodchivo.ru')
    time.sleep(1)
    wd.find_element(By.XPATH, '//input[@name="btnK"]').click()
    wd.find_element(By.XPATH, '//div[@id="rso"]/div/div/div/div/div/div/div/a/div/cite').click()
    wd.execute_script("window.scrollTo (0, 7000)")
    element = []
    block = wd.find_elements(By.CSS_SELECTOR, '#__next > div > div._2hzFm > div.kZLWL > main > div:nth-child(11) '
                                              '> div > ul li')
    for i in block:
        element.append(block)
    assert len(element) == 6
    button = wd.find_element(By.XPATH, '//div[@id="__next"]/div/div/div[2]/main/div[4]/div/button')
    wd.execute_script("window.scrollTo (0, 7963)")
    time.sleep(1)
    ActionChains(wd).move_to_element(button).pause(1).click().perform()
    time.sleep(3)
    element2 = []
    block2 = wd.find_elements(By.CSS_SELECTOR, '#__next > div > div._2hzFm > div.kZLWL > main > div:nth-child(11) '
                                               '> div > ul li')
    time.sleep(3)
    for i in block2:
        element2.append(block2)
    assert len(element2) == 12
    name_main = wd.find_element(By.CSS_SELECTOR, '#__next > div > div._2hzFm > div.kZLWL > main > div:nth-child(3) > '
                                                 'div > ul > li:nth-child(1) > div > div > div:nth-child(2) > a p').text
    wd.find_element(By.XPATH, '// div [4] / div / ul / li / div / a / picture / img').click()
    time.sleep(3)
    name_news = wd.find_element(By.XPATH, '// h1').text
    assert name_news == name_main


























