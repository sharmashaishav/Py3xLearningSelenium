from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def test_open_vmologin():
    chrome_option = Options()
    driver = webdriver.Chrome(options=chrome_option)
    chrome_option.add_argument("--headless")
    # chrome_option.page_load_strategy("page-load-strategy=none")
    # driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    assert driver.current_url == "https://app.vwo.com/#/login"