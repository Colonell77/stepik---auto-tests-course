from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.CONTENT_IS_PRESENT), 'Товар присутствует в корзине'

    def basket_empty_message(self):
        message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        assert message.find('Your basket is empty') != -1, 'Надписи "Your basket is empty" нет'

