from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//div[@id='content_inner']/p[contains(text(), 'Your basket is empty')]")
    BASKET_FORMSET = (By.CSS_SELECTOR, "#basket_formset")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, ".register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.XPATH, "//form[@id ='register_form']/button")
    
class MainPageLocators():
    LOOK_BASKET_BUTTON = (By.PARTIAL_LINK_TEXT, "basket")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    PRODUCT_IN_BASKET = (By.XPATH, "/html/body/div/div/div/div/div/strong")
    PRICE_IN_BASKET = (By.XPATH, "/html/body/div/div/div/div/div/p/strong")
    SUCCESS_MESSAGE = (By.XPATH, "/html/body/div/div/div/div/div")






