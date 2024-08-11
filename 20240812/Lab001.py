import time
import pytest
import allure
from selenium import webdriver

def test_open_url():

    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    time.sleep(5)
    assert driver.title == "Google"