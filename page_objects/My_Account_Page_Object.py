from selenium.webdriver.common.by import By


class MyAccountPage:

    MYACCOUNTPAGELINK_XPATH = "//a[@title='View my customer account']"
    WISHLISTSPAGELINK_XPATH = "//span[normalize-space()='My wishlists']"

    def __init__(self, driver):
        self.driver = driver

    def go_to_my_account_page(self):
        self.driver.find_element(By.XPATH, self.MYACCOUNTPAGELINK_XPATH).click()

    def go_to_my_wishlists_page(self):
        self.driver.find_element(By.XPATH, self.WISHLISTSPAGELINK_XPATH).click()
