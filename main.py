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
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        print("accept cookies")
        cookies_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]")
        cookies_button.click()
        time.sleep(5)
        print("find username area and enter username")
        username_area = self.driver.find_element(By.NAME, "username")
        username_area.send_keys(MY_USERNAME)
        time.sleep(5)
        print("find password area and enter password")
        password_area = self.driver.find_element(By.NAME, "password")
        password_area.send_keys(MY_PASSWORD)
        time.sleep(5)
        print("find 'se connecter' button and click on it")
        sign_in_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button")
        sign_in_button.click()
        time.sleep(5)
        print("decline to register to credentials")
        later_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button")
        later_button.click()
        time.sleep(5)
        print("decline the notifications")
        notif_later_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
        notif_later_button.click()


    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(5)
        print("open the list of followers")
        nb_followers = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div")
        nb_followers.click()
        time.sleep(3)
        print("scroll in the modal")
        modal = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")
        for n in range(3):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            print(n)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(3)

    def follow(self):
        time.sleep(3)
        print("get all_buttons follow")
        all_buttons_follow = self.driver.find_elements(By.CSS_SELECTOR, "button._acan _acap _acas _aj1-")
        print(len(all_buttons_follow))
        print("click on follow button")
        for button in all_buttons_follow[1:10]:
            time.sleep(3)
            print()
            button.click()


insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()
