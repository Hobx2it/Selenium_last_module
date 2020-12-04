from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    ENTER_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    ENTER_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_DUPLICATE = (By.CSS_SELECTOR, "#id_registration-password2")
    