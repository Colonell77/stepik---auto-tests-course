from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    WORD_IN_URL = '/login/'
    FORM_LOGIN_ID = (By.CSS_SELECTOR, '#login_form')
    FORM_REGISTER_ID = (By.CSS_SELECTOR, '#register_form')
    EMAIL_ADDRESS = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD1 = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')
    BUTTON_REGISTER = (By.CSS_SELECTOR, "button[name = 'registration_submit']")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form button')
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    NAME_OF_PRODUCT_IN_MESSAGE = (By.CSS_SELECTOR, '.alertinner strong')
    COST_OF_PRODUCT = (By.CSS_SELECTOR, 'p.price_color')
    COST_OF_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '.alert-info strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group a')
    CONTENT_IS_PRESENT = (By.CSS_SELECTOR, '.col-sm-4 a')
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner')
