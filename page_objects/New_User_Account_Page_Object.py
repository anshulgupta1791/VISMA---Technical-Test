from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.Login_Page_Objects import LoginPage
from utilities import excelUtils
from utilities.readProperties import readConf


class NewUserAccountCreationPage:

    newUserExcel = './/Test_Data/NewUsersForRegistration.xlsx'
    sheet = 'Sheet1'

    """BY LOCATORS OR OBJECT REPOSITORY"""
    NEWUSERACCOUNTFORMTITLE_XPATH = "//h3[normalize-space()='Your personal information']"
    MALERADIOBUTTON_XPATH = "//label[normalize-space()='Mr.']"
    FEMALERADIOBUTTON_XPATH = "//input[@value='2']"
    INPUTFIRSTNAME_ID = "customer_firstname"
    INPUTLASTNAME_ID = "customer_lastname"
    INPUTPASSWORD_ID = "passwd"
    SELECTDAY_ID = "days"
    SELECTMONTH_ID = "months"
    SELECTYEAR_ID = "years"
    NEWSLETTERCHECKBOX_ID = "newsletter"
    OFFERSCHECKBOX_ID = "optin"
    INPUTFNAMEADDRESS_ID = "firstname"
    INPUTLNAMEADDRESS_ID = "lastname"
    INPUTCOMPANYNAME_ID = "company"
    INPUTADDRESSLINE1_ID = "address1"
    INPUTADDRESSLINE2_ID = "address2"
    INPUTCITY_ID = "city"
    SELECTSTATE_ID = "id_state"
    INPUTZIPCODE_ID = "postcode"
    INPUTADDINFOR_ID = "other"
    INPUTHOMEPHONE_ID = "phone"
    INPUTMOBILEPHONE_ID = "phone_mobile"
    INPUTADDRESSALIAS_ID = "alias"
    REGISTERACCOUNTBUTTON_XPATH = "//span[normalize-space()='Register']"
    NOPHONENUMBERPROVIDEDERROR_XPATH = "//li[normalize-space()='You must register at least one phone number.']"
    LNAMEREQUIREDERROR_XPATH = "//b[normalize-space()='lastname']"
    FNAMEREQUIREDERROR_XPATH = "//b[normalize-space()='firstname']"
    EMAILREQUIREDERROR_XPATH = "//b[normalize-space()='email']"
    PASSWORDREQUIREDERROR_XPATH = "//b[normalize-space()='passwd']"
    ADDRESSALIASREQUIREDERROR_XPATH = "//b[normalize-space()='alias']"
    ADDRESSLINE1REQUIREDERROR_XPATH = "//b[normalize-space()='address1']"
    CITYREQUIREDERROR_XPATH = "//b[normalize-space()='city']"
    ZIPCODEREQUIREDERROR_XPATH = "//li[contains(text(),'Postal code')]"
    STATEREQUIREDERROR_XPATH = "//li[normalize-space()='This country requires you to choose a State.']"
    TECHNICALERRORONLOGINPAGE_XPATH = "//div[@class='fancybox-outer']//p[contains(text(), 'error')]"
    CLOSETECHNICALERRORBOX_XPATH = "//a[@title='Close']"

    """Class Constructor"""

    def __init__(self, driver):
        self.driver = driver

    """Common Function Which Can Used In This Class Or Outside If Needed"""
    """def return_list_of_elements(locator_type, by_locator):
        list = self.driver.find_elements(locator_type, by_locator)
        return list"""

    @staticmethod
    def select_by_value(by_locator, value):
        select = Select(by_locator)
        return select.select_by_value(value)

    @staticmethod
    def select_by_index(by_locator, value):
        select = Select(by_locator)
        return select.select_by_index(value)



    """Page Actions Used For Test Cases (This Can be Saved in a Different Class)"""

    def verify_form_title(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.NEWUSERACCOUNTFORMTITLE_XPATH)))
        actualText = self.driver.find_element(By.XPATH, self.NEWUSERACCOUNTFORMTITLE_XPATH).text
        formTitle = readConf.get_new_user_form_title()
        assert actualText.casefold() == formTitle.casefold()

    def select_mr_button(self):
        self.driver.find_element(By.XPATH, self.MALERADIOBUTTON_XPATH).click()

    def select_mrs_button(self):
        self.driver.find_element(By.XPATH, self.FEMALERADIOBUTTON_XPATH).click()

    def enter_first_name(self, fName):
        self.driver.find_element(By.ID, self.INPUTFIRSTNAME_ID).clear()
        self.driver.find_element(By.ID, self.INPUTFIRSTNAME_ID).send_keys(fName)

    def enter_last_name(self, lName):
        self.driver.find_element(By.ID, self.INPUTLASTNAME_ID).clear()
        self.driver.find_element(By.ID, self.INPUTLASTNAME_ID).send_keys(lName)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.INPUTPASSWORD_ID).clear()
        self.driver.find_element(By.ID, self.INPUTPASSWORD_ID).send_keys(password)

    def select_date(self, date):
        dateField = self.driver.find_element(By.ID, self.SELECTDAY_ID)
        """select = Select(dateField)
        select.select_by_value(date)"""
        self.select_by_index(dateField, date)

    def select_month(self, month):
        monthField = self.driver.find_element(By.ID, self.SELECTMONTH_ID)
        """select = Select(monthField)
        select.select_by_index(month)"""
        self.select_by_index(monthField, month)

    def select_year(self, year):
        yearField = self.driver.find_element(By.ID, self.SELECTYEAR_ID)
        """select = Select(yearField)
        select.select_by_value(year)"""
        self.select_by_value(yearField, year)

    def select_news_letters(self):
        self.driver.find_element(By.ID, self.NEWSLETTERCHECKBOX_ID).click()

    def select_offers(self):
        self.driver.find_element(By.ID, self.OFFERSCHECKBOX_ID).click()

    def enter_first_name_for_address(self, fName):
        self.driver.find_element(By.ID, self.INPUTFNAMEADDRESS_ID).clear()
        self.driver.find_element(By.ID, self.INPUTFNAMEADDRESS_ID).send_keys(fName)

    def enter_last_name_for_address(self, lName):
        self.driver.find_element(By.ID, self.INPUTLNAMEADDRESS_ID).clear()
        self.driver.find_element(By.ID, self.INPUTLNAMEADDRESS_ID).send_keys(lName)

    def enter_company_name(self, companyName):
        self.driver.find_element(By.ID, self.INPUTCOMPANYNAME_ID).clear()
        self.driver.find_element(By.ID, self.INPUTCOMPANYNAME_ID).send_keys(companyName)

    def enter_address_in_line_1(self, addressLine1):
        self.driver.find_element(By.ID, self.INPUTADDRESSLINE1_ID).clear()
        self.driver.find_element(By.ID, self.INPUTADDRESSLINE1_ID).send_keys(addressLine1)

    def enter_address_in_line_2(self, addressLine2):
        self.driver.find_element(By.ID, self.INPUTADDRESSLINE2_ID).clear()
        self.driver.find_element(By.ID, self.INPUTADDRESSLINE2_ID).send_keys(addressLine2)

    def enter_city(self, cityName):
        self.driver.find_element(By.ID, self.INPUTCITY_ID).clear()
        self.driver.find_element(By.ID, self.INPUTCITY_ID).send_keys(cityName)

    def select_state(self, state):
        stateDropdown = self.driver.find_element(By.ID, self.SELECTSTATE_ID)
        select = Select(stateDropdown)
        select.select_by_visible_text(state)

    def enter_zip_code(self, zipCode):
        self.driver.find_element(By.ID, self.INPUTZIPCODE_ID).clear()
        self.driver.find_element(By.ID, self.INPUTZIPCODE_ID).send_keys(zipCode)

    def enter_additional_info(self, info):
        self.driver.find_element(By.ID, self.INPUTADDINFOR_ID).clear()
        self.driver.find_element(By.ID, self.INPUTADDINFOR_ID).send_keys(info)

    def enter_home_phone(self, homePhone):
        self.driver.find_element(By.ID, self.INPUTHOMEPHONE_ID).clear()
        self.driver.find_element(By.ID, self.INPUTHOMEPHONE_ID).send_keys(homePhone)

    def enter_mobile_phone(self, mobilePhone):
        self.driver.find_element(By.ID, self.INPUTMOBILEPHONE_ID).clear()
        self.driver.find_element(By.ID, self.INPUTMOBILEPHONE_ID).send_keys(mobilePhone)

    def enter_address_alias(self, addressAlias):
        self.driver.find_element(By.ID, self.INPUTADDRESSALIAS_ID).clear()
        self.driver.find_element(By.ID, self.INPUTADDRESSALIAS_ID).send_keys(addressAlias)

    def click_on_register_account_button(self):
        self.driver.find_element(By.XPATH, self.REGISTERACCOUNTBUTTON_XPATH).click()

    def verify_phone_number_not_entered_error(self):
        list = self.driver.find_elements(By.XPATH, self.NOPHONENUMBERPROVIDEDERROR_XPATH)
        if len(list) == 0:
            assert False
        else:
            assert True

    def verify_last_name_required_error(self):
        list = self.driver.find_elements(By.XPATH, self.LNAMEREQUIREDERROR_XPATH)
        if len(list) == 0:
            assert False
        else:
            assert True

    def verify_first_name_require_error(self):
        list = self.driver.find_elements(By.XPATH, self.FNAMEREQUIREDERROR_XPATH)
        if len(list) == 0:
            assert False
        else:
            assert True

    def verify_email_required_error(self):
        list = self.driver.find_elements(By.XPATH, self.EMAILREQUIREDERROR_XPATH)
        if len(list) == 0:
            assert False
        else:
            assert True

    def verify_password_required_error(self):
        list = self.driver.find_elements(By.XPATH, self.PASSWORDREQUIREDERROR_XPATH)
        if len(list) == 0:
            assert False
        else:
            assert True

    def verify_address_alias_required_error(self):
        list = self.driver.find_elements(By.XPATH, self.ADDRESSALIASREQUIREDERROR_XPATH)
        if len(list) == 0:
            assert False
        else:
            assert True

    def verify_address_line1_required_error(self):
        list = self.driver.find_elements(By.XPATH, self.ADDRESSLINE1REQUIREDERROR_XPATH)
        if len(list) == 0:
            assert False
        else:
            assert True

    def verify_city_required_error(self):
        list = self.driver.find_elements(By.XPATH, self.CITYREQUIREDERROR_XPATH)
        if len(list) == 0:
            assert False
        else:
            assert True

    def verify_state_required_error(self):
        list = self.driver.find_elements(By.XPATH, self.STATEREQUIREDERROR_XPATH)
        if len(list) == 0:
            assert False
        else:
            assert True

    def verify_zip_code_required_error(self):
        list = self.driver.find_elements(By.XPATH, self.ZIPCODEREQUIREDERROR_XPATH)
        if len(list) == 0:
            assert False
        else:
            assert True

    def verify_technical_error_is_displayed(self):
        list = self.driver.find_elements(By.XPATH, self.TECHNICALERRORONLOGINPAGE_XPATH)
        if len(list) != 0:
            self.driver.find_element(By.XPATH, self.CLOSETECHNICALERRORBOX_XPATH).click()
        else:
            assert True

    def registering_new_user(self):
        self.rows = excelUtils.get_row_count(self.newUserExcel, self.sheet)
        list_status = []
        for r in range(2, self.rows + 1):
            self.gender = excelUtils.read_data(self.newUserExcel, self.sheet, r, 1)
            self.firstName = excelUtils.read_data(self.newUserExcel, self.sheet, r, 2)
            self.lastName = excelUtils.read_data(self.newUserExcel, self.sheet, r, 3)
            self.useremail = excelUtils.read_data(self.newUserExcel, self.sheet, r, 4)
            self.password = excelUtils.read_data(self.newUserExcel, self.sheet, r, 5)
            self.date = excelUtils.read_data(self.newUserExcel, self.sheet, r, 6)
            self.month = excelUtils.read_data(self.newUserExcel, self.sheet, r, 7)
            self.year = excelUtils.read_data(self.newUserExcel, self.sheet, r, 8)
            self.year_converted = str(self.year)
            self.fName = excelUtils.read_data(self.newUserExcel, self.sheet, r, 9)
            self.lName = excelUtils.read_data(self.newUserExcel, self.sheet, r, 10)
            self.company = excelUtils.read_data(self.newUserExcel, self.sheet, r, 11)
            self.addressLine1 = excelUtils.read_data(self.newUserExcel, self.sheet, r, 12)
            self.city = excelUtils.read_data(self.newUserExcel, self.sheet, r, 13)
            self.state = excelUtils.read_data(self.newUserExcel, self.sheet, r, 14)
            self.zip = excelUtils.read_data(self.newUserExcel, self.sheet, r, 15)
            self.addInfo = excelUtils.read_data(self.newUserExcel, self.sheet, r, 16)
            self.homePhone = excelUtils.read_data(self.newUserExcel, self.sheet, r, 17)
            self.mobilePhone = excelUtils.read_data(self.newUserExcel, self.sheet, r, 18)
            self.expectedResult = excelUtils.read_data(self.newUserExcel, self.sheet, r, 19)

            self.loginpage = LoginPage(self.driver)
            self.loginpage.enter_new_user_email(self.useremail)
            self.loginpage.click_create_account_button()

            self.verify_form_title()
            if self.gender == "Male":
                self.select_mr_button()
            else:
                self.select_mrs_button()

            self.enter_first_name(self.firstName)
            self.enter_last_name(self.lastName)
            self.enter_password(self.password)
            self.select_date(self.date)
            self.select_month(self.month)
            self.select_year(self.year_converted)

            self.select_news_letters()
            self.select_offers()

            self.enter_first_name_for_address(self.fName)
            self.enter_last_name_for_address(self.lName)
            self.enter_company_name(self.company)
            self.enter_address_in_line_1(self.addressLine1)
            self.enter_city(self.city)
            self.select_state(self.state)
            self.enter_zip_code(self.zip)
            self.enter_additional_info(self.addInfo)
            self.enter_home_phone(self.homePhone)
            self.enter_mobile_phone(self.mobilePhone)
            self.enter_address_alias("My Automated Test Alias")
            self.click_on_register_account_button()

            self.driver.implicitly_wait(5)

            if self.driver.title == readConf.get_my_account_page_title():
                if self.expectedResult == 'Pass':
                    self.loginpage.click_logout_button()
                    list_status.append('Pass')
                else:
                    list_status.append('Fail')
            elif self.driver.title != readConf.get_my_account_page_title():
                if self.expectedResult == 'Pass':
                    list_status.append('Fail')
                else:
                    list_status.append('Pass')

        assert 'Fail' not in list_status

