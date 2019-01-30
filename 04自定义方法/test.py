# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get('https://huilansame.github.io')
WebDriverWait(driver,20,0.5).until(
    EC.presence_of_element_located((By.LINK_TEXT, 'CSDN')))
print driver.find_element_by_link_text('CSDN').get_attribute('href')
driver.close()

a = ['2018', '12', '14', '09', '28', '59']
for i,v in enumerate(a):
    print (str(i) + "=" + v)
