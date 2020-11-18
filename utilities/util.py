import utilities.custom_logger as cl
import logging
from traceback import print_stack
import time

class Util:

    log = cl.customLogger(logging.INFO)

    def verifyTextContains(self, expectedText, actualText):
        try:
            self.log.info("Actual text from web UI :: "+actualText)
            self.log.info("Expected text from web UI :: "+expectedText)
            if expectedText.lower() in actualText.lower():
                self.log.info("### Verification Contains !!!!!")
                return True
            else:
                self.log.info("### Verification Contains Failed !!!!!")
                return False
        except:
            self.log.error("Exception occured in verifyTextContains() util")
            print_stack()
            return False

    def sleep(self, secs):
        try:
            self.log.info("Sleeping for "+secs+" secs")
            time.sleep(secs)
        except:
            self.log.error("Exception occured in sleep() util")
            print_stack()