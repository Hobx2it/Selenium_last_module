from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators
import time


class BasketPage(BasePage):
    
    def is_empty_basket(self):
        
        assert len(self.browser.find_elements(*BasketPageLocators.BASKET_CONTENT)) == 1, 'Корзина не пуста, есть товары'
    
    
    
    