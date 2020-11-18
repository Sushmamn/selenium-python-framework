from selenium import webdriver
import os

class WebDriverFactory():


    def __init__(self, browser):
        self.browser = browser

    def createWebdriverInstance(self):
        base_url = "https://www.linkedin.com/home"
        if self.browser == "ie":
            driver = webdriver.Ie()
        elif self.browser == "chrome":
            chromedriver = "/Users/vasanth/Desktop/Python/selenium_python/drivers/chromedriver"
            os.environ["webdriver.chrome.driver"] = chromedriver
            driver = webdriver.Chrome(chromedriver)
        else:
            driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(base_url)

        return driver