from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.readProperties import readConf


class CheckoutPage:
    """BY LOCATORS OR OBJECT REPOSITORY"""
    CARTLINK_XPATH = "//a[@title='View my shopping cart']"
    FIRSTCARTITEMINPUT_XPATH = "//tr[contains(@class, 'first_item')]//input[@class='cart_quantity_input form-control grey']"
    LASTCARTITEMINPUT_XPATH = "//tr[contains(@class, 'last_item')]//input[@class='cart_quantity_input form-control grey']"
    TOTALCOSTOFALLINDIVIDUALITEMS_XPATH = "//span[contains(@id, 'total_product_price')]"
    TOTALPRODUCTSVALUE_ID = "total_product"
    TOTALSHIPPINGVALUE_ID = "total_shipping"
    TOTALVALUEBEFORETAX_ID = "total_price_without_tax"
    TOTALTAX_ID = "total_tax"
    TOTALVALUEAFTERTAX_ID = "total_price"
    DELIVERYADDRESSNAME_XPATH = "//ul[@class='address first_item item box']//span[@class='address_name']"
    DELIVERYADDRESS_XPATH = "//ul[@class='address first_item item box']//span[@class='address_address1']"
    DELIVERYCITY_XPATH = "//ul[@class='address first_item item box']//span[@class='address_city']"
    DELIEVRYCOUNTRY_XPATH = "//ul[@class='address first_item item box']//span[contains(text(),'United States')]"
    DELIVERYPHONENUMBER_XPATH = "//ul[@class='address first_item item box']//span[@class='address_phone_mobile']"
    INVOICENAME_XPATH = "//ul[@class='address last_item alternate_item box']//span[@class='address_name']"
    INVOICEADDRESS_XPATH = "//ul[@class='address last_item alternate_item box']//span[@class='address_address1']"
    INVOICECITY_XPATH = "//ul[@class='address last_item alternate_item box']//span[@class='address_city']"
    INVOICECOUNTRY_XPATH = "//ul[@class='address last_item alternate_item box']//span[contains(text(),'United States')]"
    INVOICEPHONENUMBER_XPATH = "//ul[@class='address last_item alternate_item box']//span[@class='address_phone_mobile']"
    COUNTINUESHOPPINGBUTTON_CLASSNAME = "button-exclusive btn btn-default"
    PROCEEDTOADDRESS_XPATH = "//p[@class='cart_navigation clearfix']//span[contains(text(), 'Proceed to checkout')]"
    TOTALPRODUCTSINCART_XPATH = "//span[@id='summary_products_quantity']"
    TOTALPRODUCTSDESCRIPTIONINCART_XPATH = "//tr[contains(@id, 'product')]//td[@class='cart_product']"
    HOMEICON_CLASSNAME = "icon-home"
    SELECTDELIEVRYADDRESS_ID = "id_address_delivery"
    SAMEBILLINGANDDELIVERYADDRESSCHECKBOX_XPATH = "//input[@id='addressesAreEquals']"
    UPDATEDELIVERYADDRESS_CSS = "ul[id='address_delivery'] span"
    UPDATEBILLINGADDRESS_CSS = "ul[id='address_invoice'] span"
    ADDNEWADDRESSHIDDEN_CSS = "div[id='address_invoice_form'] span"
    ADDNEWADDRESSPERM_CSS = "p[class='address_add submit'] span"
    ADDCOMMENTS_NAME = "message"
    PROCEEDTOSHIPPING_CSS = "button[name='processAddress'] span"
    SHIPPINGCHARGES_CSS = "div[class='delivery_option_price']"
    AGREETERMSBUTTON_CSS = "#cgv"
    PROCEEDTOPAYMENT_CSS = "button[name='processCarrier'] span"
    MUSTAGREETERMSERROR_CLASSNAME = "fancybox-error"
    CLOSEMUSTAGREETERMSERROR_CLASSNAME = "fancybox-item fancybox-close"
    TOTALPRICE_ID = "total_price"
    BANKWIRELINK_XPATH = "//a[@title='Pay by bank wire']"
    CHEQUELINK_CLASSNAME = "cheque"
    BANKWIRECONFIRMATIONHEADING_CLASSNAME = "page-subheading"
    CHEQUECONFIRMATIONHEADING_CLASSNAME = "page-subheading"
    ORDERCONFIRMATIONBUTTON_CSS = "button[class='button btn btn-default button-medium'] span"
    CHANGEPAYMENTTYPE_XPATH = "//a[normalize-space()='Other payment methods']"
    CONFIRMATIONOFORDER_CLASSNAME = "alert alert-success"
    BACKTOORDERS_CSS = "a[title='Back to orders']"
    EMPTYCARTALERT_XPATH = "//p[@class='alert alert-warning'][contains(text(), 'shopping cart is empty')]"
    CARTNOTEMPTY_XPATH = "//span[@class='heading-counter'][contains(text(), 'cart contains')]"
    USERISATADDRESSSTEP_XPATH = "//label[normalize-space()='Choose a delivery address:']"
    USERISATSHIPPINGSTEP_XPATH = "//p[contains(text(),'Choose a shipping')]"
    PROCEEDTOSIGNIN_XPATH = "(//span[contains(text(),'Proceed to checkout')])[2]"
    FIRSTITEMUNITPRICEINCART_XPATH = "//tr[contains(@class, 'first_item')]/td/span/span"
    TOTALPRICEFORFIRSTITEMINCART_XPATH = "//tr[contains(@class, 'first_item')]/td/span[contains(@id, 'total_product_price')]"
    COMMONPRODUCTLINKINCART_XPATH = "//a[contains(text(),'Color : Yellow, Size : M')]/parent::small/parent::td//small[@class='cart_ref'][contains(text(), '')]"
    COMMONUNITSPECIALPRICELINKINCART_XPATH = "//a[contains(text(),'Color : Yellow, Size : M')]/parent::small/parent::td//small[@class='cart_ref'][contains(text(), '')]/ancestor::tr//span[contains(@class, 'special')]"
    COMMONTOTALPRODUCTPRICELINKINCART_XPATH = "//a[contains(text(),'Color : Yellow, Size : M')]/parent::small/parent::td//small[@class='cart_ref'][contains(text(), '')]/ancestor::tr//span[contains(@id, 'total')]"
    COMMONUNITPRICELINKINCART_XPATH = "//a[contains(text(),'S')]/parent::small/parent::td//small[@class='cart_ref'][contains(text(), '')]/ancestor::tr//span[@class='price']/span[@class='price']"
    FIRSTNAMEINUPDATEFORM_CSS = "#firstname"
    LASTNAMEINUPDATEFORM_CSS = "#lastname"
    COMPANYINUPDATEFORM_CSS = "#company"
    ADDRESSLINE1INUPDATEFORM_CSS = "#address1"
    ADDRESSLINE2INUPDATEFORM_CSS = "#address2"
    CITYINUPDATEFORM_CSS = "#city"
    STATEINUPDATEFORM_CSS = "#id_state"
    ZIPINUPDATEFORM_CSS = "#postcode"
    HOMEPHONEINUPDATEFORM_CSS = "#phone"
    MOBILEPHONEINUPDATEFORM_CSS = "#phone_mobile"
    ADDITIONALINFOINUPDATEFOR_CSS = "#other"
    ALIASINUPDATEFORM_CSS = "#alias"
    SAVEBUTTONINUPDATEFORM_CSS = "button[id='submitAddress'] span"
    BACKBUTTONINUPDATEFORM_CSS = "a[class='btn btn-defaul button button-small'] span"
    CHOOSEDELIVERYADDRESS_XPATH = "//select[@id='id_address_delivery']"
    CHOOSEBILLINGADDRESS_XPATH = "//select[@id='id_address_invoice']"
    TOTALPRODUCTSAMOUNTATPAYMENT_CSS = "#total_product"
    TOTALORDERAMOUNTATPAYMENT_CSS = "#total_price"
    ORDERREFERENCEONCONFIRMATIONPAGE_XPATH = "//div[@class='box order-confirmation']"


    def __init__(self, driver):
        self.driver = driver

    def go_to_checkout_page(self):
        self.driver.find_element(By.XPATH, self.CARTLINK_XPATH).click()

    def verify_cart_is_empty(self):
        list = self.driver.find_elements(By.XPATH, self.EMPTYCARTALERT_XPATH)
        assert len(list) != 0

    def verify_cart_is_not_empty(self):
        list = self.driver.find_elements(By.XPATH, self.CARTNOTEMPTY_XPATH)
        assert len(list) != 0

    def get_total_products_price(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.TOTALPRODUCTSVALUE_ID)))
        element = self.driver.find_element(By.ID, self.TOTALPRODUCTSVALUE_ID)
        price = element.text
        totalProductsPrice = price[1:]
        return float(totalProductsPrice)

    def get_shipping_price(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.TOTALSHIPPINGVALUE_ID)))
        element = self.driver.find_element(By.ID, self.TOTALSHIPPINGVALUE_ID)
        price = element.text
        shippingAmount = price[1:]
        return float(shippingAmount)

    def get_total_amount_before_tax(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.TOTALVALUEBEFORETAX_ID)))
        element = self.driver.find_element(By.ID, self.TOTALVALUEBEFORETAX_ID)
        price = element.text
        beforeTax = price[1:]
        return float(beforeTax)

    def verify_total_amount_before_tax(self):
        productCosts = self.get_total_products_price()
        shippingCosts = self.get_shipping_price()
        totalBeforeTax = productCosts + shippingCosts
        beforeTaxAmount = self.get_total_amount_before_tax()
        assert totalBeforeTax == beforeTaxAmount

    def get_tax_amount(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.TOTALTAX_ID)))
        element = self.driver.find_element(By.ID, self.TOTALTAX_ID)
        price = element.text
        tax = price[1:]
        return float(tax)

    def get_total_amount_after_tax(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.TOTALVALUEAFTERTAX_ID)))
        element = self.driver.find_element(By.ID, self.TOTALVALUEAFTERTAX_ID)
        price = element.text
        afterTax = price[1:]
        return float(afterTax)

    def verify_amount_after_tax(self):
        beforeTaxAmount = self.get_total_amount_before_tax()
        taxAmount = self.get_tax_amount()
        sumOfBeforeTaxAndTax = beforeTaxAmount + taxAmount
        afterTaxAmount = self.get_total_amount_after_tax()
        assert sumOfBeforeTaxAndTax == afterTaxAmount

    def click_on_proceed_to_address_step(self):
        self.driver.find_element(By.XPATH, self.PROCEEDTOADDRESS_XPATH).click()

    def click_on_proceed_to_shipping_step(self):
        self.driver.find_element(By.CSS_SELECTOR, self.PROCEEDTOSHIPPING_CSS).click()

    def click_to_agree_terms_on_shipping_step(self):
        self.driver.find_element(By.ID, self.AGREETERMSBUTTON_CSS).click()

    def click_on_proceed_to_payment_step(self):
        self.driver.find_element(By.CSS_SELECTOR, self.PROCEEDTOPAYMENT_CSS).click()

    def click_on_pay_by_bank_wire_link(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.BANKWIRELINK_XPATH)))
        self.driver.find_element(By.XPATH, self.BANKWIRELINK_XPATH).click()

    def click_on_pay_by_cheque_link(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.CHEQUELINK_CLASSNAME)))
        self.driver.find_element(By.CLASS_NAME, self.CHEQUELINK_CLASSNAME).click()

    def click_to_change_payment_type(self):
        self.driver.find_element(By.XPATH, self.CHANGEPAYMENTTYPE_XPATH).click()

    def click_on_order_confirm_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.ORDERCONFIRMATIONBUTTON_CSS).click()

    def verify_user_is_at_address_step(self):
        list = self.driver.find_elements(By.XPATH, self.USERISATADDRESSSTEP_XPATH)
        assert len(list) != 0

    def verify_user_is_at_shipping_step(self):
        list = self.driver.find_elements(By.XPATH, self.USERISATSHIPPINGSTEP_XPATH)
        assert len(list) != 0

    def proceed_to_signin_step(self):
        self.driver.find_element(By.XPATH, self.PROCEEDTOSIGNIN_XPATH).click()

    def get_unit_price_of_product_in_cart(self):
        element = self.driver.find_element(By.XPATH, self.FIRSTITEMUNITPRICEINCART_XPATH)
        price = element.text
        unitPrice = price[1:]
        return float(unitPrice)

    def get_total_price_of_a_product(self):
        element = self.driver.find_element(By.XPATH, self.TOTALPRICEFORFIRSTITEMINCART_XPATH)
        price = element.text
        totalPrice = price[1:]
        return float(totalPrice)

    def get_unit_price_for_a_product(self, color, size, productIdentifier):
        element = self.driver.find_element(By.XPATH,
                                           "//a[contains(text(),'Color : "+color+", Size : "+size+"')]/parent::small/parent::td//small[@class='cart_ref'][contains(text(), '" + productIdentifier + "')]/ancestor::tr//span[@class='price']/span[@class='price']")
        price = element.text
        unitPrice = price[1:]
        return float(unitPrice)

    def get_unit_price_for_a_discounted_product(self, color, size, productIdentifier):
        element = self.driver.find_element(By.XPATH,
                                           "//a[contains(text(),'Color : "+color+", Size : "+size+"')]/parent::small/parent::td//small[@class='cart_ref'][contains(text(), '" + productIdentifier + "')]/ancestor::tr//span[contains(@class, 'special')]")
        price = element.text
        discountedPrice = price[1:]
        return float(discountedPrice)

    def get_total_unit_costs(self, color, size, productIdentifier):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Color : "+color+", Size : "+size+"')]/parent::small/parent::td//small[@class='cart_ref'][contains(text(), '"+productIdentifier+"')]/ancestor::tr//span[contains(@id, 'total')]")))
        element = self.driver.find_element(By.XPATH, "//a[contains(text(),'Color : "+color+", Size : "+size+"')]/parent::small/parent::td//small[@class='cart_ref'][contains(text(), '"+productIdentifier+"')]/ancestor::tr//span[contains(@id, 'total')]")
        price = element.text
        totalCosts = price[1:]
        return float(totalCosts)

    def get_number_of_products_in_cart(self):
        element = self.driver.find_element(By.XPATH, self.CARTNOTEMPTY_XPATH)
        numberOfProductsInCart = element.text
        return numberOfProductsInCart

    def compare_user_name_at_address_step(self):
        element1 = self.driver.find_element(By.CSS_SELECTOR, "ul[id='address_delivery'] li[class='address_firstname address_lastname']")
        deliveryUserName = element1.text
        element2 = self.driver.find_element(By.CSS_SELECTOR, "ul[id='address_invoice'] li[class='address_firstname address_lastname']")
        billingUserName = element2.text
        assert deliveryUserName == billingUserName

    def compare_address_at_address_step(self):
        element1 = self.driver.find_element(By.CSS_SELECTOR, "ul[id='address_delivery'] li[class='address_address1 address_address2']")
        delievryAddress = element1.text
        element2 = self.driver.find_element(By.CSS_SELECTOR, "ul[id='address_invoice'] li[class='address_address1 address_address2']")
        billingUserName = element2.text
        assert delievryAddress == billingUserName

    def compare_phone_number_at_address_step(self):
        element1 = self.driver.find_element(By.CSS_SELECTOR, "ul[id='address_delivery'] li[class='address_phone_mobile']")
        phoneNumberDelivery = element1.text
        element2 = self.driver.find_element(By.CSS_SELECTOR, "ul[id='address_invoice'] li[class='address_phone_mobile']")
        phoneNumberBilling = element2.text
        assert phoneNumberBilling == phoneNumberDelivery

    def click_to_update_delivery_address(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.UPDATEDELIVERYADDRESS_CSS)))
        self.driver.find_element(By.CSS_SELECTOR, self.UPDATEDELIVERYADDRESS_CSS).click()
        self.driver.find_element(By.CSS_SELECTOR, self.ADDRESSLINE1INUPDATEFORM_CSS).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.ADDRESSLINE1INUPDATEFORM_CSS).send_keys(readConf.get_address_for_update())
        self.driver.find_element(By.CSS_SELECTOR, self.CITYINUPDATEFORM_CSS).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.CITYINUPDATEFORM_CSS).send_keys(readConf.get_city_for_update())
        state = self.driver.find_element(By.CSS_SELECTOR, self.STATEINUPDATEFORM_CSS)
        select = Select(state)
        select.select_by_visible_text(readConf.get_state_for_update())
        self.driver.find_element(By.CSS_SELECTOR, self.ZIPINUPDATEFORM_CSS).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.ZIPINUPDATEFORM_CSS).send_keys(readConf.get_zip_for_update())
        self.driver.find_element(By.CSS_SELECTOR, self.HOMEPHONEINUPDATEFORM_CSS).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.HOMEPHONEINUPDATEFORM_CSS).send_keys(readConf.get_home_phone_for_update())
        self.driver.find_element(By.CSS_SELECTOR, self.MOBILEPHONEINUPDATEFORM_CSS).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.MOBILEPHONEINUPDATEFORM_CSS).send_keys(readConf.get_mobile_phone_for_update())
        self.driver.find_element(By.CSS_SELECTOR, self.ALIASINUPDATEFORM_CSS).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.ALIASINUPDATEFORM_CSS).send_keys(readConf.get_addressalias_for_update())
        self.driver.find_element(By.CSS_SELECTOR, self.SAVEBUTTONINUPDATEFORM_CSS).click()

    def click_to_update_billing_address(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.UPDATEBILLINGADDRESS_CSS)))
        self.driver.find_element(By.CSS_SELECTOR, self.UPDATEBILLINGADDRESS_CSS).click()
        self.driver.find_element(By.CSS_SELECTOR, self.ADDRESSLINE1INUPDATEFORM_CSS).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.ADDRESSLINE1INUPDATEFORM_CSS).send_keys(readConf.get_address_for_update())
        self.driver.find_element(By.CSS_SELECTOR, self.CITYINUPDATEFORM_CSS).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.CITYINUPDATEFORM_CSS).send_keys(readConf.get_city_for_update())
        state = self.driver.find_element(By.CSS_SELECTOR, self.STATEINUPDATEFORM_CSS)
        select = Select(state)
        select.select_by_visible_text(readConf.get_state_for_update())
        self.driver.find_element(By.CSS_SELECTOR, self.ZIPINUPDATEFORM_CSS).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.ZIPINUPDATEFORM_CSS).send_keys(readConf.get_zip_for_update())
        self.driver.find_element(By.CSS_SELECTOR, self.HOMEPHONEINUPDATEFORM_CSS).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.HOMEPHONEINUPDATEFORM_CSS).send_keys(readConf.get_home_phone_for_update())
        self.driver.find_element(By.CSS_SELECTOR, self.MOBILEPHONEINUPDATEFORM_CSS).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.MOBILEPHONEINUPDATEFORM_CSS).send_keys(readConf.get_mobile_phone_for_update())
        self.driver.find_element(By.CSS_SELECTOR, self.ALIASINUPDATEFORM_CSS).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.ALIASINUPDATEFORM_CSS).send_keys(readConf.get_addressalias_for_update())
        self.driver.find_element(By.CSS_SELECTOR, self.SAVEBUTTONINUPDATEFORM_CSS).click()

    def click_to_make_billing_and_delivery_address_different(self):
        self.driver.find_element(By.XPATH, self.SAMEBILLINGANDDELIVERYADDRESSCHECKBOX_XPATH).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.ADDNEWADDRESSHIDDEN_CSS)))
        self.driver.find_element(By.CSS_SELECTOR, self.ADDNEWADDRESSHIDDEN_CSS).click()
        self.driver.find_element(By.CSS_SELECTOR, self.ADDRESSLINE1INUPDATEFORM_CSS).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.ADDRESSLINE1INUPDATEFORM_CSS).send_keys(readConf.get_address_for_update())
        self.driver.find_element(By.CSS_SELECTOR, self.CITYINUPDATEFORM_CSS).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.CITYINUPDATEFORM_CSS).send_keys(readConf.get_city_for_update())
        state = self.driver.find_element(By.CSS_SELECTOR, self.STATEINUPDATEFORM_CSS)
        select = Select(state)
        select.select_by_visible_text(readConf.get_state_for_update())
        self.driver.find_element(By.CSS_SELECTOR, self.ZIPINUPDATEFORM_CSS).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.ZIPINUPDATEFORM_CSS).send_keys(readConf.get_zip_for_update())
        self.driver.find_element(By.CSS_SELECTOR, self.HOMEPHONEINUPDATEFORM_CSS).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.HOMEPHONEINUPDATEFORM_CSS).send_keys(readConf.get_home_phone_for_update())
        self.driver.find_element(By.CSS_SELECTOR, self.MOBILEPHONEINUPDATEFORM_CSS).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.MOBILEPHONEINUPDATEFORM_CSS).send_keys(readConf.get_mobile_phone_for_update())
        self.driver.find_element(By.CSS_SELECTOR, self.ALIASINUPDATEFORM_CSS).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.ALIASINUPDATEFORM_CSS).send_keys(readConf.get_addressalias_for_update())
        self.driver.find_element(By.CSS_SELECTOR, self.SAVEBUTTONINUPDATEFORM_CSS).click()

    def verify_delivery_address_update(self):
        element1 = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul[id='address_delivery'] li[class='address_address1 address_address2']")
        delievryAddress = element1.text
        updatedAddress = readConf.get_address_for_update()
        assert delievryAddress == updatedAddress

    def verify_delivery_mobile_number_update(self):
        element1 = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul[id='address_delivery'] li[class='address_phone_mobile']")
        phoneNumberDelivery = element1.text
        updatedPhoneNumber = readConf.get_mobile_phone_for_update()
        assert phoneNumberDelivery == updatedPhoneNumber

    def verify_delivery_state_update(self):
        element1 = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul[id='address_delivery'] li[class='address_city address_state_name address_postcode']")
        state = element1.text
        updatedState = readConf.get_state_for_update()
        assert updatedState in state

    def verify_delivery_city_update(self):
        element1 = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul[id='address_delivery'] li[class='address_city address_state_name address_postcode']")
        city = element1.text
        updatedCity = readConf.get_city_for_update()
        assert updatedCity in city

    def verify_delivery_home_number_update(self):
        element1 = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul[id='address_delivery'] li[class='address_phone']")
        homephone = element1.text
        updatedHomeNumber = readConf.get_home_phone_for_update()
        assert updatedHomeNumber == homephone

    def verify_delivery_zip_code_update(self):
        element1 = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul[id='address_delivery'] li[class='address_city address_state_name address_postcode']")
        zip = element1.text
        updatedZip = readConf.get_zip_for_update()
        assert updatedZip in zip

    def verify_billing_address_update(self):
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           "ul[id='address_invoice'] li[class='address_address1 address_address2']")
        address = element.text
        updtedAddress = readConf.get_address_for_update()
        assert updtedAddress == address

    def verify_billing_mobile_number(self):
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           "ul[id='address_invoice'] li[class='address_phone_mobile']")
        mobile = element.text
        updatedMobile = readConf.get_mobile_phone_for_update()
        assert updatedMobile == mobile

    def verify_billing_state(self):
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           "ul[id='address_invoice'] li[class='address_city address_state_name address_postcode']")
        state = element.text
        updatedState = readConf.get_state_for_update()
        assert updatedState in state

    def verify_billing_city(self):
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           "ul[id='address_invoice'] li[class='address_city address_state_name address_postcode']")
        city = element.text
        updatedCity = readConf.get_city_for_update()
        assert updatedCity in city

    def verify_billing_zip(self):
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           "ul[id='address_invoice'] li[class='address_city address_state_name address_postcode']")
        zip = element.text
        updatedZip = readConf.get_zip_for_update()
        assert updatedZip in zip

    def verify_billing_home_phone(self):
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           "ul[id='address_invoice'] li[class='address_phone']")
        homephone = element.text
        updatedHomePhone = readConf.get_home_phone_for_update()
        assert updatedHomePhone == homephone

    def click_on_agree_terms_checkbox_at_shipping_step(self):
        self.driver.find_element(By.CSS_SELECTOR, self.AGREETERMSBUTTON_CSS).click()

    def click_on_proceed_to_payment(self):
        self.driver.find_element(self.PROCEEDTOPAYMENT_CSS).click()
        """list = self.driver.find_elements(By.CLASS_NAME, self.MUSTAGREETERMSERROR_CLASSNAME)
        if len(list) != 0:
            self.driver.find_element(By.CLASS_NAME, self.CLOSEMUSTAGREETERMSERROR_CLASSNAME).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, self.AGREETERMSBUTTON_CSS)))
            self.driver.find_element(By.CSS_SELECTOR, self.AGREETERMSBUTTON_CSS).click()
        else:
            assert True"""

    def verify_unit_price_of_product_at_payment_page(self, color, size, productIdentifier):
        element = self.driver.find_element(By.XPATH,
                                           "//a[contains(text(),'Color : " + color + ", Size : " + size + "')]/parent::small/parent::td//small[@class='cart_ref'][contains(text(), '" + productIdentifier + "')]/ancestor::tr//span[@class='price']/span[@class='price']")
        price = element.text
        totalPerUnitPriceAtPayment = price[1:]
        return float(totalPerUnitPriceAtPayment)

    def verify_product_quanity_at_payment_page(self, color, size, productIdentifier):
        element = self.driver.find_element(By.XPATH,
                                           "//a[contains(text(),'Color : "+color+", Size : "+size+"')]/parent::small/parent::td//small[@class='cart_ref'][contains(text(), '"+productIdentifier+"')]/ancestor::tr//td[@class='cart_quantity text-center']/span")
        quantity = element.text
        assert quantity == readConf.get_product_quanity()

    def verify_product_total_amount_at_payment_page(self, color, size, productIdentifier):
        element = self.driver.find_element(By.XPATH,
                                           "//a[contains(text(),'Color : " + color + ", Size : " + size + "')]/parent::small/parent::td//small[@class='cart_ref'][contains(text(), '" + productIdentifier + "')]/ancestor::tr//span[contains(@id, 'total')]")
        price = element.text
        totalProductAmountAtPayment = price[1:]
        return float(totalProductAmountAtPayment)

    def verify_total_amount_of_all_products_at_payment_page(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.TOTALPRODUCTSAMOUNTATPAYMENT_CSS)
        price = element.text
        totalProductsPriceAtPayment = price[1:]
        return float(totalProductsPriceAtPayment)

    def verify_total_amount_of_order_at_payment_page(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.TOTALORDERAMOUNTATPAYMENT_CSS)
        price = element.text
        totalOrderValueAtPayment = price[1:]
        return float(totalOrderValueAtPayment)

    def order_reference_on_confirmation_page(self):
        element = self.driver.find_element(By.XPATH, self.ORDERREFERENCEONCONFIRMATIONPAGE_XPATH)
        orderRef = element.text
        return orderRef

    def back_to_orders_page_from_confirmation_page(self):
        self.driver.find_element(By.CSS_SELECTOR, self.BACKTOORDERS_CSS).click()

    def verify_cheque_payment_heading(self):
        element = self.driver.find_element(By.CLASS_NAME, self.CHEQUECONFIRMATIONHEADING_CLASSNAME)
        heading = element.text
        return heading

    def verify_bank_wire_payment_heading(self):
        element = self.driver.find_element(By.CLASS_NAME, self.BANKWIRECONFIRMATIONHEADING_CLASSNAME)
        heading = element.text
        return heading