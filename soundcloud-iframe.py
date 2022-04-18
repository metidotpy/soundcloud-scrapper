from db.main import database
from json_.main import json_
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from create_all import create_all
import time


name_of_path = input("enter path name: ")
urls = json_.read_data(path=name_of_path, name=name_of_path)
iframes = {}

driver = webdriver.Chrome(executable_path='.\chromedriver.exe')
action = ActionChains(driver=driver)

for index, url in enumerate(urls):
    try:
        driver.get(url)
        if index == 0:
            time.sleep(5)
        else:
            time.sleep(3)
        name = driver.find_element(By.CSS_SELECTOR, '#content > div > div.l-listen-hero > div > div.fullHero__foreground.fullListenHero__foreground.sc-p-4x > div.fullHero__title > div > div > div.soundTitle__usernameTitleContainer.sc-mb-0\.5x > div.soundTitle__titleHeroContainer > h1 > span').text
        author = driver.find_element(By.CSS_SELECTOR, '#content > div > div.l-listen-hero > div > div.fullHero__foreground.fullListenHero__foreground.sc-p-4x > div.fullHero__title > div > div > div.soundTitle__usernameTitleContainer.sc-mb-0\.5x > div.soundTitle__usernameHeroContainer > h2 > a').text
        author_link = driver.find_element(By.CSS_SELECTOR, '#content > div > div.l-listen-hero > div > div.fullHero__foreground.fullListenHero__foreground.sc-p-4x > div.fullHero__title > div > div > div.soundTitle__usernameTitleContainer.sc-mb-0\.5x > div.soundTitle__usernameHeroContainer > h2 > a').get_attribute('href')
        share = driver.find_element(By.CLASS_NAME, 'sc-button-share')
        share.click()
        time.sleep(1.0)
        try:
            embed = driver.find_element(By.CSS_SELECTOR, 'li.g-tabs-item:nth-child(2) > a:nth-child(1)')
        except NoSuchElementException:
            print('this playlist {0} dont have iframe.'.format(url))
            continue
        embed.click()
        time.sleep(0.7)
        iframe = driver.find_element(By.CSS_SELECTOR, '.widgetCustomization__textInput')
        try:
            if iframe.get_attribute('value') in iframes:
                continue
            else:
                iframes[url] = [name, author, author_link, iframe.get_attribute('value')]
        except:
            if iframes:
                create_all.all_iframe(path=name_of_path, name='iframes', datas=iframes)
                break
    except Exception as e:
        print('error on this url => {0}, reason => {1}'.format(url, e))

if iframes:
    create_all.all_iframe(path=name_of_path, name='iframes', datas=iframes)
