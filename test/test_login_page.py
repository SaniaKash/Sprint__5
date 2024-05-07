
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver,get_main_page
from locators import StellarBurgerslocators
from input_data import InputData


class TestLogin:
    def test_from_login_page_to_main_page_success(self,driver,get_main_page):
        driver.find_element(*StellarBurgerslocators.PRIMARY_ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(StellarBurgerslocators.INPUT_EMAIL))
        driver.find_element(*StellarBurgerslocators.INPUT_EMAIL).send_keys(InputData.constant_login)
        driver.find_element(*StellarBurgerslocators.INPUT_PASSWORD).send_keys(InputData.constant_password)
        driver.find_element(*StellarBurgerslocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgerslocators.MAIN_PAGE_IMG))
        assert driver.current_url == StellarBurgerslocators.URL_MAIN_PAGE



    def test_from_personal_account_login_to_main_page_success(self,driver,get_main_page):
        driver.find_element(*StellarBurgerslocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgerslocators.INPUT_EMAIL))
        driver.find_element(*StellarBurgerslocators.INPUT_EMAIL).send_keys(InputData.constant_login)
        driver.find_element(*StellarBurgerslocators.INPUT_PASSWORD).send_keys(InputData.constant_password)
        driver.find_element(*StellarBurgerslocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgerslocators.MAIN_PAGE_IMG))
        assert driver.current_url == StellarBurgerslocators.URL_MAIN_PAGE



    def test_from_reg_page_login_to_main_page_success(self, driver,get_main_page):
        driver.find_element(*StellarBurgerslocators.PRIMARY_ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StellarBurgerslocators.AUTH_LINK))

        driver.find_element(*StellarBurgerslocators.AUTH_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StellarBurgerslocators.LINK_ENTER_BUTTON))
        driver.find_element(*StellarBurgerslocators.LINK_ENTER_BUTTON).click()
        driver.find_element(*StellarBurgerslocators.INPUT_EMAIL).send_keys(InputData.constant_login)
        driver.find_element(*StellarBurgerslocators.INPUT_PASSWORD).send_keys(InputData.constant_password)
        driver.find_element(*StellarBurgerslocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgerslocators.MAIN_PAGE_IMG))
        assert driver.current_url == StellarBurgerslocators.URL_MAIN_PAGE



    def test_from_recovery_page_login_to_main_page_success(self, driver,get_main_page):
        driver.find_element(*StellarBurgerslocators.PRIMARY_ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgerslocators.FORGOT_PASSWORD))
        driver.find_element(*StellarBurgerslocators.FORGOT_PASSWORD).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgerslocators.LINK_ENTER_BUTTON))
        driver.find_element(*StellarBurgerslocators.LINK_ENTER_BUTTON).click()


        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgerslocators.INPUT_EMAIL))
        driver.find_element(*StellarBurgerslocators.INPUT_EMAIL).send_keys(InputData.constant_login)
        driver.find_element(*StellarBurgerslocators.INPUT_PASSWORD).send_keys(InputData.constant_password)
        driver.find_element(*StellarBurgerslocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgerslocators.MAIN_PAGE_IMG))
        assert driver.current_url == StellarBurgerslocators.URL_MAIN_PAGE