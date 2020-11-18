import pytest
from selenium import webdriver
from base.webdriverFactory import WebDriverFactory

@pytest.yield_fixture
def setUp():
    print("Running setup before execution starts")
    yield
    print("Running tearDown after execution ends")\


@pytest.yield_fixture(scope= 'class')
def onetimesetUp(request, browser):
    print("Running one time module setup")
    wdf = WebDriverFactory(browser)
    driver = wdf.createWebdriverInstance()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running ome time module tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.yield_fixture(scope= 'session')
def browser(request):
    return request.config.getoption("--browser")

