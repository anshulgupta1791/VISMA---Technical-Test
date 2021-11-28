from page_objects.Checkout_Page_Objects import CheckoutPage
from page_objects.Home_Page_Objects import HomePage
from page_objects.Product_Page import ProductPage
from page_objects.Woment_TAB_Page_Object import WomenTitlePage
from utilities import excelUtils
from utilities.customLogger import Logger
from utilities.readProperties import readConf


class TestProductPage:

    logs = Logger.generate_log()
    productExcelFile = ".//Test_Data/Products.xlsx"
    product1Sheet = 'Product1'
    product2Sheet = 'Product2'
    product3Sheet = 'Product3'
    product4Sheet = 'Product4'
    product5Sheet = 'Product5'
    product6Sheet = 'Product6'
    product7Sheet = 'Product7'

    def test_productPageTitle(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.wpage = WomenTitlePage(self.driver)
        assert self.driver.title == readConf.get_women_page_title()
        self.wpage.click_on_list_view()
        self.wpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        productCode = self.productpage.verify_product_page_opened(readConf.get_product1_code())
        assert productCode == readConf.get_product1_code()
        self.driver.quit()

    def test_add_product_to_cart(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.wpage = WomenTitlePage(self.driver)
        assert self.driver.title == readConf.get_women_page_title()
        self.wpage.click_on_list_view()
        self.wpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        productCode = self.productpage.verify_product_page_opened(readConf.get_product1_code())
        assert productCode == readConf.get_product1_code()
        self.productpage.add_to_cart()
        self.productpage.verify_product_added_to_cart()
        self.driver.quit()

    def test_continue_shopping_button(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.wpage = WomenTitlePage(self.driver)
        assert self.driver.title == readConf.get_women_page_title()
        self.wpage.click_on_list_view()
        self.wpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        productCode = self.productpage.verify_product_page_opened(readConf.get_product1_code())
        assert productCode == readConf.get_product1_code()
        self.productpage.add_to_cart()
        self.productpage.verify_product_added_to_cart()
        self.productpage.click_on_continue_shopping_button()
        productCode = self.productpage.verify_product_page_opened(readConf.get_product1_code())
        assert productCode == readConf.get_product1_code()
        self.driver.quit()

    def test_add_medium_size_product_to_cart(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.wpage = WomenTitlePage(self.driver)
        assert self.driver.title == readConf.get_women_page_title()
        self.wpage.click_on_list_view()
        self.wpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        productCode = self.productpage.verify_product_page_opened(readConf.get_product1_code())
        assert productCode == readConf.get_product1_code()
        self.productpage.select_size(readConf.get_medium_size())
        self.productpage.add_to_cart()
        self.productpage.verify_product_added_to_cart()
        self.productpage.confirm_selected_size_product_is_added_to_cart(readConf.get_medium_size())
        self.driver.quit()

    def test_add_large_size_product_to_cart(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.wpage = WomenTitlePage(self.driver)
        assert self.driver.title == readConf.get_women_page_title()
        self.wpage.click_on_list_view()
        self.wpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        productCode = self.productpage.verify_product_page_opened(readConf.get_product1_code())
        assert productCode == readConf.get_product1_code()
        self.productpage.select_size(readConf.get_large_size())
        self.productpage.add_to_cart()
        self.productpage.verify_product_added_to_cart()
        self.productpage.confirm_selected_size_product_is_added_to_cart(readConf.get_large_size())
        self.driver.quit()

    def test_add_small_size_product_to_cart(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.wpage = WomenTitlePage(self.driver)
        assert self.driver.title == readConf.get_women_page_title()
        self.wpage.click_on_list_view()
        self.wpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        productCode = self.productpage.verify_product_page_opened(readConf.get_product1_code())
        assert productCode == readConf.get_product1_code()
        self.productpage.add_to_cart()
        self.productpage.verify_product_added_to_cart()
        self.productpage.confirm_selected_size_product_is_added_to_cart(readConf.get_small_size())
        self.driver.quit()

    def test_add_specific_color_product_to_cart(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.wpage = WomenTitlePage(self.driver)
        assert self.driver.title == readConf.get_women_page_title()
        self.wpage.click_on_list_view()
        self.wpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        productCode = self.productpage.verify_product_page_opened(readConf.get_product1_code())
        assert productCode == readConf.get_product1_code()
        self.productpage.select_color(readConf.get_blue_color())
        self.productpage.add_to_cart()
        self.productpage.verify_product_added_to_cart()
        self.productpage.confirm_selected_color_product_is_added_to_cart(readConf.get_blue_color())
        self.driver.quit()

    def test_add_specific_color_product_to_cart_1(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.wpage = WomenTitlePage(self.driver)
        assert self.driver.title == readConf.get_women_page_title()
        self.wpage.click_on_list_view()
        self.wpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        productCode = self.productpage.verify_product_page_opened(readConf.get_product1_code())
        assert productCode == readConf.get_product1_code()
        self.productpage.select_color(readConf.get_orange_color())
        self.productpage.add_to_cart()
        self.productpage.verify_product_added_to_cart()
        self.productpage.confirm_selected_color_product_is_added_to_cart(readConf.get_orange_color())
        self.driver.quit()

    def test_proceed_to_checkout_button(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.wpage = WomenTitlePage(self.driver)
        assert self.driver.title == readConf.get_women_page_title()
        self.wpage.click_on_list_view()
        self.wpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        productCode = self.productpage.verify_product_page_opened(readConf.get_product1_code())
        assert productCode == readConf.get_product1_code()
        self.productpage.add_to_cart()
        self.productpage.verify_product_added_to_cart()
        self.productpage.click_on_proceed_to_checkout_button()
        assert self.driver.title == readConf.get_checkout_page_title()
        self.driver.quit()

    def test_verify_price(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.wpage = WomenTitlePage(self.driver)
        assert self.driver.title == readConf.get_women_page_title()
        self.wpage.click_on_list_view()
        self.wpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        productCode = self.productpage.verify_product_page_opened(readConf.get_product1_code())
        assert productCode == readConf.get_product1_code()
        self.productpage.check_displayed_price_of_product(16.51)
        self.driver.quit()

    def test_product_quantity_added(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.wpage = WomenTitlePage(self.driver)
        assert self.driver.title == readConf.get_women_page_title()
        self.wpage.click_on_list_view()
        self.wpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        productCode = self.productpage.verify_product_page_opened(readConf.get_product1_code())
        assert productCode == readConf.get_product1_code()
        self.productpage.add_to_cart()
        afterAddingToCart = self.productpage.verify_product_quantity_added_in_cart()
        assert 1 == afterAddingToCart
        self.driver.quit()

    def test_product_quick_view_popup_open(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.wpage = WomenTitlePage(self.driver)
        assert self.driver.title == readConf.get_women_page_title()
        self.wpage.click_on_list_view()
        self.productPage = ProductPage(self.driver)
        self.productPage.quick_view_a_product(readConf.get_product1_text())
        self.productPage.verify_quick_view_popup_open()
        self.driver.quit()

    def test_color_not_available_for_selected_product(self, setup_method):
        self.logs.info("****** test_color_not_available_for_selected_product ******")
        self.logs.info("****** Started ******")
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.wpage = WomenTitlePage(self.driver)
        assert self.driver.title == readConf.get_women_page_title()
        self.wpage.click_on_list_view()
        self.wpage.click_on_specified_product(readConf.get_product1_text())
        self.productPage = ProductPage(self.driver)
        self.productPage.select_color(readConf.get_beige_color())
        self.driver.quit()
        self.logs.info("****** Finished ******")

    # below test case can be implemented for all other 6 products
    def test_add_all_variety_of_product1_in_cart(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.wpage = WomenTitlePage(self.driver)
        assert self.driver.title == readConf.get_women_page_title()
        self.wpage.click_on_list_view()
        self.wpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        self.rows = excelUtils.get_row_count(self.productExcelFile, self.product1Sheet)
        count = 0
        for r in range(2, self.rows + 1):
            self.color = excelUtils.read_data(self.productExcelFile, self.product1Sheet, r, 2)
            self.size = excelUtils.read_data(self.productExcelFile, self.product2Sheet, r, 3)
            self.productpage.select_color(self.color)
            self.productpage.select_size(self.size)
            self.productpage.add_to_cart()
            self.productpage.verify_product_added_to_cart()
            self.productpage.click_on_continue_shopping_button()
            count += 1
        count = str(count)
        self.homepage.click_on_view_cart()
        self.checkout = CheckoutPage(self.driver)
        productsInCart = self.checkout.get_number_of_products_in_cart()
        assert count in productsInCart
        self.driver.quit()

    def test_add_product_to_wishlist_without_signin(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.wpage = WomenTitlePage(self.driver)
        assert self.driver.title == readConf.get_women_page_title()
        self.wpage.click_on_list_view()
        self.wpage.click_to_add_product_in_wishlist_without_signin(readConf.get_product1_text())
        self.driver.quit()
