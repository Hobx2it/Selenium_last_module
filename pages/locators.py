from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    ENTER_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    ENTER_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_DUPLICATE = (By.CSS_SELECTOR, "#id_registration-password2")
    
class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")  
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, ".alert-success:first-child strong")
    SUM_IN_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner p:first-child")
    
    
    
