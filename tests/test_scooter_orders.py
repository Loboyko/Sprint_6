import data
from pages.main_page import MainPage
from pages.order_page import OrderPage
import pytest
import allure

class TestScooterOrders:

    @pytest.mark.parametrize(
        "order_button_method, user",
        [
            (MainPage.click_order_from_header, data.user[0]),
            (MainPage.click_order_from_center, data.user[1]),
        ])
    
    @allure.title("Проверка бронирования самокатов")
    def test_scooter_order(self, driver, order_button_method, user):
        main_page=MainPage(driver)
        order_page=OrderPage(driver)
        
        main_page.open()
        main_page.accept_cookies()
        order_button_method(main_page)
        name, surname, address, metro_station, phone_number, date, duration, color, comments = user
        
        order_page.fill_first_order_form(name, surname, address, metro_station, phone_number)
        
        order_page.fill_second_order_form(date, duration, color, comments)
        
        order_page.confirm_order()
        
        assert order_page.is_order_success_modal_displayed(), "Не появилось окно успешного оформления заказа"
        


