from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
import time
import os


MY_EMAIL = os.environ["EMAIL"]
MY_USERNAME = os.environ["USERNAME"]
MY_PASSWORD =  os.environ["PASSWORD"]
SIMILAR_ACCOUNT = "chefsteps"

chrome_driver_path = os.environ["CHROME_DRIVER_PATH"]
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=service, options=options)
        self.followers = []

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        print("accept cookies")
        cookies_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]")
        cookies_button.click()
        time.sleep(5)
        print("find username area and enter username")
        username_area = self.driver.find_element(By.NAME, "username")
        username_area.send_keys(MY_USERNAME)
        print("find password area and enter password")
        time.sleep(5)
        password_area = self.driver.find_element(By.NAME, "password")
        password_area.send_keys(MY_PASSWORD)
        print("find 'se connecter' button and click on it")
        time.sleep(5)
        sign_in_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button")
        sign_in_button.click()


    def find_followers(self):
    pass


    def follow(self):
        pass


insta_bot = InstaFollower()
insta_bot.login()
# insta_bot.find_followers()
# insta_bot.follow()