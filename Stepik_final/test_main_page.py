from .Pages.main_page import MainPage
from .Pages.basket_page import BasketPage
from .Pages.locators import BasketPageLocators

# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                      # открываем страницу
#     page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина
#     page.should_be_login_link()
#     log_page = LoginPage(browser, browser.current_url)
#     log_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    assert page.is_element_present(*BasketPageLocators.BASKET_LINK), 'Ссылка на корзину отсутствует'
    page.open_basket(*BasketPageLocators.BASKET_LINK)
    page.basket_is_empty()
    page.basket_empty_message()
    # time.sleep(2000)
