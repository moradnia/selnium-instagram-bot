import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.ui import Select
import time
import random
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.instagram.com/accounts/emailsignup/'


class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def log_in(self):
        driver = self.driver
        driver.get(url)
        WebDriverWait(driver, 10).until(Ec.element_to_be_clickable((By.LINK_TEXT, 'Log in'))).click()
        driver.maximize_window()

    def info(self):
        driver = self.driver
        username = WebDriverWait(driver, 10).until(Ec.element_to_be_clickable((By.NAME, 'username'))).send_keys(
            '<username>')
        password = WebDriverWait(driver, 10).until(Ec.element_to_be_clickable((By.NAME, 'password'))).send_keys(
            '<password>' + Keys.ENTER)

    def notif(self):
        driver = self.driver
        time.sleep(5)
        btn_2 = driver.find_element_by_css_selector('button[type="button"]').click()
        time.sleep(5)
        btn_3 = driver.find_element_by_css_selector('button.HoLwm').click()

    def page(self, name):
        post = []
        follower = []
        follow = []
        driver = self.driver
        url = "https://www.instagram.com{}".format(name)
        driver.get(url)
        following = WebDriverWait(driver, 10).until(Ec.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/<username>/following/"]')))
        following.click()
        time.sleep(5)
        for i in range(1, 3):
            auto_follow = driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div[2]/ul/div/li[{}]/div/div[3]/button'.format(i))
            time.sleep(5)
            auto_follow.click()
            time.sleep(5)
        driver.get(url)
        # html = driver.page_source
        # soup = BeautifulSoup(html)
        # flw = soup.select('span.g47SY')
        # post.append(flw[0].get_text())
        # follower.append(flw[1].get_text())
        # follow.append(flw[2].get_text())
        # # print(flw[1].get_text())
        # # print(post, follower, follow)
        # product = {'post': post, 'follower': follower, 'following': follow}
        # df = pd.DataFrame.from_dict(product)
        # print(df)

    def like(self, name):
        driver = self.driver
        like_url = "https://www.instagram.com{}".format(name)
        driver.get(like_url)
        time.sleep(5)
        WebDriverWait(driver, 10).until(Ec.element_to_be_clickable((By.CSS_SELECTOR, '#react-root > section > main > '
                                                                                     'div > div._2z6nI > article > '
                                                                                     'div:nth-child(1) > div > '
                                                                                     'div:nth-child(1) > '
                                                                                     'div:nth-child(1) > a'))).click()
        i = 1
        time.sleep(3)
        while i <= 5:
            time.sleep(5)
            if driver.find_elements_by_xpath('//*[contains(@aria-label,"Unlike")]'):
                time.sleep(5)
                driver.find_element_by_link_text('Next').click()
                time.sleep(5)
            elif driver.find_elements_by_xpath('//*[contains(@aria-label,"Like")]'):
                time.sleep(5)
                driver.find_element_by_css_selector('span.fr66n').click()
                time.sleep(5)
                driver.find_element_by_link_text('Next').click()
                i += 1
                time.sleep(5)
        driver.get(like_url)

    def comment(self, name):
        driver = self.driver
        like_url = "https://www.instagram.com{}".format(name)
        driver.get(like_url)
        time.sleep(5)
        WebDriverWait(driver, 10).until(
            Ec.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/p/CFcpeUKlJyt/"]'))).click()
        time.sleep(5)
        i = 1
        while i <= 3:
            cm = WebDriverWait(driver, 10).until(Ec.element_to_be_clickable((By.CLASS_NAME, 'Ypffh')))
            time.sleep(3)
            cm.click()
            cm = WebDriverWait(driver, 10).until(Ec.element_to_be_clickable((By.CLASS_NAME, 'Ypffh')))
            cm.send_keys('very nice' + Keys.ENTER)
            time.sleep(5)
            driver.find_element_by_link_text('Next').click()
            i += 1
            time.sleep(5)
        driver.get(like_url)


test = Bot()
test.log_in()
test.info()
test.notif()
test.page('/<username>/')
test.like('/<username>/')
test.comment('/<username>/')
