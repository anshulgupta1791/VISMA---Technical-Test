from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities import excelUtils


class HomePage:

    newUserForNewsLetterSubscription = ".//Test_Data/NewUserForNewsLetterSubscription.xlsx"

    """BY LOCATORS OR OBJECT REPOSITORY"""
    PHONENUMBER_CLASSNAME = "shop-phone"
    LOGO_XPATH = "//img[@alt='My Store']"
    WOMENTAB_XPATH = "//a[@title='Women']"
    DRESSESTAB_XPATH = "//body/div[@id='page']/div[@class='header-container']/header[@id='header']/div/div[@class='container']/div[@class='row']/div[@id='block_top_menu']/ul[@class='sf-menu clearfix menu-content sf-js-enabled sf-arrows']/li[2]/a[1]"
    TSHIRTSTAB_XPATH = "(//a[@title='T-shirts'][normalize-space()='T-shirts'])[2]"
    POPULARTAB_XPATH = "//a[normalize-space()='Popular']"
    ITEMSINPOPULARTAB_XPATH = "//ul[@id='homefeatured']//a[@class='product-name']"
    BESTSELLERSTAB_XPATH = "//a[normalize-space()='Best Sellers']"
    ITEMSINBESTSELLERSTAB_XPATH = "//ul[@id='blockbestsellers']//a[@class='product-name']"
    CENTERSECTION_ID = "center_column"
    SLIDERS_ID = "slider_row"
    SLIDERNEXT_LINKTEXT = "Next"
    EMAILFORNEWSLETTER_ID = "newsletter-input"
    SUBMITNEWSLETTER_NAME = "submitNewsletter"
    NEWSLETTERSUBCRIPTIONSUCCESSMESSAGE_XPATH = "//p[contains(text(),'Newsletter : You have successfully subscribed to t')]"
    NEWSLETTERSUBCRIPTIONERRORMESSAGE_XPATH = "//p[contains(text(),'Newsletter : This email address is already registe')]"
    FOOTER_XPATH = "//body/div[@id='page']/div/footer[@id='footer']/div[1]"
    CATEGORIES_XPATH = "//h4[normalize-space()='Categories']"
    SPECIALS_CSS = "a[title='Specials']"
    NEWPRODUCTS_CSS = "a[title='New products']"
    BESTSELLERSFOOTER_CSS = "a[title='Best sellers']"
    OURSTORES_CSS = "a[title='Our stores']"
    CONTACTUSFOOTER_CSS = "a[title='Contact us']"
    TERMSANDCONDITION_CSS = "a[title='Terms and conditions of use']"
    ABOUTUS_CSS = "a[title='About us']"
    SITEMAP_CSS = "a[title='Sitemap']"
    MYORDERS_LINKTEXT = "My orders"
    MYCREDITSLIPS_LINKTEXT = "My credit slips"
    MYADDRESSES_LINKTEXT = "My addresses"
    MYPERSONALINFO_LINKTEXT = "My personal info"
    SEARCHBOX_ID = "search_query_top"
    SEARCHSUBMIT_NAME = "submit_search"
    VIEWMYCART_XPATH = "//a[@title='View my shopping cart']"
    CONTACTUSHEADER_LINKTEXT = "Contact us"
    SIGNIN_PARTIAL = "Sign"
    TOPHEADER_XPATH = "//body/div[@id='page']/div/header[@id='header']/div/div/div/a/img[1]"
    CENTERBANNERS_XPATH = "//div[@id='htmlcontent_home']//ul/li"
    TOPSUNDERWOMENTTAB_XPATH = "//a[@title='Tops']"
    DRESSESUNDERWOMENTAB_XPATH = "(//a[@title='Dresses'][normalize-space()='Dresses'])[1]"
    TSHIRTSTABUNDERWOMENTAB_XPATH = "//li[@class='sfHover']//a[@title='T-shirts'][normalize-space()='T-shirts']"
    BLOUSESTABUNDERWOMENTAB_XPATH = "//a[@title='Blouses']"
    CASUALDRESSESUNDERWOMENTAB_XPATH = "//li[@class='sfHover']//a[@title='Casual Dresses'][normalize-space()='Casual Dresses']"
    EVENINGDRESSUNDERWOMENTAB_XPATH = "//li[@class='sfHover']//a[@title='Evening Dresses'][normalize-space()='Evening Dresses']"
    SUMMERDRESSUNDERWOMENTAB_XPATH = "//li[@class='sfHover']//a[@title='Summer Dresses'][normalize-space()='Summer Dresses']"
    CASUALDRESSUNDERDRESSESTAB_XPATH = "//li[@class='sfHover']//a[@title='Casual Dresses'][normalize-space()='Casual Dresses']"
    EVENVINGDRESSUNDERDRESSESTAB_XPATH = "//li[@class='sfHover']//a[@title='Evening Dresses'][normalize-space()='Evening Dresses']"
    SUMMERDRESSUNDERDRESSESTAB_XPATH = "//li[@class='sfHover']//a[@title='Summer Dresses'][normalize-space()='Summer Dresses']"
    QUICKVIEWBUTOON_XPATH = "(//span[contains(text(),'Quick view')])[1]"
    PRODUCTSLISTUNDERPOPULAR_XPATH = "//ul[@id='homefeatured']//div[@class='right-block']//h5//a"

    def __init__(self, driver):
        self.driver = driver

    def click_on_women_tab(self):
        self.driver.find_element(By.XPATH, self.WOMENTAB_XPATH).click()

    def click_on_dresses_tab(self):
        self.driver.find_element(By.XPATH, self.DRESSESTAB_XPATH).click()

    def click_on_tshirts_tab(self):
        self.driver.find_element(By.XPATH, self.TSHIRTSTAB_XPATH).click()

    def click_on_popular_tab(self):
        self.driver.find_element(By.XPATH, self.POPULARTAB_XPATH).click()

    def click_on_tops_under_women_tab(self):
        womenTabElement = self.driver.find_element(By.XPATH, self.WOMENTAB_XPATH)
        topsTabElement = self.driver.find_element(By.XPATH, self.TOPSUNDERWOMENTTAB_XPATH)
        actions = ActionChains(self.driver)
        actions.move_to_element(womenTabElement).move_to_element(topsTabElement).click().perform()

    def click_on_dresses_under_women_tab(self):
        womenTabElement = self.driver.find_element(By.XPATH, self.WOMENTAB_XPATH)
        dressesElement = self.driver.find_element(By.XPATH, self.DRESSESUNDERWOMENTAB_XPATH)
        actions = ActionChains(self.driver)
        actions.move_to_element(womenTabElement).move_to_element(dressesElement).click().perform()

    def click_on_specials_link(self):
        self.driver.find_element(By.CSS_SELECTOR, self.SPECIALS_CSS).click()

    def click_on_new_products_link(self):
        self.driver.find_element(By.CSS_SELECTOR, self.NEWPRODUCTS_CSS).click()

    def click_on_bestsellers_footer(self):
        self.driver.find_element(By.CSS_SELECTOR, self.BESTSELLERSFOOTER_CSS).click()

    def click_on_view_cart(self):
        self.driver.find_element(By.XPATH, self.VIEWMYCART_XPATH).click()

    def search_a_product(self, product):
        self.driver.find_element(By.ID, self.SEARCHBOX_ID).send_keys(product)
        self.driver.find_element(By.NAME, self.SEARCHSUBMIT_NAME).click()

    def click_on_contact_us_header(self):
        self.driver.find_element(By.LINK_TEXT, self.CONTACTUSHEADER_LINKTEXT).click()

    def return_to_homepage(self):
        self.driver.find_element(By.XPATH, self.LOGO_XPATH).click()

    def select_specific_product_from_popular(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.POPULARTAB_XPATH)))
        self.driver.find_element(By.XPATH, self.POPULARTAB_XPATH).click()
        productElement = self.driver.find_element(
            By.XPATH, "//ul[@id='homefeatured']//a[contains(text(), 'Faded')]")
        productElement.click()

    def select_specific_product_from_best_sellers(self):
        self.driver.find_element(By.XPATH, self.BESTSELLERSTAB_XPATH).click()
        productElement = self.driver.find_element(
            By.XPATH, "//ul[@id='blockbestsellers']//a[contains(text(), 'Chiffon')]")
        productElement.click()


    def subscribe_to_news_letter_with_new_user(self):
        self.rows = excelUtils.get_row_count(self.newUserForNewsLetterSubscription, 'Sheet1')
        list_status = []
        for r in range(2, self.rows + 1):
            self.useremail = excelUtils.read_data(self.newUserForNewsLetterSubscription, 'Sheet1', r, 1)
            self.expResult = excelUtils.read_data(self.newUserForNewsLetterSubscription, 'Sheet1', r, 2)
            self.driver.find_element(By.ID, self.EMAILFORNEWSLETTER_ID).clear()
            self.driver.find_element(By.ID, self.EMAILFORNEWSLETTER_ID).send_keys(self.useremail)
            self.driver.find_element(By.NAME, self.SUBMITNEWSLETTER_NAME).click()
            ele = self.driver.find_elements(By.XPATH, self.NEWSLETTERSUBCRIPTIONERRORMESSAGE_XPATH)
            if len(ele) != 0:
                if self.expResult == 'Pass':
                    list_status.append('Fail')
            else:
                list_status.append('Pass')
        assert 'Fail' not in list_status

    def click_on_signin_link(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.SIGNIN_PARTIAL).click()

    def add_popular_product_to_cart_from_home(self, productDesc):
        product = self.driver.find_element(By.XPATH, "//ul[@id='homefeatured']//div[@class='right-block']//a[contains(text(), '"+productDesc+"')]")
        quickViewElement = self.driver.find_element(
            By.XPATH, "(//a[@class='quick-view'])[1]")
        action = ActionChains(self.driver)
        action.move_to_element(product).move_to_element(quickViewElement).click().perform()
        list = self.driver.find_elements(By.XPATH, "//iframe[contains(@id, 'fancybox-frame')]")
        if len(list) != 0:
            self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'fancybox-frame')]"))
            self.driver.find_element(By.XPATH, "//span[normalize-space()='Add to cart']").click()
        else:
            assert False

    def add_popular_product_to_wishlist_from_home_without_loggingIn(self, productDesc):
        product = self.driver.find_element(By.XPATH, "//ul[@id='homefeatured']//div[@class='right-block']//a[contains(text(), '"+productDesc+"')]")
        quickViewElement = self.driver.find_element(
            By.XPATH, "(//a[@class='quick-view'])[1]")
        action = ActionChains(self.driver)
        action.move_to_element(product).move_to_element(quickViewElement).click().perform()
        list = self.driver.find_elements(By.XPATH, "//iframe[contains(@id, 'fancybox-frame')]")
        if len(list) != 0:
            self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'fancybox-frame')]"))
            self.driver.find_element(By.XPATH, "//a[@id='wishlist_button']").click()
            list1 = self.driver.find_elements(By.XPATH, "//p[@class='fancybox-error']")
            assert len(list1) != 0
        else:
            assert False

    def add_popular_product_to_wishlist_from_home_after_loggingIn(self, productDesc):
        product = self.driver.find_element(By.XPATH, "//ul[@id='homefeatured']//div[@class='right-block']//a[contains(text(), '"+productDesc+"')]")
        quickViewElement = self.driver.find_element(
            By.XPATH, "(//a[@class='quick-view'])[1]")
        action = ActionChains(self.driver)
        action.move_to_element(product).move_to_element(quickViewElement).click().perform()
        list = self.driver.find_elements(By.XPATH, "//iframe[contains(@id, 'fancybox-frame')]")
        if len(list) != 0:
            self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//iframe[contains(@id, 'fancybox-frame')]"))
            self.driver.find_element(By.XPATH, "//a[@id='wishlist_button']").click()
            list1 = self.driver.find_elements(By.XPATH, "//p[@class='fancybox-error']")
            assert len(list1) != 0
            self.driver.find_element(By.XPATH, "//a[@title='Close']").click()
            self.driver.switch_to.default_content()
        else:
            assert False
        self.driver.find_element(By.XPATH, "//a[@title='Close']").click()



