from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.readProperties import readConf


class WomenTitlePage:
    """BY LOCATORS OR OBJECT REPOSITORY"""
    TOPSSUBMENUITEMS_XPATH = "//div[@id='categories_block_left']//li[1]//span[1]"
    DRESSESSUBMENUITEMS_XPATH = "//div[@id='categories_block_left']//li[1]//span[2]"
    TSHIRTSSUBMENUTAB_XPATH = "//ul[@style='display: block;']/li/a[contains(text(), 'T-shirts')]"
    BLOUSESSUBMENUTAB_XPATH = "//ul[@style='display: block;']/li/a[contains(text(), 'Blouses')]"
    CASUALDRESSESSUBMENUTAB_XPATH = "//ul[@style='display: block;']/li/a[contains(text(), 'Casual')]"
    EVENINGDRESSESSUBMENUTAB_XPATH = "//ul[@style='display: block;']/li/a[contains(text(), 'Evening')]"
    SUMMERDRESSESSUBMENUTAB_XPATH = "//ul[@style='display: block;']/li/a[contains(text(), 'Summer')]"
    TOPSCATEGORYCHECKBOX_XPATH = "//input[@id='layered_category_4']"
    DRESSESCATEGORYCHECKBOX_XPATH = "//input[@id='layered_category_8']"
    SIZESMALLCHECKBOX_XPATH = "//input[@id='layered_id_attribute_group_1']"
    SIZEMEDIUMCHECKBOX_XPATH = "//input[@id='layered_id_attribute_group_2']"
    SIZELARGECHECKBOX_XPATH = "//input[@id='layered_id_attribute_group_3']"
    BEIGECOLOR_XPATH = "//ul[@class='col-lg-12 layered_filter_ul color-group']//a[contains(text(), 'Beige')]"
    WHITECOLOR_XPATH = "//ul[@class='col-lg-12 layered_filter_ul color-group']//a[contains(text(), 'White')]"
    BLACKCOLOR_XPATH = "//ul[@class='col-lg-12 layered_filter_ul color-group']//a[contains(text(), 'Black')]"
    ORANGECOLOR_XPATH = "//ul[@class='col-lg-12 layered_filter_ul color-group']//a[contains(text(), 'Orange')]"
    BLUECOLOR_XPATH = "//ul[@class='col-lg-12 layered_filter_ul color-group']//a[contains(text(), 'Blue')]"
    GREENCOLOR_XPATH = "//ul[@class='col-lg-12 layered_filter_ul color-group']//a[contains(text(), 'Green')]"
    YELLOWCOLOR_XPATH = "//ul[@class='col-lg-12 layered_filter_ul color-group']//a[contains(text(), 'Yellow')]"
    PINKCOLOR_XPATH = "//ul[@class='col-lg-12 layered_filter_ul color-group']//a[contains(text(), 'Pink')]"
    COTTONCHECKBOX_XPATH = "//input[@id='layered_id_feature_5']"
    POLYESTERCHECKBOX_LINKTEXT = "Polyester"
    VISCOSECHECKBOX_LINKTEXT = "Viscose"
    CASUALCEHCKBOX_LINKTEXT = "Casual"
    DRESSYCHECKBOX_LINKTEXT = "Dressy"
    GIRLYCHECKBOX_LINKTEXT = "Girly"
    COLORFULDRESSCEHCKBOX_LINKTEXT = "Colorful Dress"
    MAXIDRESSCHECKBOX_LINKTEXT = "Maxi Dress"
    MIDIDRESSCHECKBOX_LINKTEXT = "Midi Dress"
    SHORTDRESSCHECKBOX_LINKTEXT = "Short Dress"
    SHORTSLEEVECHECKBOX_LINKTEXT = "Short Sleeve"
    INSTOCKCHECKBOX_LINKTEXT = "In stock"
    FASHIONMANUFACTURERCHECKBOX_LINKTEXT = "Fashion Manufacturer"
    NEWCHECKBOX_LINKTEXT = "New"
    DELIVERYLINK_CSS = "a[title='Delivery']"
    LEGALNOTICELINK_CSS = "a[title='Legal Notice']"
    TERMSLINK_CSS = "div[class='block_content list-block'] a[title='Terms and conditions of use']"
    ABOUTUS_CSS = "div[class='block_content list-block'] a[title='About us']"
    SECUREPAYMENT_CSS = "a[title='Secure payment']"
    OURSTORES_CSS = "div[class='block_content list-block'] a[title='Our stores']"
    ALLSPECIALSLINK_CSS = "a[title='All specials'] span"
    DISCOVEROURSTORES_CSS = "a[title='All specials'] span"
    FIRSTITEMINVIEWEDPRODUCTSLIST_XPATH = "//div[@id='viewed-products_block_left']//li[@class='clearfix first_item']/a[@class='products-block-image']"
    LASTITEMINVIEWEDPRODUCTSLIST_XPATH = "//div[@id='viewed-products_block_left']//li[@class='clearfix last_item']/a[@class='products-block-image']"
    TOPSSUBCATEGORYLINK_XPATH = "//a[@class='subcategory-name'][normalize-space()='Tops']"
    DRESSESSUBCATEGORYLINK_XPATH = "//a[@class='subcategory-name'][normalize-space()='Dresses']"
    SORTBYLIST_ID = "selectProductSort"
    LISTVIEWICON_CLASSNAME = "icon-th-list"
    GRIDVIEWICON_CLASSNAME = "icon-th-large"
    PRODUCTNAMECOMMONLINK_XPATH = "//ul[@class='product_list row list']//a[contains(normalize-space(), '')]"
    ADDTOCARTCOMMONLINK_XPATH = "(//span[contains(text(),'Add to cart')])"
    MORECOMMONLINK_XPATH = "(//span[contains(text(),'More')])"
    WISHLISTCOMMONLINK_XPATH = "//p[contains(text(),'Faded')]/parent::div/parent::div/div[contains(@class, 'right-block')]//div[@class='wishlist']"
    ADDTOCOMPARECOMMONLINK_XPATH = "//p[contains(text(),'Faded')]/parent::div/parent::div/div[contains(@class, 'right-block')]//div[@class='compare']"
    TOPCOMPAREBUTTON_XPATH = "(//form[@class='compare-form'])[1]"
    BOTTOMCOMPAREBUTTON_XPATH = "(//form[@class='compare-form'])[2]"
    DISCOUNTPERCENTAGECOMMONELEMENT_XPATH = "//div[@class='content_price col-xs-5 col-md-12']//span[@class='price-percent-reduction'][contains(normalize-space(),'%')]"

    def __init__(self, driver):
        self.driver = driver

    def click_on_list_view(self):
        self.driver.find_element(By.CLASS_NAME, self.LISTVIEWICON_CLASSNAME).click()

    def click_on_specified_product(self, productDesc):
        self.driver.find_element(
            By.XPATH, "//p[contains(text(),'" + productDesc + "')]/parent::div/h5").click()

    def add_discounted_product_to_cart(self, discount):
        self.driver.find_element(
            By.XPATH,
            "//div[@class='content_price col-xs-5 col-md-12']//span[@class='price-percent-reduction'][contains(normalize-space(),'-" + discount + "%')]/parent::div/following-sibling::div[1]//span[contains(text(), 'Add to cart')]").click()

    def click_to_view_discount_product(self, discount):
        self.driver.find_element(
            By.XPATH,
            "//div[@class='content_price col-xs-5 col-md-12']//span[@class='price-percent-reduction'][contains(normalize-space(),'-" + discount + "%')]/parent::div/parent::div/parent::div/parent::div/child::div/h5").click()

    def click_to_add_product_in_wishlist_without_signin(self, productName):
        self.driver.find_element(By.XPATH,
                                 "//p[contains(text(),'" + productName + "')]/parent::div/parent::div/div[contains(@class, 'right-block')]//div[@class='wishlist']").click()
        list = self.driver.find_elements(By.XPATH, "//p[@class='fancybox-error']")
        assert len(list) != 0

    def click_to_add_product_in_compare_list(self, productName):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                 "//p[contains(text(),'"+productName+"')]/parent::div/parent::div/div[contains(@class, 'right-block')]//div[@class='compare']")))
        self.driver.find_element(By.XPATH,
                                 "//p[contains(text(),'"+productName+"')]/parent::div/parent::div/div[contains(@class, 'right-block')]//div[@class='compare']").click()

    def click_to_view_compare_list(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.TOPCOMPAREBUTTON_XPATH)))
        element = self.driver.find_elements(By.XPATH, self.TOPCOMPAREBUTTON_XPATH)
        if len(element) != 0:
            self.driver.find_element(By.XPATH, self.TOPCOMPAREBUTTON_XPATH).click()
            assert True
        else:
            assert False
