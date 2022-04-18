from db.main import database
from json_.main import json_
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from create_all import create_all
import time
import os

name = input("enter name of file: ")
url = input("enter playlists of soundcloud: ")
urls = []

driver = webdriver.Chrome(executable_path='.\chromedriver.exe')
try:
    driver.get(url)
    print("scroll down.")
    time.sleep(20)
    try:
        links = driver.find_elements(By.CSS_SELECTOR, 'a.sc-link-dark')
        for link in links:
            try:
                if link.get_attribute('href') in urls:
                    continue
                else:
                    urls.append(link.get_attribute('href'))
            except:
                if urls:
                    if '.' in name:
                        new_name = name[:name.find('.')]
                        os.mkdir(new_name)
                        create_all.all(path=new_name, name=name, datas=urls)
                    else:
                        os.mkdir(name)
                        create_all.all(path=name, name=name, datas=urls)
    except NoSuchElementException:
        print("can't find this element")
except Exception as e:
    print("error on this url => {0}, reason => {1}".format(url, e))

if urls:
    if '.' in name:
        new_name = name[:name.find('.')]
        os.mkdir(new_name)
        create_all.all(path=new_name, name=name, datas=urls)
    else:
        os.mkdir(name)
        create_all.all(path=name, name=name, datas=urls)