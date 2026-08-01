from selenium.webdriver.common.by import By

class MainPageLocators:

    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    QUESTION_PRICE = (By.XPATH, "//div[@role ='button' and @aria-controls='accordion__panel-0']")
    QUESTION_PRICE_ANSWER = (By.ID, "accordion__panel-0")
    MULTIPLE_SCOOTERS = (By.XPATH, 
        "//div[@role ='button' and @aria-controls='accordion__panel-1']")
    MULTIPLE_SCOOTERS_ANSWER = (By.ID, "accordion__panel-1")
    RENTAL_TIME = (By.XPATH, 
        "//div[@role='button' and @aria-controls='accordion__panel-2']")
    RENTAL_TIME_ANSWER = (By.ID, "accordion__panel-2")

    RENT_RIGHT_NOW = (By.XPATH, 
        "//div[@role='button' and @aria-controls='accordion__panel-3']")
    RENT_RIGHT_NOW_ANSWER = (By.ID, "accordion__panel-3")

    EXTEND_OR_RETURN_EARLIER= (By.XPATH, 
        "//div[@role='button' and @aria-controls='accordion__panel-4']")
    EXTEND_OR_RETURN_EARLIER_ANSWER = (By.ID, "accordion__panel-4")

    QUESTION_CHARGER = (By.XPATH, 
        "//div[@role='button' and @aria-controls='accordion__panel-5']")
    QUESTION_CHARGER_ANSWER = (By.ID, "accordion__panel-5")

    HOW_TO_CANCEL = (By.XPATH, 
        "//div[@role='button' and @aria-controls='accordion__panel-6']")
    HOW_TO_CANCEL_ANSWER = (By.ID, "accordion__panel-6")

    BRING_IT_FAR = (By.XPATH, 
        "//div[@role='button' and @aria-controls='accordion__panel-7']")
    BRING_IT_FAR_ANSWER = (By.ID, "accordion__panel-7")

    ORDER_FROM_HEADER = (By.XPATH,
        "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")

    ORDER_FROM_CENTER = (By.XPATH,
        "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    
    SCOOTER_IMAGE = (By.XPATH, "//img[@alt='Scooter']")
    
    YANDEX_IMAGE = (By.XPATH,"//img[@alt='Yandex']")

class OrderPageLocators:

    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    # локаторы первой страницы формы
    ORDER_NAME = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    ORDER_SURNAME = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")

    ORDER_ADDRESS = (By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]')
    
    ORDER_METRO_STATION = (By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]')
    METRO_STATION_OPTION = "//button[contains(@class, 'select-search__option') and contains(., '{}')]"
    
    ORDER_PHONE_NUMBER = (By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]')

    ORDER_TO_CONTINUE = (By.XPATH, '//button[contains(@class, "Button_Button__ra12g") and contains(@class, "Button_Middle__1CSJM")]')

    # локаторы второй страницы формы
    ORDER_DATE_TRANSFER = (By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]')
    ORDER_RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-control")
    ORDER_RENTAL_PERIOD_OPTION = "//div[@class='Dropdown-option' and text()='{}']"
    ORDER_SCOOTER_COLOR = "//label[contains(@class, 'Checkbox_Label') and contains(text(), '{}')]"
    ORDER_COMMENT_FOR_COURIER = (By.CSS_SELECTOR, 'input[placeholder="Комментарий для курьера"]')
    ORDER_FINISH_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Middle") and normalize-space()="Заказать"]')

    # локаторы подтверждения заказа
    ORDER_CONSENT_CONFIRMATION = (By.XPATH, '//button[contains(@class, "Button_Button__ra12g") and contains(@class, "Button_Middle__1CSJM") and normalize-space()="Да"]')
    ORDER_SUCCESS_TITLE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(., 'Заказ оформлен')]")
    VIEW_STATUS_BUTTON = (By.XPATH, '//button[text()="Посмотреть статус"]')
