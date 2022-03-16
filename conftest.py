'''
Configuration file for scripts that are run via pytest.
'''

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


SUPPORTED_BROWSERS = ('chrome', 'firefox')


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='ru',
                     help='Choose language: ru, en, es...')


def browser_options(browser_name, user_language):
    if browser_name == 'chrome':
        chrome_options = Options()
        chrome_options.add_experimental_option('prefs',
                {'intl.accept_languages': user_language})
        driver = webdriver.Chrome(options=chrome_options)

    elif browser_name == 'firefox':
        firefox_options = webdriver.FirefoxProfile()
        firefox_options.set_preference(
                'intl.accept_languages', user_language)
        driver = webdriver.Firefox(firefox_profile=firefox_options)
    return driver


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')

    if browser_name in SUPPORTED_BROWSERS:
        driver = browser_options(browser_name, user_language)
    else:
        supported = ', '.join(SUPPORTED_BROWSERS)
        raise pytest.UsageError(f'Supported browsers: {supported}')

    yield driver
    driver.quit()
