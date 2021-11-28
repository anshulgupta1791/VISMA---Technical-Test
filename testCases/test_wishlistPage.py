from page_objects.Home_Page_Objects import HomePage
from page_objects.Login_Page_Objects import LoginPage
from page_objects.My_Account_Page_Object import MyAccountPage
from page_objects.Wishlist_Page_Object import WishlistPage
from utilities.readProperties import readConf


class TestWishlistFeature:

    def test_wishlist_error_for_not_logged_in_user(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        assert self.driver.title == readConf.get_home_page_title()
        self.homepage.add_popular_product_to_wishlist_from_home_without_loggingIn("Faded")
        self.driver.quit()

    def test_add_to_wishlist_for_logged_in_user(self, setup_method):
        self.driver = setup_method
        self.homepage = HomePage(self.driver)
        self.homepage.click_on_signin_link()
        self.loginpage = LoginPage(self.driver)
        self.loginpage.enter_existing_user_email(readConf.get_useremail())
        self.loginpage.enter_existing_user_password(readConf.get_userpassword())
        self.loginpage.click_login_button()
        self.homepage.return_to_homepage()
        self.homepage.add_popular_product_to_wishlist_from_home_after_loggingIn("Faded")
        self.myaccount = MyAccountPage(self.driver)
        self.myaccount.go_to_my_account_page()
        assert self.driver.title == readConf.get_my_account_page_title()
        self.myaccount.go_to_my_wishlists_page()
        self.wishlistpage = WishlistPage(self.driver)
        self.wishlistpage.click_on_deafult_named_wishlist()
        self.wishlistpage.verify_product_is_displaying_in_wishlist("Faded")
        self.driver.quit()
