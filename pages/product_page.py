from selenium.common.exceptions import NoSuchElementException
from .locators import ProductPageLocators
from .base_page import BasePage
import time

class ProductPage(BasePage):

    def put_product_in_basket(self):
        self.should_put_product_in_basket()
        self.should_be_product_in_basket()
        self.should_be_price_in_basket()

    def should_put_product_in_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        self.chosen_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        #print(self.chosen_product)
        self.product_price =  self.browser.find_element(*ProductPageLocators.PRICE).text
        #print(self.product_price)
        basket_button.click()

        #self.solve_quiz_and_get_code() 
    
    def should_be_product_in_basket(self):
        #time.sleep(30)
        try:
            product_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET).text
            #print(product_in_basket)
            assert product_in_basket == self.chosen_product, "Товар не совпадает!"
        except NoSuchElementException:
            print("Корзина пуста!")
    def should_be_price_in_basket(self):
        try:
            price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
            #print(price_in_basket)
            assert price_in_basket == self.product_price, "Цена не совпадает!"
        except NoSuchElementException:
            print("Корзина пуста!")

    def should_not_be_success_message(self):
        #print(self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text)
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"
    
    def should_be_disappeared(self):
        #print(self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text)
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Element is not disappeared, but should be"
        

