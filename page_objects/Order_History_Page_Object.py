from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderHistory:

    MOSTRECENTORDERREF_XPATH = "//tr[contains(@class,'first_item')]//td[@class='history_link bold footable-first-column']/a"

    def __init__(self, driver):
        self.driver = driver

    def get_most_recent_order_reference(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.MOSTRECENTORDERREF_XPATH)))
        element = self.driver.find_element(By.XPATH, self.MOSTRECENTORDERREF_XPATH)
        recentOrderRef = element.text
        return recentOrderRef