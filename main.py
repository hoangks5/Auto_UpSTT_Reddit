from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

user = input('Nhập username: ')
mk = input('Nhập password: ')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.reddit.com/login/')
time.sleep(1)
driver.find_element_by_id('loginUsername').send_keys(user)
driver.find_element_by_id('loginPassword').send_keys(mk)
time.sleep(1)
driver.find_element_by_id('loginPassword').send_keys(Keys.ENTER)
time.sleep(5)
listgr = open('linkgr.txt','r',encoding='utf-8').read().splitlines()
while True:
    for link in listgr:
        try:
            driver.get(link)
            time.sleep(2)
            __title = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div[1]/div/textarea')
            __title.send_keys(open('title.txt','r',encoding='utf-8').read())
            time.sleep(1)
            __text = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/div[3]/div/div[1]/div/div/div')
            text = open('text.txt','r',encoding='utf-8').read()
            
         
            time.sleep(100000)
            __text.send_keys(text)
            time.sleep(100000)
            #__text.send_keys('')
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[3]/div[2]/div/div[1]/button').click()
            time.sleep(int(open('time.txt','r',encoding='utf-8').read()))
        except:
            pass