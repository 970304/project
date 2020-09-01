import pytest
from selenium import webdriver
from pageObject.loginpage import LoginPage
from testdata import web_datas
from pageObject.investpage import InvestPage
import time

driver = None
@pytest.fixture(scope="class")
def open_web():
    global driver
    driver = webdriver.Chrome()
    driver.get(web_datas.web_url)
    lg = LoginPage(driver)
    yield driver, lg
    driver.quit()

@pytest.fixture()
def refresh():
    global driver
    yield
    time.sleep(0.5)
    driver.refresh()

@pytest.fixture(scope="class")
def user_login():
    global driver
    driver = webdriver.Chrome()
    driver.get(web_datas.web_url)
    LoginPage(driver).login(web_datas.username, web_datas.pwd)
    invest = InvestPage(driver)
    invest.home_page()
    yield driver, invest
    driver.quit()





