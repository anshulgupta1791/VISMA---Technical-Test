from page_objects.Home_Page_Objects import HomePage
from utilities.readProperties import readConf


class TestHomePage:

    def test_home_page_title(self, setup_method):
        self.driver = setup_method
        assert self.driver.title == readConf.get_home_page_title()
        self.driver.close()

    def test_women_tab_link(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_women_tab()
        assert self.driver.title == readConf.get_women_page_title()
        self.driver.quit()

    def test_dresses_tab_link(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_dresses_tab()
        assert self.driver.title == readConf.get_dresses_page_title()
        self.driver.close()

    def test_tshirts_tab_link(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_tshirts_tab()
        assert self.driver.title == readConf.get_tshirts_page_title()
        self.driver.close()

    def test_hidden_tops_tab_link(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        self.homepage.click_on_tops_under_women_tab()
        assert self.driver.title == readConf.get_tops_page_title()
        self.driver.close()

    def test_hidden_dresses_tab_link(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_dresses_under_women_tab()
        assert self.driver.title == readConf.get_dresses_page_title()
        self.driver.close()

    def test_specials_link(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_specials_link()
        assert self.driver.title == readConf.get_specials_page_title()
        self.driver.close()

    def test_new_products_link(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.click_on_new_products_link()
        assert self.driver.title == readConf.get_new_products_page_title()
        self.driver.close()

    def test_best_sellers_footer_link(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        self.homepage.click_on_bestsellers_footer()
        assert self.driver.title == readConf.get_best_sellers_page_title()
        self.driver.quit()

    def test_view_cart_button(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        self.homepage.click_on_view_cart()
        assert self.driver.title == readConf.get_checkout_page_title()
        self.driver.quit()

    def test_search_box_in_header(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        self.homepage.search_a_product("casual")
        assert self.driver.title == readConf.get_search_page_title()
        self.driver.quit()

    def test_header_contact_us_link(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        self.homepage.click_on_contact_us_header()
        assert self.driver.title == readConf.get_contact_us_page_title()
        self.homepage.return_to_homepage()
        assert self.driver.title == readConf.get_home_page_title()
        self.driver.quit()

    def test_clicking_specific_product(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        self.homepage.select_specific_product_from_popular()
        assert "Faded" in self.driver.title
        self.driver.quit()

    def test_clicking_specific_product_from_best_sellers(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        self.homepage.select_specific_product_from_best_sellers()
        assert "Chiffon" in self.driver.title
        self.driver.quit()

    def test_news_letter_subscription(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        self.homepage.subscribe_to_news_letter_with_new_user()
        self.driver.quit()
