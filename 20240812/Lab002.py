from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def test_open_vmologin():
    chrome_option = Options()
    chrome_option.add_argument("--headerless")
    chrome_option.page_load_strategy("--none")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    assert driver.current_url == "https://app.vwo.com/#/login"