from selenium.webdriver.common.by import By

from utilities import excelUtils
from utilities.customLogger import Logger
from utilities.readProperties import readConf


class LoginPage:
    logs = Logger.generate_log()
    existingUserFilePath = ".//Test_Data/ExistingUserLoginDetails.xlsx"
    sheet = "Sheet1"

    """BY LOCATORS OR OBJECT REPOSITORY"""
    SIGNIN_XPATH = "//a[normalize-space()='Sign in']"
    USERNAME_ID = "email"
    PASSWORD_ID = "passwd"
    LOGINBUTTON_XPATH = "//span[normalize-space()='Sign in']"
    LOGOUTBUTTON_XPATH = "//a[@title='Log me out']"
    INPUTEMAILNEWUSER_ID = "email_create"
    CREATENEWACCOUNTBUTTON_XPATH = "//span[normalize-space()='Create an account']"
    INVALIDEMAILERRORMESSAGE_XPATH = "//li[normalize-space()='Invalid email address.']"
    NOEMAILENTEREDERRORMESSAGE_XPATH = "//li[normalize-space()='An email address required.']"
    NOPASSWORDENTEREDERROMESSAGE_XPATH = "//li[normalize-space()='Password is required.']"
    USERALREADYREGISTEREDERRORMESSAGE_XPATH = "//li[contains(text(),'An account using this email address has already be')]"
    HOMEBUTTON_CLASSNAME = "home"
    FORGOTPASSWORDLINK_LINKTEXT = "Forgot your password?"
    RETRIVEPASSWORDBUTTON_XPATH = "//span[normalize-space()='Retrieve Password']"
    PASSWORDRETRIEVEREQUESTSUCCESS_XPATH = "//p[@class='alert alert-success']"
    INVALIDEMAILERRORONRETRIEVEPASSPORDSTEP_XPATH = "//li[normalize-space()='Invalid email address.']"
    NOREGISTEREDACCOUNTERRORONRETRIEVEPASSWORDSTEP_XPATH = "//li[contains(text(),'There is no account registered for this email addr')]"

    def __init__(self, driver):
        self.driver = driver

    def click_on_signIn_button(self):
        self.driver.find_element(By.XPATH, self.SIGNIN_XPATH).click()

    def enter_existing_user_email(self, email):
        self.driver.find_element(By.ID, self.USERNAME_ID).clear()
        self.driver.find_element(By.ID, self.USERNAME_ID).send_keys(email)

    def enter_existing_user_password(self, password):
        self.driver.find_element(By.ID, self.PASSWORD_ID).clear()
        self.driver.find_element(By.ID, self.PASSWORD_ID).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.LOGINBUTTON_XPATH).click()

    def click_logout_button(self):
        self.driver.find_element(By.XPATH, self.LOGOUTBUTTON_XPATH).click()

    def enter_new_user_email(self, newUserEmail):
        self.driver.find_element(By.ID, self.INPUTEMAILNEWUSER_ID).clear()
        self.driver.find_element(By.ID, self.INPUTEMAILNEWUSER_ID).send_keys(newUserEmail)

    def click_create_account_button(self):
        self.driver.find_element(By.XPATH, self.CREATENEWACCOUNTBUTTON_XPATH).click()

    def error_for_invalid_email(self, email):
        self.enter_existing_user_email(email)
        self.click_login_button()
        list = self.driver.find_elements(By.XPATH, self.INVALIDEMAILERRORMESSAGE_XPATH)
        if len(list) == 0:
            assert False
        else:
            assert True

    def error_for_email_required(self):
        self.enter_existing_user_email("")
        self.click_login_button()
        list = self.driver.find_elements(By.XPATH, self.NOEMAILENTEREDERRORMESSAGE_XPATH)
        if len(list) == 0:
            assert False
        else:
            assert True

    def error_for_password_required(self, email):
        self.enter_existing_user_email(email)
        self.enter_existing_user_password("")
        self.click_login_button()
        list = self.driver.find_elements(By.XPATH, self.NOPASSWORDENTEREDERROMESSAGE_XPATH)
        if len(list) == 0:
            assert False
        else:
            assert True

    def error_for_already_registered_user(self):
        self.rows = excelUtils.get_row_count(self.existingUserFilePath, self.sheet)
        for r in range(2, self.rows + 1):
            self.useremail = excelUtils.read_data(self.existingUserFilePath, self.sheet, r, 1)
            self.enter_new_user_email(self.useremail)
            self.click_create_account_button()
            list = self.driver.find_elements(By.XPATH, self.USERALREADYREGISTEREDERRORMESSAGE_XPATH)
            if len(list) == 0:
                assert False
            else:
                assert True

    def return_to_home_page(self):
        self.click_on_signIn_button()
        self.driver.find_element(By.CLASS_NAME, self.HOMEBUTTON_CLASSNAME).click()

    def click_on_forgot_password_link(self):
        self.driver.find_element(By.LINK_TEXT, self.FORGOTPASSWORDLINK_LINKTEXT).click()

    def click_retrieve_password_button(self):
        self.driver.find_element(By.XPATH, self.RETRIVEPASSWORDBUTTON_XPATH).click()

    def verify_password_retrieve_request_success(self):
        list = self.driver.find_elements(By.XPATH, self.PASSWORDRETRIEVEREQUESTSUCCESS_XPATH)
        if len(list) == 0:
            assert False
        else:
            assert True

    def invalid_email_error_while_retriving_password(self):
        list = self.driver.find_elements(By.XPATH, self.INVALIDEMAILERRORONRETRIEVEPASSPORDSTEP_XPATH)
        if len(list) == 0:
            assert False
        else:
            assert True

    def no_account_registered_error_while_retrieving_password(self):
        list = self.driver.find_elements(By.XPATH, self.NOREGISTEREDACCOUNTERRORONRETRIEVEPASSWORDSTEP_XPATH)
        if len(list) == 0:
            assert False
        else:
            assert True

    def login_with_registered_user(self):
        self.rows = excelUtils.get_row_count(self.existingUserFilePath, self.sheet)
        list_status = []
        for r in range(2, self.rows + 1):
            self.useremail = excelUtils.read_data(self.existingUserFilePath, self.sheet, r, 1)
            self.password = excelUtils.read_data(self.existingUserFilePath, self.sheet, r, 2)
            self.exResult = excelUtils.read_data(self.existingUserFilePath, self.sheet, r, 3)
            self.enter_existing_user_email(self.useremail)
            self.enter_existing_user_password(self.password)
            self.click_login_button()
            if self.driver.title == readConf.get_my_account_page_title():
                if self.exResult == 'Pass':
                    self.logs.info("****** Succesfully Logged In With Registred User - TEST PASSED ******")
                    list_status.append('Pass')
                elif self.exResult == 'Fail':
                    self.logs.info("****** Successfully Logges In With NON-Registered User - TEST FAILED ******")
                    list_status.append('Fail')
            elif self.driver.title != readConf.get_my_account_page_title():
                if self.exResult == 'Pass':
                    self.logs.info("****** User Is Not Logged In - TEST FAILED ******")
                    list_status.append('Fail')
                elif self.exResult == 'Fail':
                    self.logs.info("****** NON-Registered User Not Logged - TEST PASSED ******")
                    list_status.append('Pass')

        assert 'Fail' not in list_status

    def login_with_registered_user_at_checkout(self):
        self.rows = excelUtils.get_row_count(self.existingUserFilePath, self.sheet)
        list_status = []
        for r in range(2, self.rows + 1):
            self.useremail = excelUtils.read_data(self.existingUserFilePath, self.sheet, r, 1)
            self.password = excelUtils.read_data(self.existingUserFilePath, self.sheet, r, 2)
            self.exResult = excelUtils.read_data(self.existingUserFilePath, self.sheet, r, 3)
            self.enter_existing_user_email(self.useremail)
            self.enter_existing_user_password(self.password)
            self.click_login_button()
