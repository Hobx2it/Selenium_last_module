from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
import pytest
import time
import selenium

# urls = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

# bugged_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"

# @pytest.mark.parametrize('link', [i for i in urls if i != "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"]
#                                   + [pytest.param(bugged_link, marks=pytest.mark.xfail(reason='Исправлять не будут ' + bugged_link))])

@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    
  
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        link = 'http://selenium1py.pythonanywhere.com/'
        page = BasePage(self.browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(self.browser, self.browser.current_url)
        email = str(time.time()) + "@fakemail.org"
        password = "password" + str(time.time())
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()
        
    
    @pytest.mark.skip    
    def test_user_cant_see_success_message(self, browser):
        self.browser = browser
        '''Открываем страницу товара 
        Проверяем, что нет сообщения об успехе с помощью is_not_element_present'''
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(self.browser, link)
        page.open()
        page.should_be_product_page()
        page.should_not_be_success_message()
        time.sleep(1)
        
    #@pytest.mark.skip
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

        page = ProductPage(self.browser, link)
        page.open()
        page.should_be_product_page()
        page.product_to_basket()
        time.sleep(1)
        
@pytest.mark.need_review    
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.product_to_basket()
    time.sleep(1)    


    
@pytest.mark.xfail(reason="norm")
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    '''Открываем страницу товара 
    Добавляем товар в корзину 
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present'''
    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.product_to_basket()
    page.should_not_be_success_message()

@pytest.mark.skip
@pytest.mark.xfail(reason="norm")
def test_message_disappeared_after_adding_product_to_basket(browser): 
    '''Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_disappeared'''
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.product_to_basket()
    page.should_not_be_success_message_with_is_disappeared()
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
@pytest.mark.need_review    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):

    '''Гость открывает страницу товара
    Переходит в корзину по кнопке в шапке 
    Ожидаем, что в корзине нет товаров
    Ожидаем, что есть текст о том что корзина пуста'''
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.is_empty_basket()
    
    
    
    
    
    
  
