from selenium.webdriver.common.by import By


class StellarBurgerslocators:

    # ГЛАВНАЯ СТРАНИЦА САЙТА
    # все картинке на главной странице сайта
    MAIN_PAGE_IMG = (By.XPATH, "//img")
    # главная страница StellarBurgers
    URL_MAIN_PAGE = 'https://stellarburgers.nomoreparties.site/'
    # кнопка "Личный кабинет" на главной странице
    PERSONAL_ACCOUNT_BUTTON=(By.XPATH, "//*[text()='Личный Кабинет']")
    # кнопка "войти в аккаунт" на главной странице
    PRIMARY_ENTER_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # ссылка "Зарегистрироваться"
    AUTH_LINK = (By.XPATH, "//*[text()='Зарегистрироваться']")

    # ГЛАВНАЯ СТРАНИЦА САЙТА(КОНСТРУКТОР)
    # кнопка "Соусы"
    SAUCE_BUT=(By.XPATH,"//span[text()='Соусы']")
    # кнопка "Булки"
    SPAN_BUT=(By.XPATH,"//span[text()='Булки']")
    # кнопка "Флюоресцентная булка R2 - D3"
    SPAN_R2_D3=(By.XPATH,"//p[text()='Флюоресцентная булка R2-D3']")
    # кнопка "Соус традиционный галактический"
    GALACTIC_SAUCE=(By.XPATH,"//p[contains(text(),'галактический')]")
    # активная вкладка в конструкторе
    ACTIVE_TAB_CONST=(By.XPATH, "//*[contains(@class,'current')]")
    # кнопка "Начинки"
    FILLINGS_BUT = (By.XPATH, "//span[text()='Начинки']")
    # кнопка "Говяжий метеорит"
    BEEF_METEOR=(By.XPATH, "//p[text()='Говяжий метеорит (отбивная)']")


    # СТРАНИЦА РЕГИСТРАЦИИ
    # поле ввода имени
    REG_URL = 'https://stellarburgers.nomoreparties.site/register'
    INPUT_NAME_REGISTER = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input")
    # поле ввода эмейла
    INPUT_EMAIL_REGISTER = (By.XPATH, "//label[text() = 'Email']/following-sibling::input")
    # поле ввода пароля
    INPUT_PASSWORD_REGISTER = (By.XPATH, '//label[text() = "Пароль"]/following-sibling::input')
    # кнопка "Зарегистрироваться" на странице регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # ссылка "Войти"
    LINK_ENTER_BUTTON = (By.XPATH, "//*[text() = 'Войти']")
    # текст ошибки неверного пароля: "Некорректный пароль"
    ERROR_TEXT=(By.XPATH,"//*[text()='Некорректный пароль']")

    # СТРАНИЦА ВХОДА
    URL_LOGIN_PAGE = 'https://stellarburgers.nomoreparties.site/login'
    # поле ввода логина на странице входа
    INPUT_EMAIL = (By.XPATH, ".//input[@name = 'name']")
    # поле ввода пароля на странице входа
    INPUT_PASSWORD = (By.XPATH, ".//input[@name = 'Пароль']")
    # кнопка "Войти" на странице входа
    ENTER_BUTTON = (By.XPATH, "//button[text() = 'Войти']")
    # ссылка "Восстановить пароль" на странице входа
    FORGOT_PASSWORD=(By.XPATH, "//a[text()='Восстановить пароль']")


    # СТРАНИЦА "ЛИЧНЫЙ КАБИНЕТ"
    # кнопка "Выход" в личном кабинете
    PROFILE_OUT_BUTTON = (By.XPATH, "//*[text()='Выход']")
    PROFILE_URL = 'https://stellarburgers.nomoreparties.site/account/profile'
    # ссылка "Конструктор"
    CONSTRUCT_LINK= (By.XPATH, "//*[text()='Конструктор']")
    # ссылка StellarBurgers
    LOGO=(By.XPATH,"//div[@class='AppHeader_header__logo__2D0X2']")
