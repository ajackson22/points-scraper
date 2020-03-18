from selenium.webdriver.common.by import By

# IHG Locators
class IHGMainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = IHGMainPageLocators()
        return cls.instance

    DESTINATION_INPUT = (By.NAME, 'destination')
    RATE_PREFERENCE = (By.NAME, 'ratePreference')
    SEARCH_BTN = (By.XPATH, "(\"//div[contains(text(), 'Search')]\")")


ihg_locators = IHGMainPageLocators.get_instance()