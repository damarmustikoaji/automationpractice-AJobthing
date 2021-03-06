from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options

def DriverBrowser(BROWSER):
    if BROWSER == "HEADLESS":
        options = Options()
        options.add_argument('--headless')
        try:
            driver = webdriver.Chrome(chrome_options=options)
            driver.set_window_size(1280, 800)
        except Exception as e:
            driver = webdriver.Chrome(executable_path='../driver/chromedriver', chrome_options=options)
            driver.set_window_size(1280, 800)
    elif BROWSER == "Firefox":
        try:
            driver = webdriver.Firefox(executable_path="../driver/geckodriver")
            driver.set_window_size(1280, 800)
        except Exception as e:
            raise
    elif BROWSER == "VM":
        try:
            display = Display(visible=0, size=(1280, 768))
            display.start()
            driver = webdriver.Chrome()
        except Exception as e:
            raise
    else:
        driver = webdriver.Chrome(executable_path='../driver/chromedriver')
        driver.set_window_size(1280, 800)
    return driver

def CloseBrowser(driver):
    return driver
