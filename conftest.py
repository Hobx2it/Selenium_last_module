import pytest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options
import time



def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: english or russian (en|ru)")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        binary = FirefoxBinary(r'C:\Users\AmanovRA\AppData\Local\Mozilla Firefox\firefox.exe')
        exec_path = "geckodriver.exe"
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(executable_path=exec_path, firefox_binary=binary, firefox_profile=fp)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
        
    if user_language not in ('en', 'ru'):
        raise pytest.UsageError("--langi=uage should be english or russian")
        
    yield browser
    
    print("\nquit browser..")
    browser.quit()
    
    


