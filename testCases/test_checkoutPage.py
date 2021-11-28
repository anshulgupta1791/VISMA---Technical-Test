from page_objects.Checkout_Page_Objects import CheckoutPage
from page_objects.Home_Page_Objects import HomePage
from page_objects.Login_Page_Objects import LoginPage
from page_objects.Order_History_Page_Object import OrderHistory
from page_objects.Product_Page import ProductPage
from page_objects.Woment_TAB_Page_Object import WomenTitlePage
from utilities.readProperties import readConf


class TestCheckoutSection:
    products = (readConf.get_product1_text(), readConf.get_product2_text())

    def test_view_my_cart(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_view_cart()
        assert self.driver.title == readConf.get_checkout_page_title()
        self.driver.quit()

    def test_cart_is_empty(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_view_cart()
        assert self.driver.title == readConf.get_checkout_page_title()
        self.checkout = CheckoutPage(self.driver)
        self.checkout.verify_cart_is_empty()
        self.driver.quit()

    def test_cart_is_not_empty(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.womenpage = WomenTitlePage(self.driver)
        self.womenpage.click_on_list_view()
        self.womenpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        self.productpage.add_to_cart()
        self.productpage.verify_product_added_to_cart()
        self.productpage.click_on_proceed_to_checkout_button()
        self.checkout = CheckoutPage(self.driver)
        assert readConf.get_checkout_page_title() == self.driver.title
        self.checkout.verify_cart_is_not_empty()
        self.driver.quit()

    def test_login_step_in_checkout(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.womenpage = WomenTitlePage(self.driver)
        self.womenpage.click_on_list_view()
        self.womenpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        self.productpage.add_to_cart()
        self.productpage.verify_product_added_to_cart()
        self.productpage.click_on_proceed_to_checkout_button()
        self.checkout = CheckoutPage(self.driver)
        assert readConf.get_checkout_page_title() == self.driver.title
        self.checkout.verify_cart_is_not_empty()
        self.checkout.proceed_to_signin_step()
        self.loginpage = LoginPage(self.driver)
        self.loginpage.login_with_registered_user_at_checkout()
        self.checkout.verify_user_is_at_address_step()
        self.driver.quit()

    def test_verify_total_cart_value(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.womenpage = WomenTitlePage(self.driver)
        self.womenpage.click_on_list_view()
        self.womenpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        self.productpage.add_to_cart()
        self.productpage.verify_product_added_to_cart()
        self.productpage.click_on_proceed_to_checkout_button()
        self.checkout = CheckoutPage(self.driver)
        assert readConf.get_checkout_page_title() == self.driver.title
        self.checkout.verify_cart_is_not_empty()
        self.checkout.verify_total_amount_before_tax()
        self.checkout.verify_amount_after_tax()
        self.driver.quit()

    def test_verify_total_product_price_for_one_unit(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.womenpage = WomenTitlePage(self.driver)
        self.womenpage.click_on_list_view()
        self.womenpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        self.productpage.add_to_cart()
        self.productpage.verify_product_added_to_cart()
        self.productpage.click_on_proceed_to_checkout_button()
        self.checkout = CheckoutPage(self.driver)
        assert readConf.get_checkout_page_title() == self.driver.title
        self.checkout.verify_cart_is_not_empty()
        unitPrice = self.checkout.get_unit_price_for_a_product(readConf.get_orange_color(), readConf.get_small_size(), readConf.get_product1_identifier())
        totalPrice = self.checkout.get_total_unit_costs(readConf.get_orange_color(), readConf.get_small_size(), readConf.get_product1_identifier())
        assert unitPrice == totalPrice
        self.driver.quit()

    def test_verify_total_product_price_for_more_than_one_unit(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.womenpage = WomenTitlePage(self.driver)
        self.womenpage.click_on_list_view()
        self.womenpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        self.productpage.enter_product_quantity(readConf.get_product_quanity())
        self.productpage.add_to_cart()
        self.productpage.verify_product_added_to_cart()
        self.productpage.click_on_proceed_to_checkout_button()
        self.checkout = CheckoutPage(self.driver)
        assert readConf.get_checkout_page_title() == self.driver.title
        self.checkout.verify_cart_is_not_empty()
        unitPrice = self.checkout.get_unit_price_for_a_product(readConf.get_orange_color(), readConf.get_small_size(),
                                                               readConf.get_product1_identifier())
        totalPrice = self.checkout.get_total_unit_costs(readConf.get_orange_color(), readConf.get_small_size(),
                                                        readConf.get_product1_identifier())
        assert totalPrice == (unitPrice * readConf.get_product_quanity())
        self.driver.quit()

    def test_verify_total_amount_for_different_products_in_cart(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        
        for i in self.products:
            self.homepage.click_on_women_tab()
            self.womenpage = WomenTitlePage(self.driver)
            self.womenpage.click_on_list_view()
            self.womenpage.click_on_specified_product(i)
            self.productpage = ProductPage(self.driver)
            self.productpage.add_to_cart()
            self.productpage.verify_product_added_to_cart()
            self.productpage.click_on_proceed_to_checkout_button()
        self.checkout = CheckoutPage(self.driver)
        assert readConf.get_checkout_page_title() == self.driver.title
        self.checkout.verify_cart_is_not_empty()
        unitPriceForProduct1 = self.checkout.get_unit_price_for_a_product(readConf.get_orange_color(), readConf.get_small_size(), readConf.get_product1_identifier())
        unitPriceForProduct2 = self.checkout.get_unit_price_for_a_product(readConf.get_black_color(), readConf.get_small_size(), readConf.get_product2_identifier())
        totalPriceOfProduct1 = self.checkout.get_total_unit_costs(readConf.get_orange_color(), readConf.get_small_size(), readConf.get_product1_identifier())
        totalPriceOfProduct2 = self.checkout.get_total_unit_costs(readConf.get_black_color(), readConf.get_small_size(), readConf.get_product2_identifier())
        assert (unitPriceForProduct2 == totalPriceOfProduct2) and (unitPriceForProduct1 == totalPriceOfProduct1)
        self.driver.quit()

    def test_delivery_and_billing_details_are_same(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.womenpage = WomenTitlePage(self.driver)
        self.womenpage.click_on_list_view()
        self.womenpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        self.productpage.add_to_cart()
        self.productpage.verify_product_added_to_cart()
        self.productpage.click_on_proceed_to_checkout_button()
        self.checkout = CheckoutPage(self.driver)
        assert readConf.get_checkout_page_title() == self.driver.title
        self.checkout.verify_cart_is_not_empty()
        self.checkout.proceed_to_signin_step()
        self.loginpage = LoginPage(self.driver)
        self.loginpage.login_with_registered_user_at_checkout()
        self.checkout.verify_user_is_at_address_step()
        self.checkout.compare_address_at_address_step()
        self.checkout.compare_phone_number_at_address_step()
        self.checkout.compare_user_name_at_address_step()
        self.driver.quit()

    def test_update_delivery_details(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.womenpage = WomenTitlePage(self.driver)
        self.womenpage.click_on_list_view()
        self.womenpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        self.productpage.add_to_cart()
        self.productpage.verify_product_added_to_cart()
        self.productpage.click_on_proceed_to_checkout_button()
        self.checkout = CheckoutPage(self.driver)
        assert readConf.get_checkout_page_title() == self.driver.title
        self.checkout.verify_cart_is_not_empty()
        self.checkout.proceed_to_signin_step()
        self.loginpage = LoginPage(self.driver)
        self.loginpage.login_with_registered_user_at_checkout()
        self.checkout.verify_user_is_at_address_step()
        self.checkout.click_to_update_delivery_address()
        self.checkout.verify_delivery_address_update()
        self.checkout.verify_delivery_city_update()
        self.checkout.verify_delivery_state_update()
        self.checkout.verify_delivery_mobile_number_update()
        self.checkout.verify_delivery_home_number_update()
        self.checkout.verify_delivery_zip_code_update()
        self.driver.quit()

    def test_update_billing_details(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.womenpage = WomenTitlePage(self.driver)
        self.womenpage.click_on_list_view()
        self.womenpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        self.productpage.add_to_cart()
        self.productpage.verify_product_added_to_cart()
        self.productpage.click_on_proceed_to_checkout_button()
        self.checkout = CheckoutPage(self.driver)
        assert readConf.get_checkout_page_title() == self.driver.title
        self.checkout.verify_cart_is_not_empty()
        self.checkout.proceed_to_signin_step()
        self.loginpage = LoginPage(self.driver)
        self.loginpage.login_with_registered_user_at_checkout()
        self.checkout.verify_user_is_at_address_step()
        self.checkout.click_to_update_billing_address()
        self.checkout.verify_billing_address_update()
        self.checkout.verify_billing_zip()
        self.checkout.verify_billing_city()
        self.checkout.verify_billing_state()
        self.checkout.verify_billing_home_phone()
        self.checkout.verify_billing_mobile_number()
        self.driver.quit()

    def test_different_billing_delivery_address(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.womenpage = WomenTitlePage(self.driver)
        self.womenpage.click_on_list_view()
        self.womenpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        self.productpage.add_to_cart()
        self.productpage.verify_product_added_to_cart()
        self.productpage.click_on_proceed_to_checkout_button()
        self.checkout = CheckoutPage(self.driver)
        assert readConf.get_checkout_page_title() == self.driver.title
        self.checkout.verify_cart_is_not_empty()
        self.checkout.proceed_to_signin_step()
        self.loginpage = LoginPage(self.driver)
        self.loginpage.login_with_registered_user_at_checkout()
        self.checkout.verify_user_is_at_address_step()
        self.checkout.click_to_make_billing_and_delivery_address_different()
        self.checkout.verify_billing_address_update()
        self.checkout.verify_billing_zip()
        self.checkout.verify_billing_city()
        self.checkout.verify_billing_state()
        self.checkout.verify_billing_home_phone()
        self.checkout.verify_billing_mobile_number()
        self.driver.quit()

    def test_shipping_step_in_checkout(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.womenpage = WomenTitlePage(self.driver)
        self.womenpage.click_on_list_view()
        self.womenpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        self.productpage.add_to_cart()
        self.productpage.verify_product_added_to_cart()
        self.productpage.click_on_proceed_to_checkout_button()
        self.checkout = CheckoutPage(self.driver)
        assert readConf.get_checkout_page_title() == self.driver.title
        self.checkout.verify_cart_is_not_empty()
        self.checkout.proceed_to_signin_step()
        self.loginpage = LoginPage(self.driver)
        self.loginpage.login_with_registered_user_at_checkout()
        self.checkout.verify_user_is_at_address_step()
        self.checkout.click_on_proceed_to_shipping_step()
        self.checkout.verify_user_is_at_shipping_step()
        self.driver.quit()

    def test_user_at_payment_step(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.womenpage = WomenTitlePage(self.driver)
        self.womenpage.click_on_list_view()
        self.womenpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        self.productpage.add_to_cart()
        self.productpage.verify_product_added_to_cart()
        self.productpage.click_on_proceed_to_checkout_button()
        self.checkout = CheckoutPage(self.driver)
        assert readConf.get_checkout_page_title() == self.driver.title
        self.checkout.verify_cart_is_not_empty()
        self.checkout.proceed_to_signin_step()
        self.loginpage = LoginPage(self.driver)
        self.loginpage.login_with_registered_user_at_checkout()
        self.checkout.verify_user_is_at_address_step()
        self.checkout.click_on_proceed_to_shipping_step()
        self.checkout.verify_user_is_at_shipping_step()
        self.checkout.click_on_proceed_to_payment_step()
        self.driver.quit()

    def test_payment_step(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.womenpage = WomenTitlePage(self.driver)
        self.womenpage.click_on_list_view()
        self.womenpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        self.productpage.add_to_cart()
        self.productpage.verify_product_added_to_cart()
        self.productpage.click_on_proceed_to_checkout_button()
        self.checkout = CheckoutPage(self.driver)
        assert readConf.get_checkout_page_title() == self.driver.title
        self.checkout.verify_cart_is_not_empty()
        totalPerProductAmountInCart = self.checkout.get_unit_price_of_product_in_cart()
        totalProductAmountInCart = self.checkout.get_total_products_price()
        self.checkout.proceed_to_signin_step()
        self.loginpage = LoginPage(self.driver)
        self.loginpage.login_with_registered_user_at_checkout()
        self.checkout.verify_user_is_at_address_step()
        self.checkout.click_on_proceed_to_shipping_step()
        self.checkout.verify_user_is_at_shipping_step()
        self.checkout.click_on_agree_terms_checkbox_at_shipping_step()
        self.checkout.click_on_proceed_to_payment_step()
        totalPerProductAmountAtPaymentPage = self.checkout.verify_unit_price_of_product_at_payment_page(readConf.get_orange_color(),
                                                                   readConf.get_small_size(),
                                                                   readConf.get_product1_identifier())
        totalProductAmountAtPaymentPage = self.checkout.verify_product_total_amount_at_payment_page(readConf.get_orange_color(),
                                                                   readConf.get_small_size(),
                                                                   readConf.get_product1_identifier())
        assert (totalPerProductAmountInCart == totalPerProductAmountAtPaymentPage) and (totalProductAmountInCart == totalProductAmountAtPaymentPage)
        self.driver.quit()

    def test_order_by_bank_wire(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.womenpage = WomenTitlePage(self.driver)
        self.womenpage.click_on_list_view()
        self.womenpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        self.productpage.add_to_cart()
        self.productpage.verify_product_added_to_cart()
        self.productpage.click_on_proceed_to_checkout_button()
        self.checkout = CheckoutPage(self.driver)
        assert readConf.get_checkout_page_title() == self.driver.title
        self.checkout.verify_cart_is_not_empty()
        self.checkout.proceed_to_signin_step()
        self.loginpage = LoginPage(self.driver)
        self.loginpage.login_with_registered_user_at_checkout()
        self.checkout.verify_user_is_at_address_step()
        self.checkout.click_on_proceed_to_shipping_step()
        self.checkout.verify_user_is_at_shipping_step()
        self.checkout.click_on_agree_terms_checkbox_at_shipping_step()
        self.checkout.click_on_proceed_to_payment_step()
        self.checkout.click_on_pay_by_bank_wire_link()
        self.checkout.click_on_order_confirm_button()
        assert readConf.get_order_confirmation_page_title() == self.driver.title
        self.driver.quit()

    def test_order_by_cheque(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.womenpage = WomenTitlePage(self.driver)
        self.womenpage.click_on_list_view()
        self.womenpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        self.productpage.add_to_cart()
        self.productpage.verify_product_added_to_cart()
        self.productpage.click_on_proceed_to_checkout_button()
        self.checkout = CheckoutPage(self.driver)
        assert readConf.get_checkout_page_title() == self.driver.title
        self.checkout.verify_cart_is_not_empty()
        self.checkout.proceed_to_signin_step()
        self.loginpage = LoginPage(self.driver)
        self.loginpage.login_with_registered_user_at_checkout()
        self.checkout.verify_user_is_at_address_step()
        self.checkout.click_on_proceed_to_shipping_step()
        self.checkout.verify_user_is_at_shipping_step()
        self.checkout.click_on_agree_terms_checkbox_at_shipping_step()
        self.checkout.click_on_proceed_to_payment_step()
        self.checkout.click_on_pay_by_cheque_link()
        self.checkout.click_on_order_confirm_button()
        assert readConf.get_order_confirmation_page_title() == self.driver.title
        self.driver.quit()

    def test_order_reference_number_present_in_order_history(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.womenpage = WomenTitlePage(self.driver)
        self.womenpage.click_on_list_view()
        self.womenpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        self.productpage.add_to_cart()
        self.productpage.verify_product_added_to_cart()
        self.productpage.click_on_proceed_to_checkout_button()
        self.checkout = CheckoutPage(self.driver)
        assert readConf.get_checkout_page_title() == self.driver.title
        self.checkout.verify_cart_is_not_empty()
        self.checkout.proceed_to_signin_step()
        self.loginpage = LoginPage(self.driver)
        self.loginpage.login_with_registered_user_at_checkout()
        self.checkout.verify_user_is_at_address_step()
        self.checkout.click_on_proceed_to_shipping_step()
        self.checkout.verify_user_is_at_shipping_step()
        self.checkout.click_on_agree_terms_checkbox_at_shipping_step()
        self.checkout.click_on_proceed_to_payment_step()
        self.checkout.click_on_pay_by_cheque_link()
        self.checkout.click_on_order_confirm_button()
        assert readConf.get_order_confirmation_page_title() == self.driver.title
        orderRefAfterPayment = self.checkout.order_reference_on_confirmation_page()
        self.checkout.back_to_orders_page_from_confirmation_page()
        self.order = OrderHistory(self.driver)
        recentOrderRefInHistory = self.order.get_most_recent_order_reference()
        assert recentOrderRefInHistory in orderRefAfterPayment
        self.driver.quit()

    def test_update_payment_from_bank_wire_to_cheque(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        self.womenpage = WomenTitlePage(self.driver)
        self.womenpage.click_on_list_view()
        self.womenpage.click_on_specified_product(readConf.get_product1_text())
        self.productpage = ProductPage(self.driver)
        self.productpage.add_to_cart()
        self.productpage.verify_product_added_to_cart()
        self.productpage.click_on_proceed_to_checkout_button()
        self.checkout = CheckoutPage(self.driver)
        assert readConf.get_checkout_page_title() == self.driver.title
        self.checkout.verify_cart_is_not_empty()
        self.checkout.proceed_to_signin_step()
        self.loginpage = LoginPage(self.driver)
        self.loginpage.login_with_registered_user_at_checkout()
        self.checkout.verify_user_is_at_address_step()
        self.checkout.click_on_proceed_to_shipping_step()
        self.checkout.verify_user_is_at_shipping_step()
        self.checkout.click_on_agree_terms_checkbox_at_shipping_step()
        self.checkout.click_on_proceed_to_payment_step()
        self.checkout.click_on_pay_by_bank_wire_link()
        bankWireHeading = self.checkout.verify_bank_wire_payment_heading()
        self.checkout.click_to_change_payment_type()
        self.checkout.click_on_pay_by_cheque_link()
        chequeHeading = self.checkout.verify_cheque_payment_heading()
        assert bankWireHeading != chequeHeading
        self.driver.quit()