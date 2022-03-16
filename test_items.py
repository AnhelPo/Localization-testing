'''
Checks out if the button for adding item to the shopping cart
exists on page.
Uncomment lines for visual check.
'''

# import time

from selenium.webdriver.common.by import By


URL = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_basket_button(browser):
    browser.get(URL)
    add_to_cart = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')
    assert len(add_to_cart) > 0, \
               'Button for adding item to the shopping cart was not found!'
    # time.sleep(10)
