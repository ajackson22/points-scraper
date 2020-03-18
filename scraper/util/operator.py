from scraper.framework.driver_navigation import driver_navigation
from scraper.pages.ihg.ihg_homepage import ihg_homepage
from scraper.pages.ihg.ihg_search_results import ihg_search_results
from scraper.util.config import settings


class Operator(object):
    instance = None
    brand = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Operator()
        return cls.instance

    def __init__(self):
        self.driver = driver_navigation.get_driver()

    def navigate_to(self):
        if self.brand == "IHG":
            driver_navigation.get_driver().get(str(settings['ihg_homepage']))
            ihg_homepage.close_popup()

    def search(self, location):
        if self.brand == "IHG":
            ihg_homepage.hotel_search_by_city(location)

    def scrap(self):
        if self.brand == "IHG":
            ihg_search_results.collect_hotel_grid_info()

    def change_currency(self, currency):
        if self.brand == "IHG":
            ihg_search_results.change_currency(currency)

    def calculate_valuation(self):
        if self.brand == "IHG":
            ihg_search_results.calculate_valuations()

    def show(self):
        if self.brand == "IHG":
            ihg_search_results.show_list()

    def best_award(self):
        if self.brand == "IHG":
            best = next(iter(ihg_search_results.hotels_list))
            for hotel in ihg_search_results.hotels_list:
                if ihg_search_results.hotels_list.get(hotel).point_valuation is not None:
                    if ihg_search_results.hotels_list.get(
                            best).point_valuation is None or ihg_search_results.hotels_list.get(
                            hotel).point_valuation > ihg_search_results.hotels_list.get(best).point_valuation:
                        best = hotel
            print("Best Hotel Option: ")
            print(ihg_search_results.hotels_list.get(best))


operator = Operator.get_instance()
