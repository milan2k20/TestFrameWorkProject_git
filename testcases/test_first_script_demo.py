import logging
import pytest
import softest
from ddt import ddt, unpack, data, file_data
from Pages.yatra_homepage import SearchFlight
from Utilities.utils import Utils


@pytest.mark.usefixtures("set_up_browser")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):
    log = Utils.custom_logger(logLevel=logging.INFO)

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.search_flight_obj = SearchFlight(self.driver)
        self.utils_obj = Utils()

# Run testcase with multiple data by using tuple

    @data(("GOI", "Mumbai", "10/01/2022", "20/02/2022", "Non Stop"), ("Chennai", "HYD", "14/01/2022", "25/02/2022", "Non Stop"))
    @unpack
    def test_search_flight(self, going_from, going_to, origin_date, return_date, stop):
        search_flight_result = self.search_flight_obj.search_flights(going_from, going_to, origin_date, return_date)
        self.search_flight_obj.dynamic_page_scroll()
        search_flight_result.filter_flights_by_stop(stop)
        all_stops = search_flight_result.get_search_flight_results()
        self.log.info(len(all_stops))
        self.utils_obj.assert_list_item_text(all_stops, stop)

# Run testcase with multiple data by using a json or yaml file

    '''@file_data("E:\\Selenium Project\\TestFrameworkDemo\\TestData\\Demo_testData.yaml")
    def test_search_flight(self, going_from, going_to, origin_date, return_date, stop):
        search_flight_result = self.search_flight_obj.search_flights(going_from, going_to, origin_date, return_date)
        self.search_flight_obj.dynamic_page_scroll()
        search_flight_result.filter_flights_by_stop(stop)
        all_stops = search_flight_result.get_search_flight_results()
        self.log.info(len(all_stops))
        self.utils_obj.assert_list_item_text(all_stops, stop)'''

    # Run testcase with multiple data by using Excel file

    '''@data(*Utils.read_data_from_excelfile("E:\Selenium Project\TestFrameworkDemo\TestData\TestDataDemo.xlsx", "Sheet1"))
    @unpack
    def test_search_flight(self, going_from, going_to, origin_date, return_date, stop):
        search_flight_result = self.search_flight_obj.search_flights(going_from, going_to, origin_date, return_date)
        self.search_flight_obj.dynamic_page_scroll()
        search_flight_result.filter_flights_by_stop(stop)
        all_stops = search_flight_result.get_search_flight_results()
        self.log.info(len(all_stops))
        self.utils_obj.assert_list_item_text(all_stops, stop)'''


# Run testcase with multiple data by using CSV file

    '''@data(*Utils.read_data_from_csvfile("E:\\Selenium Project\\TestFrameworkDemo\\TestData\\dummy_TestData.csv"))
    @unpack
    def test_search_flight(self, going_from, going_to, origin_date, return_date, stop):
        search_flight_result = self.search_flight_obj.search_flights(going_from, going_to, origin_date, return_date)
        self.search_flight_obj.dynamic_page_scroll()
        search_flight_result.filter_flights_by_stop(stop)
        all_stops = search_flight_result.get_search_flight_results()
        self.log.info(len(all_stops))
        self.utils_obj.assert_list_item_text(all_stops, stop)'''
