from base.selenium_driver import SeleniumDriver
from utilities.util import Util
from traceback import print_stack

class BasePage(SeleniumDriver):

    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, titleToVerify):
        try:
            self.util.sleep(5)
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(titleToVerify, actualTitle)
        except:
            self.log.error("Exception occured in verifyPageTitle() ")
            print_stack()
            return False