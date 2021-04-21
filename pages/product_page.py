from .locators import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):
    def put_product_in_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        self.chosen_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        self.product_price =  self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_button.click()
        self.solve_quiz_and_get_code() 
    
    def should_be_product_in_basket(self):
        product_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET).text
        assert product_in_basket == self.chosen_product, "Product does not match!"
            
    def should_be_price_in_basket(self):
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        assert price_in_basket == self.product_price, "Price does not match!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"
    
    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Element is not disappeared, but should be"


        

