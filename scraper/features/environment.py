from scraper.framework.driver_navigation import  driver_navigation

def after_all(context):
    driver_navigation.close()