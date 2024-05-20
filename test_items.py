from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_contain_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(5)  # import time
    assert WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket"))), "There is no 'Added to Cart' button"
    time.sleep(15)