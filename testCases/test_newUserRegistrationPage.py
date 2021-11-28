from page_objects.Login_Page_Objects import LoginPage
from page_objects.New_User_Account_Page_Object import NewUserAccountCreationPage


class TestNewUserRegistrationPage:

    def test_new_user_registration_page_title(self, setup_method):
        self.driver = setup_method
        self.loginpage = LoginPage(self.driver)
        self.loginpage.click_on_signIn_button()
        self.loginpage.enter_new_user_email("test171291@gmail.com")
        self.loginpage.click_create_account_button()
        self.newuser = NewUserAccountCreationPage(self.driver)
        self.newuser.verify_form_title()
        self.driver.quit()

    def test_mandatory_errors_displaying(self, setup_method):
        self.driver = setup_method
        self.loginpage = LoginPage(self.driver)
        self.loginpage.click_on_signIn_button()
        self.loginpage.enter_new_user_email("test171291@gmail.com")
        self.loginpage.click_create_account_button()
        self.newuser = NewUserAccountCreationPage(self.driver)
        self.newuser.verify_form_title()
        self.newuser.click_on_register_account_button()
        self.newuser.verify_city_required_error()
        self.newuser.verify_state_required_error()
        self.newuser.verify_password_required_error()
        self.newuser.verify_first_name_require_error()
        self.newuser.verify_phone_number_not_entered_error()
        self.newuser.verify_address_line1_required_error()
        self.newuser.verify_zip_code_required_error()
        self.newuser.verify_last_name_required_error()
        self.driver.quit()

    def test_new_user_registration(self, setup_method):
        self.driver = setup_method
        self.loginpage = LoginPage(self.driver)
        self.loginpage.click_on_signIn_button()
        self.newuser = NewUserAccountCreationPage(self.driver)
        self.newuser.registering_new_user()
        self.driver.quit()
