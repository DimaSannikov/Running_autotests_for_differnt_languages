import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: 'chrome' or 'firefox'")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: 'en' or 'es' or 'fr'")
    

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_argument(f"--lang={user_language}")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = FFOptions()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox OR"
                                " --language should be 'en' or 'es' or 'fr'")
    yield browser
    print("\nquit browser..")
    browser.quit()