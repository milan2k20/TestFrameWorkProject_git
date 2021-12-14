import logging
import time

from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver
from Utilities.utils import Utils


class SearchFlightResult(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.WARNING)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    FILTER_BY_1_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    FILTER_BY_2_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    FILTER_BY_NON_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='0']"
    SEARCH_FLIGHT_RESULT = "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop(s)')]"

    def get_filter_by_one_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_1_STOP_ICON)

    def get_filter_by_two_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_2_STOP_ICON)

    def get_filter_by_non_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_NON_STOP_ICON)

    def get_search_flight_results(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.SEARCH_FLIGHT_RESULT)

    def filter_flights_by_stop(self, by_stop):
        if by_stop == '1 Stop':
            self.get_filter_by_one_stop_icon().click()
            self.log.warning('Selected flights by 1 stop')
            time.sleep(3)
        elif by_stop == '2 Stop(s)':
            self.get_filter_by_two_stop_icon().click()
            self.log.warning('Selected flights by 2 stop')
            time.sleep(3)
        elif by_stop == 'Non Stop':
            self.get_filter_by_non_stop_icon().click()
            self.log.warning('Selected flights by non stop')
            time.sleep(3)
        else:
            self.log.error('Please provide valid filter option')