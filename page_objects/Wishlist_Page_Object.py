from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WishlistPage:

    DEFAULTNAMEDWISHLIST_XPATH = "//a[normalize-space()='My wishlist']"
    PRODUCTSINDEFAULTWISHLIST_XPATH = "//ul[@class='row wlp_bought_list']//p[@class='product-name'][contains(text(), '')]"

    def __init__(self, driver):
        self.driver = driver

    def click_on_deafult_named_wishlist(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.DEFAULTNAMEDWISHLIST_XPATH)))
        self.driver.find_element(By.XPATH, self.DEFAULTNAMEDWISHLIST_XPATH).click()

    def verify_product_is_displaying_in_wishlist(self, product):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//ul[@class='row wlp_bought_list']//p[@class='product-name'][contains(text(), '"+product+"')]")))
        list = self.driver.find_elements(
            By.XPATH, "//ul[@class='row wlp_bought_list']//p[@class='product-name'][contains(text(), '"+product+"')]")
        assert len(list) != 0
