import logging
import time
from Base.base_driver import BaseDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Pages.search_flight_resultpage import SearchFlightResult
from Utilities.utils import Utils


class SearchFlight(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.INFO)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    GOING_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    ORIGIN_DATE = "//input[@id='BE_flight_origin_date']"
    ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    RETURN_DATE = "//input[@id='BE_flight_arrival_date']"
    SEARCH_BUTTON = "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']"

    def get_going_from_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_FROM_FIELD)

    def enter_going_from_field(self, depart_location):
        self.get_going_from_field().click()
        time.sleep(2)
        self.get_going_from_field().send_keys(depart_location)
        time.sleep(2)
        self.get_going_from_field().send_keys(Keys.ENTER)
        self.log.info('Typed text into going from field successfully')
        time.sleep(2)

    def get_going_to_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)

    def enter_going_to_field(self, arrival_location):
        self.get_going_to_field().click()
        time.sleep(2)
        self.get_going_to_field().send_keys(arrival_location)
        time.sleep(2)
        self.get_going_to_field().send_keys(Keys.ENTER)
        self.log.info('Typed text into going to field successfully')
        time.sleep(2)

    def get_deparature_date_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ORIGIN_DATE)

    def enter_deparature_date_field(self, origin_date):
        self.get_deparature_date_field().click()
        time.sleep(2)
        all_dates = self.get_deparature_date_field().find_elements(By.XPATH, self.ALL_DATES)
        for date in all_dates:
            if date.get_attribute("data-date") == origin_date:
                date.click()
                time.sleep(2)
                break

    def get_arrival_date_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.RETURN_DATE)

    def enter_arrival_date_field(self, return_date):
        self.get_arrival_date_field().click()
        time.sleep(2)
        all_dates = self.get_deparature_date_field().find_elements(By.XPATH, self.ALL_DATES)
        for date in all_dates:
            if date.get_attribute("data-date") == return_date:
                date.click()
                time.sleep(2)
                break

    def get_search_flight_button(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SEARCH_BUTTON)

    def click_search_flight_button(self):
        self.get_search_flight_button().click()
        time.sleep(2)

    def search_flights(self, going_from, going_to, origin_date, return_date):
        self.enter_going_from_field(going_from)
        self.enter_going_to_field(going_to)
        self.enter_deparature_date_field(origin_date)
        self.enter_arrival_date_field(return_date)
        self.click_search_flight_button()
        flight_result_obj = SearchFlightResult(self.driver)
        return flight_result_obj