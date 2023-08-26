#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime


class MessageAutomator:
    """ Automates sending a message to a user on Instagram """

    def __init__(self, username, password):
        """ Initializes the MessageAutomator class """

        self.username = username
        self.password = password

        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        self.__driver = webdriver.Chrome(options=chrome_options)
        self.__driver.implicitly_wait(20)
        self.__driver.maximize_window()

    def login(self):
        """ Logs into Instagram """

        self.__driver.get("https://www.instagram.com/accounts/login/")
        print("Logging in...")
        self.__driver.find_element(By.NAME, "username").send_keys(self.username)
        self.__driver.find_element(By.NAME, "password").send_keys(self.password)
        self.__driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

        try:
            self.__driver.find_element(By.CSS_SELECTOR, "button[type=button]").click()
        except Exception:
            pass

        try:
            self.__driver.find_element(By.CSS_SELECTOR, "._a9_1").click()
        except Exception:
            pass

    def send_message(self, user, message):
        """ Sends a message to a user """

        self.__driver.get(f"https://www.instagram.com/{user}/")
        print("Sending message to {}...".format(user))

        try:
            xpath_expr = "//div[@role='button' and text()='Message']"
            self.__driver.find_element(By.XPATH, xpath_expr).click()
        except Exception:
            print("Message button not found. You are probably not following this user.")
            return

        try:
            self.__driver.find_element(By.CSS_SELECTOR, "._a9_1").click()
        except Exception:
            pass
        
        message_box = self.__driver.find_element(By.XPATH, "//div[@contenteditable='true']")
        message_box.send_keys(message)
        message_box.send_keys(Keys.RETURN)
        print("Message sent to {} at {}".format(user, datetime.now().strftime("%H:%M:%S")))