
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver,get_profile_page,get_main_page
from locators import StellarBurgerslocators
from input_data import InputData



class TestPersonalAccount:
    def test_enter_personal_account_success(self,driver,get_main_page):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgerslocators.MAIN_PAGE_IMG))
        driver.find_element(*StellarBurgerslocators.PRIMARY_ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(StellarBurgerslocators.INPUT_EMAIL))
        driver.find_element(*StellarBurgerslocators.INPUT_EMAIL).send_keys(InputData.constant_login)
        driver.find_element(*StellarBurgerslocators.INPUT_PASSWORD).send_keys(InputData.constant_password)
        driver.find_element(*StellarBurgerslocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(StellarBurgerslocators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*StellarBurgerslocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(StellarBurgerslocators.PROFILE_OUT_BUTTON))
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

        assert driver.current_url == StellarBurgerslocators.URL_LOGIN_PAGE