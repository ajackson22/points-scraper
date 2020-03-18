from scraper.framework.driver_navigation import driver_navigation
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IhgHomepage():
    instance = None
    location = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = IhgHomepage()
        return cls.instance

    def __init__(self):
        self.driver = driver_navigation.get_driver()

    def close_popup(self):
        try:
            # COVID-19 popup
            popup = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "featherlight"))
            )
            self.driver.execute_script("arguments[0].style.visibility='hidden'", popup)

            # Cookies popup
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "truste-consent-button")))
            self.driver.find_element_by_id("truste-consent-button").click()
        except NoSuchElementException:
            return  # popup does not exist

    def hotel_search_by_city(self, city):
        self.location = city
        destination_input = self.driver.find_element_by_name("destination")
        destination_input.send_keys(city)
        search_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Search')]")))
        search_btn.click()


ihg_homepage = IhgHomepage.get_instance()
