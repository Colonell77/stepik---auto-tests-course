from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    word_in_url = '/login/'
    form_login_id = (By.CSS_SELECTOR,'#login_form')
    form_register_id = (By.CSS_SELECTOR,'#register_form')
