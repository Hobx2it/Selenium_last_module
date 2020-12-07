import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self                       
    def test_guest_can_go_to_login_page(self, browser):     
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)


    def test_guest_should_see_login_link(self, browser):
        '''Гость открывает главную страницу 
        Переходит в корзину по кнопке в шапке сайта
        Ожидаем, что в корзине нет товаров
        Ожидаем, что есть текст о том что корзина пуста'''
        link = "http://selenium1py.pythonanywhere.com"
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_link()
        
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        '''Гость открывает главную страницу 
        Переходит в корзину по кнопке в шапке сайта
        Ожидаем, что в корзине нет товаров
        Ожидаем, что есть текст о том что корзина пуста'''

        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page = BasketPage(browser, browser.current_url)
        page.is_empty_basket()        
 

  
