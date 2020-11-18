from base.selenium_driver import SeleniumDriver


class TestStatus(SeleniumDriver):

    def __init__(self, driver):
        super(TestStatus, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultmessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### Verification Successful :: "+resultmessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.info("### Verification Failed :: " + resultmessage)
                    self.screenshot(resultmessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("### Verification Failed :: " + resultmessage)
                self.screenshot(resultmessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("### Exception Occured ")
            self.screenshot(resultmessage)

    def mark(self, result, resultmessage):
        self.setResult(result, resultmessage)

    def markFinal(self, testName, result, resultmessage):
        self.setResult(result, resultmessage)

        if "FAIL" in self.resultList:
            self.log.error(testName+" : ### TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName+" : ### TEST PASSED")
            self.resultList.clear()
            assert True == True