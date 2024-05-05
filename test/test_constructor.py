
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver,get_main_page
from locators import StellarBurgerslocators


class TestConstructor:
    def test_const_switch_to_bun_from_sauce_success(self, driver,get_main_page):
        driver.find_element(*StellarBurgerslocators.SAUCE_BUT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgerslocators.GALACTIC_SAUCE))
        driver.find_element(*StellarBurgerslocators.SPAN_BUT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgerslocators.SPAN_R2_D3))
        assert 'Булки' in driver.find_element(*StellarBurgerslocators.ACTIVE_TAB_CONST).text


    def test_const_switch_to_sauces_from_fillings_success(self, driver,get_main_page):
        driver.find_element(*StellarBurgerslocators.FILLINGS_BUT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgerslocators.BEEF_METEOR))
        driver.find_element(*StellarBurgerslocators.SAUCE_BUT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgerslocators.GALACTIC_SAUCE))
        assert 'Соусы' in driver.find_element(*StellarBurgerslocators.ACTIVE_TAB_CONST).text


    def test_const_switch_to_fillings_from_bun_success(self, driver,get_main_page):
        driver.find_element(*StellarBurgerslocators.FILLINGS_BUT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgerslocators.BEEF_METEOR))
        assert 'Начинки' in driver.find_element(*StellarBurgerslocators.ACTIVE_TAB_CONST).text
