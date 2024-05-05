
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver,get_profile_page
from locators import StellarBurgerslocators




class TestPersonalAccount:
    def test_enter_personal_account_success(self,driver,get_profile_page):
        assert driver.current_url == StellarBurgerslocators.PROFILE_URL




    def test_from_personal_account_constr_link_to_main_page_success(self, driver,get_profile_page):
        driver.find_element(*StellarBurgerslocators.CONSTRUCT_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgerslocators.MAIN_PAGE_IMG))
        assert driver.current_url == StellarBurgerslocators.URL_MAIN_PAGE




    def test_from_personal_account_logo_link_to_main_page_success(self, driver, get_profile_page):
        driver.find_element(*StellarBurgerslocators.LOGO).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgerslocators.MAIN_PAGE_IMG))
        assert driver.current_url == StellarBurgerslocators.URL_MAIN_PAGE




    def test_from_personal_account_out_to_login_page_success(self, driver, get_profile_page):
        driver.find_element(*StellarBurgerslocators.PROFILE_OUT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(StellarBurgerslocators.INPUT_EMAIL))

        assert driver.current_url == StellarBurgerslocators.LOGIN_PAGE