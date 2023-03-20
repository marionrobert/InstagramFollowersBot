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

    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass


insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()


# driver.get("https://www.instagram.com/")