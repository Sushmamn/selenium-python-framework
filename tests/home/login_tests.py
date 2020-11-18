from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest
import pytest
import time
from utilities.teststatus import TestStatus

@pytest.mark.usefixtures("onetimesetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        print("Running class setup")

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login("abc@gmail.com", "abcabc112**", usecase="valid_login")
        result1 = self.lp.verifyPageTitle(titleToVerify="Feed | LinkedIn")
        self.ts.mark(result1, "Title verification")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_valid_login", result2, "Valid Login")
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.login("abc@gmail.com", "abcabc112", usecase="invalid_login")
        time.sleep(5)
        result = self.lp.verifyLoginFailed()
        self.ts.markFinal("test_invalid_login", result, "Invalid Login verification")