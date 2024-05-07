
import pytest
from selenium import webdriver
from locators import StellarBurgerslocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from input_data import InputData



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()




@pytest.fixture
def get_main_page(driver):
    driver.get(StellarBurgerslocators.URL_MAIN_PAGE)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgerslocators.MAIN_PAGE_IMG))



@pytest.fixture
def get_profile_page(driver):
    driver.get(StellarBurgerslocators.URL_MAIN_PAGE)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgerslocators.MAIN_PAGE_IMG))
    driver.find_element(*StellarBurgerslocators.PRIMARY_ENTER_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(StellarBurgerslocators.INPUT_EMAIL))
    driver.find_element(*StellarBurgerslocators.INPUT_EMAIL).send_keys(InputData.constant_login)
    driver.find_element(*StellarBurgerslocators.INPUT_PASSWORD).send_keys(InputData.constant_password)
    driver.find_element(*StellarBurgerslocators.ENTER_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(StellarBurgerslocators.PERSONAL_ACCOUNT_BUTTON))
    driver.find_element(*StellarBurgerslocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(StellarBurgerslocators.PROFILE_OUT_BUTTON))
