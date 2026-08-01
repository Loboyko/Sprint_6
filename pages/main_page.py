import constants
import allure
from locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):

    @allure.step(f'Открываем главную страницу {constants.URL_SITE}')
    def open(self):
        self.open_url(constants.URL_SITE)

    @allure.step("Принимаем куки")
    def accept_cookies(self):
        self.click_element(MainPageLocators.COOKIE_BUTTON)
    
    @allure.step('Выбираем и кликаем на очередной вопрос')
    def click_question(self, question_locator):
        self.scroll_to_element(question_locator)
        self.click_element(question_locator)

    @allure.step('Получаем текст очередного выбранного вопроса')    
    def get_answer_text(self, answer_locator):
        return self.get_text(answer_locator)
            
    @allure.step('Ждем 3 сек кликабельности кнопки "Заказать" в шапке и кликаем')
    def click_order_from_header(self):
        self.click_element(MainPageLocators.ORDER_FROM_HEADER)

    @allure.step('Прокручиваем текущую страницу до кликабельности кнопки "Заказать"')
    def click_order_from_center(self):
        self.scroll_to_element(MainPageLocators.ORDER_FROM_CENTER)
        self.click_element(MainPageLocators.ORDER_FROM_CENTER)
        
    @allure.step('Ждем 5 сек достпности для клика картинки с названием сервиса и кликаем на нее')
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_IMAGE, timeout=5)
        
    @allure.step(f'Ждем загрузки {constants.URL_SITE}')
    def wait_for_main_page_url(self):
        self.wait_for_url_to_be(constants.URL_SITE)
            
    @allure.step('True/False - совпадает ли текущая url с url сервиса')        
    def is_main_page_opened(self):
        return self.get_current_url() == constants.URL_SITE
        
    @allure.step('Кликаем на картинку в надписью Яндекс')
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_IMAGE, timeout=10)

    @allure.step('Переключаемся на нового открываемое окно')
    def switch_to_new_window(self, old_window):
        self.wait_for_number_of_windows(2, timeout=10)
        
        new_window = [
            window for window in self.get_window_handles()
            if window != old_window][0]

        self.switch_to_window(new_window)

    @allure.step('Ждем в течении 10 сек появление в url "dzen.ru"')
    def wait_for_dzen_url(self):
        self.wait_for_url_contains("dzen.ru", timeout=10)

    @allure.step('Проверяем что открыта именно Dzen.ru(возвращаем True/False)')
    def is_dzen_opened(self):
        return "dzen.ru" in self.get_current_url()
    
    @allure.step('Открываем страницу заказа')
    def open_order_page(self):
        self.open_url(constants.URL_ORDER)