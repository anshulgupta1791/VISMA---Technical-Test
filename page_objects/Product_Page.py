from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.customLogger import Logger
from utilities.readProperties import readConf


class ProductPage:

    logs = Logger.generate_log()


    """BY LOCATORS OR OBJECT REPOSITORY"""
    INPUTPRODUCTQUANTITY_ID = "quantity_wanted"
    REDUCEPRODUCTQUANTITY_CLASSNAME = "icon-minus"
    INCREASEPRODUCTQUANTITY_CLASSNAME = "icon-plus"
    SIZEDROPDOWN_ID = "group_1"
    COLORCOMMONLINK_XPATH = "//ul[@id='color_to_pick_list']/li/a[contains(@title, '')]"
    ADDTOCARTBUTTON_CSS = "button[name='Submit'] span"
    PRODUCTADDEDTOCARTMESSAGE_XPATH = "//h2[normalize-space()='Product successfully added to your shopping cart']"
    CONTINUESHOPPINGBUTTONINPOPUP_XPATH = "//span[@title='Continue shopping']//span[1]"
    PROCEEDTOCHECKOUTBUTTONINPOPUP_XPATH = "//span[normalize-space()='Proceed to checkout']"
    CLOSEMESSAGEAFTERADDINGTOCART_CLASSNAME = "cross"
    ADDINGTOWISHLISTERROR_CLASSNAME = "fancybox-error"
    ADDINGTOWISHLISTSUCCESS_XPATH = "//p[@class='fancybox-error'][text()='Added to your wishlist.']"
    LARGEVIEWBUTTON_CLASSNAME = "span_link no-print"
    LARGEVIEWPOPUP_CLASSNAME = "fancybox-skin"
    BACKTOWOMENPAGE_XPATH = "(//a[@title='Women'][normalize-space()='Women'])[2]"
    BACKTOHOMEPAGE_CLASSNAME = "icon-home"
    CLOSEPOPUPONPRODUCTPAGE_CLASSNAME = "fancybox-item fancybox-close"
    PRODUCTPRICE_ID = "our_price_display"
    TOTALPRODUCTPRICE_CLASSNAME = "ajax_block_products_total"
    COLORINSUCCESSPOPUP_ID = "layer_cart_product_attributes"
    SIZEINSUCCESSPOPUP_ID = "layer_cart_product_attributes"
    PRODUCTQUANTITYINSUCCESSPOPUP_ID = "layer_cart_product_quantity"
    PRODUCTCOMMONSKULINK_XPATH = "//span[normalize-space()='']"


    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def select_by_value(by_locator, value):
        select = Select(by_locator)
        return select.select_by_value(value)

    @staticmethod
    def select_by_visible_text(by_locator, value):
        select = Select(by_locator)
        return select.select_by_visible_text(value)

    @staticmethod
    def select_by_index(by_locator, index):
        select = Select(by_locator)
        return select.select_by_index(index)

    def enter_product_quantity(self, quantity):
        self.driver.find_element(By.ID, self.INPUTPRODUCTQUANTITY_ID).clear()
        self.driver.find_element(By.ID, self.INPUTPRODUCTQUANTITY_ID).send_keys(quantity)

    def reduce_product_quanity(self):
        self.driver.find_element(By.CLASS_NAME, self.REDUCEPRODUCTQUANTITY_CLASSNAME).click()

    def increase_product_quantity(self):
        self.driver.find_element(By.CLASS_NAME, self.INCREASEPRODUCTQUANTITY_CLASSNAME).click()

    def select_size(self, size):
        sizeField = self.driver.find_element(By.ID, self.SIZEDROPDOWN_ID)
        self.select_by_visible_text(sizeField, size)

    def select_color(self, color):
        element = self.driver.find_elements(
            By.XPATH, "//ul[@id='color_to_pick_list']/li/a[contains(@title, '"+color+"')]")
        if len(element) != 0:
            self.driver.find_element(
                By.XPATH, "//ul[@id='color_to_pick_list']/li/a[contains(@title, '" + color + "')]").click()
        else:
            self.logs.info("****** Color Not Available for selected product ******")

    def add_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, self.ADDTOCARTBUTTON_CSS).click()

    def verify_product_added_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.PRODUCTADDEDTOCARTMESSAGE_XPATH)))
        successMessage = self.driver.find_elements(By.XPATH, self.PRODUCTADDEDTOCARTMESSAGE_XPATH)
        assert len(successMessage) != 0

    def click_on_continue_shopping_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.CONTINUESHOPPINGBUTTONINPOPUP_XPATH))).click()
        #self.driver.find_element(By.XPATH, self.CONTINUESHOPPINGBUTTONINPOPUP_XPATH).click()

    def click_on_proceed_to_checkout_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.PROCEEDTOCHECKOUTBUTTONINPOPUP_XPATH))).click()
        #self.driver.find_element(By.XPATH, self.PROCEEDTOCHECKOUTBUTTONINPOPUP_XPATH).click()

    def confirm_selected_size_product_is_added_to_cart(self, actualValue):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, self.SIZEINSUCCESSPOPUP_ID)))
        size = self.driver.find_element(By.ID, self.SIZEINSUCCESSPOPUP_ID)
        sizeText = size.text
        assert actualValue in sizeText

    def confirm_selected_color_product_is_added_to_cart(self, actualValue):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, self.COLORINSUCCESSPOPUP_ID)))
        color = self.driver.find_element(By.ID, self.COLORINSUCCESSPOPUP_ID)
        colorText = color.text
        assert actualValue in colorText

    def get_product_price_for_one(self):
        element = self.driver.find_element(By.ID, self.PRODUCTPRICE_ID)
        elementText = element.text
        priceForOne = elementText[1:]
        return float(priceForOne)

    def check_displayed_price_of_product(self, value):
        priceElement = self.driver.find_element(By.ID, self.PRODUCTPRICE_ID)
        price = priceElement.text
        productPrice = price[1:]
        assert float(productPrice) == value

    def verify_product_quantity_added_in_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.PRODUCTQUANTITYINSUCCESSPOPUP_ID)))
        element = self.driver.find_element(By.ID, self.PRODUCTQUANTITYINSUCCESSPOPUP_ID)
        product = element.text
        return float(product)

    def get_total_price_after_adding_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.TOTALPRODUCTPRICE_CLASSNAME)))
        element = self.driver.find_element(By.CLASS_NAME, self.TOTALPRODUCTPRICE_CLASSNAME)
        elementText = element.text
        totalPrice = elementText[1:]
        return float(totalPrice)

    def quick_view_a_product(self, productDesc):
        productElement = self.driver.find_element(
            By.XPATH, "//p[contains(text(),'"+productDesc+"')]/parent::div/parent::div/div[@class='left-block col-xs-4 col-xs-5 col-md-4']")
        quickViewElement = self.driver.find_element(
            By.XPATH, "(//a[@class='quick-view'])[1]")
        actions = ActionChains(self.driver)
        actions.move_to_element(productElement).move_to_element(quickViewElement).click().perform()

    def verify_quick_view_popup_open(self):
        """self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//iframe[@class='fancybox-iframe']"))
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Add to cart']").click()"""
        list = self.driver.find_elements(By.XPATH, "//iframe[@class='fancybox-iframe']")
        assert len(list) != 0

    def verify_product_page_opened(self, productSKU):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='"+productSKU+"']")))
        element = self.driver.find_element(By.XPATH, "//span[normalize-space()='"+productSKU+"']")
        productsku = element.text
        return productsku






