from page_objects.Login_Page_Objects import LoginPage
from utilities.readProperties import readConf
from utilities.customLogger import Logger


class TestLoginPage:
    logs = Logger.generate_log()

    def test_login_page_title(self, setup_method):
        self.driver = setup_method
        self.logs.info("****** test_login_page_title ******")
        self.loginpage = LoginPage(self.driver)
        self.loginpage.click_on_signIn_button()
        assert self.driver.title == readConf.get_login_page_title()
        self.logs.info("****** Login Page Title Verification ******")
        self.driver.quit()

    def test_invalid_user_email_error(self, setup_method):
        self.driver = setup_method
        self.logs.info("****** test_invalid_user_email_error ******")
        self.loginpage = LoginPage(self.driver)
        self.loginpage.click_on_signIn_button()
        assert self.driver.title == readConf.get_login_page_title()
        self.loginpage.error_for_invalid_email(readConf.get_invalid_email())
        self.driver.quit()

    def test_email_required_error(self, setup_method):
        self.driver = setup_method
        self.logs.info("****** test_email_required_error ******")
        self.loginpage = LoginPage(self.driver)
        self.loginpage.click_on_signIn_button()
        assert self.driver.title == readConf.get_login_page_title()
        self.loginpage.error_for_email_required()
        self.driver.quit()

    def test_password_required_error(self, setup_method):
        self.driver = setup_method
        self.logs.info("****** test_password_required_error ******")
        self.loginpage = LoginPage(self.driver)
        self.loginpage.click_on_signIn_button()
        assert self.driver.title == readConf.get_login_page_title()
        self.loginpage.error_for_password_required(readConf.get_useremail())
        self.driver.quit()

    def test_already_registered_user_error(self, setup_method):
        self.driver = setup_method
        self.logs.info("****** test_already_registered_user_error ******")
        self.loginpage = LoginPage(self.driver)
        self.loginpage.click_on_signIn_button()
        assert self.driver.title == readConf.get_login_page_title()
        self.loginpage.error_for_already_registered_user()
        self.driver.quit()

    def test_go_to_home_page(self, setup_method):
        self.driver = setup_method
        self.logs.info("****** test_go_to_home_page ******")
        self.loginpage = LoginPage(self.driver)
        self.loginpage.click_on_signIn_button()
        assert self.driver.title == readConf.get_login_page_title()
        self.loginpage.return_to_home_page()
        assert self.driver.title == readConf.get_home_page_title()
        self.driver.quit()

    def test_forgot_password_request(self, setup_method):
        self.driver = setup_method
        self.logs.info("****** test_forgot_password_request ******")
        self.loginpage = LoginPage(self.driver)
        self.loginpage.click_on_signIn_button()
        assert self.driver.title == readConf.get_login_page_title()
        self.loginpage.click_on_forgot_password_link()
        self.loginpage.enter_existing_user_email(readConf.get_useremail())
        self.loginpage.click_retrieve_password_button()
        self.loginpage.verify_password_retrieve_request_success()
        self.driver.quit()

    def test_email_not_entered_error_retrieve_password_page(self, setup_method):
        self.driver = setup_method
        self.logs.info("****** test_email_not_entered_error_retrieve_password_page ******")
        self.loginpage = LoginPage(self.driver)
        self.loginpage.click_on_signIn_button()
        assert self.driver.title == readConf.get_login_page_title()
        self.loginpage.click_on_forgot_password_link()
        self.loginpage.click_retrieve_password_button()
        self.loginpage.invalid_email_error_while_retriving_password()
        self.driver.quit()

    def test_no_account_registered_error_retrieve_password_page(self, setup_method):
        self.driver = setup_method
        self.logs.info("****** test_no_account_registered_error_retrieve_password_page ******")
        self.loginpage = LoginPage(self.driver)
        self.loginpage.click_on_signIn_button()
        assert self.driver.title == readConf.get_login_page_title()
        self.loginpage.click_on_forgot_password_link()
        self.loginpage.enter_existing_user_email(readConf.get_email_for_password_retrieve_error())
        self.loginpage.click_retrieve_password_button()
        self.loginpage.no_account_registered_error_while_retrieving_password()
        self.driver.quit()

    def test_successful_login(self, setup_method):
        self.driver = setup_method
        self.logs.info("****** test_login_page_title ******")
        self.loginpage = LoginPage(self.driver)
        self.loginpage.click_on_signIn_button()
        assert self.driver.title == readConf.get_login_page_title()
        self.logs.info("****** Login Page Title Verification ******")
        self.loginpage.login_with_registered_user()
        self.driver.quit()
