import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
import time


def test_guest_can_go_to_login_page(self, browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)                       # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()
    page.go_to_login_page()                              # открываем страницу
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()                    # выполняем метод страницы — переходим на страницу логина
    
def test_guest_should_see_login_link(self, browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)                        
    page.open()
    page.go_to_basket()
    #time.sleep(10)
    page = BasketPage(browser, browser.current_url)
    page.should_be_empty_basket()






