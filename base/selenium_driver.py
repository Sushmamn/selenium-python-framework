from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os


class SeleniumDriver:

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "linktext":
            return By.LINK_TEXT
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "css":
            return By.CSS_SELECTOR
        else:
            self.log.info("locator type: "+locatorType+" is incorrect or not supported")
            return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: "+locator+" and locator type: "+locatorType)
        except:
            self.log.info("Element not found with locator: "+locator+" and locator type: "+locatorType)
        return element

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element Found with locator: "+locator+" and locator type: "+locatorType)
                return True
            else:
                self.log.info("Element is not Found with locator: "+locator+" and locator type: "+locatorType)
                return False
        except:
                self.log.info("Element is not Found with locator: "+locator+" and locator type: "+locatorType)
                return False

    def elementPresenceCheck(self, locator, locatorType="id"):
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found with locator: "+locator+" and locator type: "+locatorType)
                return True
            else:
                self.log.info("Element is not Found with locator: "+locator+" and locator type: "+locatorType)
                return False
        except:
                self.log.info("Element is not Found with locator: " + locator + " and locator type: " + locatorType)
                return False

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on the element with locator: "+locator+" and locator type: "+locatorType)
        except:
            self.log.info("Cannot click on the element with locator: "+locator+" and locator type: "+locatorType)
            print_stack()

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.clear()
            element.send_keys(data)
            self.log.info("sent keys to the element with locator: "+locator+" and locator type: "+locatorType)
        except:
            self.log.info("Could not send keys to the element with locator: "+locator+
                  " and locator type "+locatorType)
            print_stack()

    def screenshot(self, resultMessage):
        filename = resultMessage+"-"+str(round(time.time())*1000)+".png"
        screenshotDir = "/screenshots/"
        relativeFilename = screenshotDir + filename
        currentDir = os.path.dirname(__file__)
        destinationDir = os.path.join(currentDir, screenshotDir)
        destinationFile = os.path.join(currentDir, relativeFilename)
        self.log.info("Current directory: "+currentDir)
        self.log.info("Screenshot file path: "+destinationFile)

        try:
            if not os.path.exists(destinationDir):
                self.log.info("Screenshot file dir: " + destinationDir)
                os.makedirs(destinationDir)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot saved to directory "+ destinationDir+ "-"+ resultMessage)
        except:
            self.log.error(" Exception Occured in screenshot ")
            print_stack()
