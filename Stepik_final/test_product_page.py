from .Pages.product_page import ProductPage
from .Pages.basket_page import BasketPage
from .Pages.locators import BasketPageLocators

import time
import pytest

# @pytest.mark.parametrize('links', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#                                                "?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page = BasketPage(browser, browser.current_url)
    assert page.is_element_present(*BasketPageLocators.BASKET_LINK), 'Ссылка на корзину отсутствует'
    page.open_basket(*BasketPageLocators.BASKET_LINK)
    page.basket_is_empty()
    page.basket_empty_message()


# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.should_not_be_success_message()
#     time.sleep(2000)
#
# def test_guest_cant_see_success_message(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()
#
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.message_disappeared_after_adding_product_to_basket()
#     # time.sleep(2000)

# def test_guest_can_add_product_to_basket(browser, links):
#     link = links
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.comparsion_names_product()   # перенесено для этой задачи
#     page.comparsion_cost_product()    # перенесено для этой задачи



# def test_comparsion_names_product(browser):
#     page = ProductPage(browser, browser.current_url)
#     page.comparsion_names_product()
#
# def test_comparsion_cost_product(browser):
#     page = ProductPage(browser, browser.current_url)
#     page.comparsion_cost_product()
#     time.sleep(2000)
