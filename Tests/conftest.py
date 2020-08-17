from selenium import webdriver
import pytest


@pytest.fixture(scope="class")
def setup(request):
    chromeDriver = "/Users/adityabhoyar/PycharmProjects/QATest_AdityaBhoyar/Driver/chromedriver"
    driver = webdriver.Chrome(chromeDriver)
    driver.get("https://yoda.shopsocially.com/store/zinreloteststore1/index")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
