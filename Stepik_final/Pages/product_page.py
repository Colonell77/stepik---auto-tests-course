from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.add_to_basket), 'Кнопка корзины отсутствует!!!!'
        self.browser.find_element(*ProductPageLocators.add_to_basket).click()

    def comparsion_names_product(self):
        name = self.browser.find_element(*ProductPageLocators.name_of_product).text
        name_in_message = self.browser.find_element(*ProductPageLocators.name_of_product_in_message).text
        assert name == name_in_message, 'Не совпадают названия продукта'

    def comparsion_cost_product(self):
        cost = self.browser.find_element(*ProductPageLocators.cost_of_product).text
        cost_in_basket = self.browser.find_element(*ProductPageLocators.cost_of_product_in_basket).text
        assert cost == cost_in_basket, 'Не совпадают цены'
