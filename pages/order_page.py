from selenium.webdriver.common.by import By
import allure
from locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):

    @allure.step('Вводим имя текущего варианта')
    def set_name(self, name):
        self.set_text(OrderPageLocators.ORDER_NAME, name)

    @allure.step('Вводим фамилию текущего варианта')        
    def set_surname(self, surname):
        self.set_text(OrderPageLocators.ORDER_SURNAME, surname)

    @allure.step('Вводим адрес текущего варианта')        
    def set_address(self, address):
        self.set_text(OrderPageLocators.ORDER_ADDRESS, address)

    @allure.step('Вводим станцию метро текущего варианта')    
    def set_metro_station(self, metro_station):
        # Кликаем на поле и вводим название станции для фильтрации
        self.click_element(OrderPageLocators.ORDER_METRO_STATION)
        self.set_text(OrderPageLocators.ORDER_METRO_STATION, metro_station)
        metro_station_option=(By.XPATH, OrderPageLocators.METRO_STATION_OPTION.format(
            metro_station))

        self.click_element(metro_station_option, timeout=5)

    @allure.step('Вводим № телефона текущего варианта')        
    def set_phone_number(self, phone_number):
        self.set_text(OrderPageLocators.ORDER_PHONE_NUMBER, phone_number)

    @allure.step('Нажимаем кнопку Далее по результатам ввода данных первой страницы')    
    def click_next_button(self):
        self.click_element(OrderPageLocators.ORDER_TO_CONTINUE)

    @allure.step('Заполнение первой страницы')        
    def fill_first_order_form(self, name, surname, address, metro_station, phone_number):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro_station(metro_station)
        self.set_phone_number(phone_number)
        self.click_next_button()        

    @allure.step('Вводим дату получения самоката')
    def set_delivery_date(self, date):
        self.set_text(OrderPageLocators.ORDER_DATE_TRANSFER, date + u'\ue007')

    @allure.step('Вводим срок аренды самоката')
    def set_rental_period(self, duration):
        self.click_element(OrderPageLocators.ORDER_RENTAL_PERIOD)

        rental_period_option = (By.XPATH,
            OrderPageLocators.ORDER_RENTAL_PERIOD_OPTION.format(duration))

        self.click_element(rental_period_option)

    @allure.step('Выбираем цвет самоката')
    def set_scooter_color(self, color):
        color_locator = (By.XPATH,
            OrderPageLocators.ORDER_SCOOTER_COLOR.format(color))

        self.click_element(color_locator)

    @allure.step('Комментарии для курьера')
    def set_comment(self, comments):
        self.set_text(OrderPageLocators.ORDER_COMMENT_FOR_COURIER, comments)

    @allure.step('Кнопка окончания подачи заявки')
    def click_order_button(self):
        self.click_element(OrderPageLocators.ORDER_FINISH_BUTTON)

    @allure.step('Заполнение второй страницы')
    def fill_second_order_form(self, date, duration, color, comments):
        self.set_delivery_date(date)
        self.set_rental_period(duration)
        self.set_scooter_color(color)
        self.set_comment(comments)
        self.click_order_button()    

    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        self.click_element(OrderPageLocators.ORDER_CONSENT_CONFIRMATION)

    @allure.step('Заголовок об успешном создании зявкаи')
    def is_order_success_modal_displayed(self):
        return self.wait_for_visible(OrderPageLocators.ORDER_SUCCESS_TITLE, timeout=5
        ).is_displayed()

    @allure.step('Ждем и кликаем на кнопку "Посмотреть статус"')
    def click_view_status_button(self):
        self.click_element(OrderPageLocators.VIEW_STATUS_BUTTON)
        
    @allure.step('Ожидает наличия в url строки /track, для подтвержения налчиия № заказа')        
    def wait_for_order_track_page(self):
        self.wait_for_url_contains("/track", timeout=5)

    @allure.step('True/False наличия в url строки /track, для подтвержения налчиия № заказа')        
    def is_order_track_page_opened(self):
        return "/track" in self.get_current_url()