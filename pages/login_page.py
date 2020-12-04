from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.ENTER_EMAIL), "login_form email_field is not presented"
        assert self.is_element_present(*LoginPageLocators.ENTER_PASSWORD), "login_form password_field is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "registration_form email_field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), "registration_form password_field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_DUPLICATE), "registration_form password_reenter_field is not presented"