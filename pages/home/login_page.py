from selenium.webdriver.common.by import By
from base.basepage import BasePage
import utilities.custom_logger as cl
import logging

class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _login_link = "//a[text()='Sign in']"
    _email_field = "username"
    _password_field = "password"
    _login_button = "//button[text()='Sign in']"

    # Getting elements
    # def get_loginLink(self):
    #     return self.driver.find_element(By.XPATH, self._login_link)
    #
    # def get_emailField(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def get_passwordField(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def get_loginButton(self):
    #     return self.driver.find_element(By.XPATH, self._login_button)

    # Actions that can be performed on the elements
    def click_loginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enter_email(self, username):
        self.sendKeys(username, self._email_field)

    def enter_password(self, password):
        self.sendKeys(password, self._password_field)

    def click_loginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, username, password, usecase):
        if usecase == "invalid_login":
            self.click_loginLink()
        self.enter_email(username)
        self.enter_password(password)
        self.click_loginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//a[contains(@href, '/in/sushma-m-n-46702230/')]", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(), 'right password')]",
                                       locatorType="xpath")
        return result

