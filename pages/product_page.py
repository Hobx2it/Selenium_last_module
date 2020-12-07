from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    
    def should_be_product_page(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "add_to_basket button is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "no product price element"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "no product name element"
    
    def product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()
        self.solve_quiz_and_get_code()
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == product_name_in_basket, 'Названия не совпали'
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text in self.browser.find_element(*ProductPageLocators.SUM_IN_BASKET).text, 'Цены товара и в корзине не совпали'
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
        
    def should_not_be_success_message_with_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, but should be"


        
        
        
        
        
    
