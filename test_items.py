'''
Checks out if the button for adding item to the shopping cart
exists on page.
Uncomment lines for visual check.
'''

# import time

from selenium.webdriver.common.by import By


URL = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_basket_button_exists(browser):
    browser.get(URL)
    # time.sleep(10)
    assert browser.find_element(By.CLASS_NAME, 'btn-add-to-basket'), \
               'Button for adding item to the shopping cart was not found!'
