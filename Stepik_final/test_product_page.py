from .Pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()


def test_comparsion_names_product(browser):
    page = ProductPage(browser, browser.current_url)
    page.comparsion_names_product()

def test_comparsion_cost_product(browser):
    page = ProductPage(browser, browser.current_url)
    page.comparsion_cost_product()
