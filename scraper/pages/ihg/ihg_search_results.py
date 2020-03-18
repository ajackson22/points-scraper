from scraper.framework.driver_navigation import driver_navigation
from scraper.model.hotel import Hotel
from scraper.pages.ihg.ihg_homepage import ihg_homepage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IhgSearchResults():
    instance = None
    hotels_list = {}

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = IhgSearchResults()
        return cls.instance

    def __init__(self):
        self.driver = driver_navigation.get_driver()

    def change_currency(self, selector):
        if selector == "cash":
            selector_btn = self.driver.find_element_by_xpath(
                '//hotel-payment-type-selector/div/div[@data-slnm-ihg="cashFilterButton"]')
        elif selector == "points":
            selector_btn = self.driver.find_element_by_xpath(
                '//hotel-payment-type-selector/div/div[@data-slnm-ihg="pointsFilterButton"]')
        elif selector == "mixed":
            selector_btn = self.driver.find_element_by_xpath(
                '//hotel-payment-type-selector/div/div[@data-slnm-ihg="cashPointsFilterButton"]')
        else:
            return
        self.driver.execute_script("arguments[0].click();", selector_btn)

    def collect_hotel_grid_info(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//div[@data-slnm-ihg=\"numberOfHotelsInList\"]")))
        hotel_offerings = self.driver.find_elements_by_xpath("//hotel-offer")
        for hotel_offering in hotel_offerings:
            self.gather_hotel_info(hotel_offering)

    def gather_hotel_info(self, hotel_offering):
        name = hotel_offering.find_element_by_xpath(
            './/span[@data-slnm-ihg="hotelName"]').text + " " + hotel_offering.find_element_by_xpath(
            './/span[@data-slnm-ihg="hotelBrand"]').text
        if name in self.hotels_list:
            try:
                cost_in_points = hotel_offering.find_element_by_xpath(
                    './/hotel-offer-price//span[@data-slnm-ihg="dailyPointsCost"]').text
            except NoSuchElementException:
                cost_in_points = None
            self.hotels_list.get(name).cost_in_points = cost_in_points
        else:
            try:
                cost_in_usd = hotel_offering.find_element_by_xpath(
                    './/hotel-offer-price//span[@data-slnm-ihg="rateValue"]').text + '.' + hotel_offering.find_element_by_xpath(
                    './/hotel-offer-price//sup[@data-slnm-ihg="rateDecimalValue"]').text
            except NoSuchElementException:
                cost_in_usd = None
            hotel = Hotel(name=name, brand="IHG", location=ihg_homepage.location, cost_in_usd=cost_in_usd,
                          cost_in_points=None,
                          point_valuation=None)
            self.hotels_list[name] = hotel

    def calculate_valuations(self):
        for hotel in self.hotels_list:
            if self.hotels_list.get(hotel).cost_in_points is not None and self.hotels_list.get(
                    hotel).cost_in_usd is not None:
                self.hotels_list.get(hotel).point_valuation = float(
                    self.hotels_list.get(hotel).cost_in_usd.replace(',', '')) / float(self.hotels_list.get(
                    hotel).cost_in_points.replace(',', ''))

    def show_list(self):
        for hotel in self.hotels_list:
            print(self.hotels_list[hotel])


ihg_search_results = IhgSearchResults.get_instance()
