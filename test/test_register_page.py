
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver,login,password,get_main_page
from locators import StellarBurgerslocators
from helpers import InputData




class TestRegisterPage:
    def test_login_page_register_open_main_page_success(self,driver,get_main_page,login,password, user_name='Alex'):

        driver.find_element(*StellarBurgerslocators.PRIMARY_ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StellarBurgerslocators.AUTH_LINK))
        driver.find_element(*StellarBurgerslocators.AUTH_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StellarBurgerslocators.INPUT_NAME_REGISTER))
        driver.find_element(*StellarBurgerslocators.INPUT_NAME_REGISTER).send_keys(user_name)
        driver.find_element(*StellarBurgerslocators.INPUT_EMAIL_REGISTER).send_keys(login)
        driver.find_element(*StellarBurgerslocators.INPUT_PASSWORD_REGISTER).send_keys(password)
        driver.find_element(*StellarBurgerslocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(StellarBurgerslocators.INPUT_EMAIL))
        driver.find_element(*StellarBurgerslocators.INPUT_EMAIL).send_keys(login)
        driver.find_element(*StellarBurgerslocators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*StellarBurgerslocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgerslocators.MAIN_PAGE_IMG))
        assert driver.current_url == StellarBurgerslocators.URL_MAIN_PAGE



    def test_reg_incorrect_password_error(self,driver,get_main_page,login,user_name='Alex'):
        driver.find_element(*StellarBurgerslocators.PRIMARY_ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StellarBurgerslocators.AUTH_LINK))
        driver.find_element(*StellarBurgerslocators.AUTH_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StellarBurgerslocators.INPUT_NAME_REGISTER))
        driver.find_element(*StellarBurgerslocators.INPUT_NAME_REGISTER).send_keys(user_name)
        driver.find_element(*StellarBurgerslocators.INPUT_EMAIL_REGISTER).send_keys(login)
        driver.find_element(*StellarBurgerslocators.INPUT_PASSWORD_REGISTER).send_keys(InputData.password_false())
        driver.find_element(*StellarBurgerslocators.REGISTER_BUTTON).click()
        error = driver.find_element(*StellarBurgerslocators.ERROR_TEXT).text


        assert 'Некорректный пароль' in error
        assert driver.current_url == StellarBurgerslocators.REG_URL