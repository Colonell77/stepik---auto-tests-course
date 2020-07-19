from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert login_url.find(LoginPageLocators.WORD_IN_URL) != -1,\
            f'login_URL не содержит {LoginPageLocators.WORD_IN_URL}'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN_ID), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.FORM_REGISTER_ID), "Register form is not presented"

    def register_new_user(self, email, password):
        assert self.is_element_present(*LoginPageLocators.EMAIL_ADDRESS), "Нет поля E-MAIL в форме регистрации"
        assert self.is_element_present(*LoginPageLocators.PASSWORD1), "Нет поля PASSWORD1 в форме регистрации"
        assert self.is_element_present(*LoginPageLocators.PASSWORD2), "Нет поля PASSWORD2 в форме регистрации"
        assert self.is_element_present(*LoginPageLocators.BUTTON_REGISTER), "Нет кнопки REGISTER в форме регистрации"
        self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER).click()
