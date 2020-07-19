from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), 'Кнопка корзины отсутствует!!!!'
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def comparsion_names_product(self):
        name = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        name_in_message = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_IN_MESSAGE).text
        assert name == name_in_message, 'Не совпадают названия продукта'

    def comparsion_cost_product(self):
        cost = self.browser.find_element(*ProductPageLocators.COST_OF_PRODUCT).text
        cost_in_basket = self.browser.find_element(*ProductPageLocators.COST_OF_PRODUCT_IN_BASKET).text
        assert cost == cost_in_basket, 'Не совпадают цены'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'SUCCESS MESSAGE  появился'

    def message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'SUCCESS MESSAGE  появился'
