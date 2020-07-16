from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    word_in_url = '/login/'
    form_login_id = (By.CSS_SELECTOR,'#login_form')
    form_register_id = (By.CSS_SELECTOR,'#register_form')

class ProductPageLocators():
    add_to_basket = (By.CSS_SELECTOR, '#add_to_basket_form button')
    name_of_product = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    name_of_product_in_message = (By.CSS_SELECTOR, '.alertinner strong')
    cost_of_product = (By.CSS_SELECTOR, 'p.price_color')
    cost_of_product_in_basket = (By.CSS_SELECTOR, '.alert-info strong')



