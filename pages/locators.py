from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, ".register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRICE = (By.CSS_SELECTOR, ".price_color")
    PRODUCT_IN_BASKET = (By.XPATH, "/html/body/div/div/div/div/div/strong")
    PRICE_IN_BASKET = (By.XPATH, "/html/body/div/div/div/div/div/p/strong")
    SUCCESS_MESSAGE = (By.XPATH, "/html/body/div/div/div/div/div")

    
   
