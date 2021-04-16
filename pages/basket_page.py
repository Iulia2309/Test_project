from .base_page import BasePage
from .locators import BasketPageLocators
#from selenium.common.exceptions import NoSuchElementException

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.shold_not_be_products_in_basket()
        self.shold_be_empty_basket_text()
        
    def shold_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET), \
           "Basket is not empty, but should be"

    def shold_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), \
               "Text is not present, but should be"
   
