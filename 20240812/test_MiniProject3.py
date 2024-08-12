from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pytest
import allure
import allure_pytest

@allure.title("Mini Project# 3")
@allure.description("Verify that if user validity is expired and needs to upgrade")
def test_mini_project3():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.idrive360.com/enterprise/login")
    user_id = driver.find_element(By.ID,"username")
    user_id.send_keys("augtest_040823@idrive.com")

    pswd = driver.find_element(By.ID, "password")
    pswd.send_keys("123456")

    sign_in = driver.find_element(By.ID,"frm-btn")
    sign_in.click()
    time.sleep(20)

    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"
    allure.attach(driver.get_screenshot_as_png(),name='Screenshot')
    upgrade_now = driver.find_element(By.ID, "upgrade")
    upgrade_now.click()
    time.sleep(10)
    upgrade_noww = driver.find_element(By.CLASS_NAME,"id-card-title")
    assert upgrade_noww.is_displayed()
    allure.attach(driver.get_screenshot_as_png(), name='upgrade_Screenshot')
