from pages.main_page import MainPage
import allure

class TestLogoNavigation:

    @allure.title("Проверка перехода после нажатия на логотип Самоката")
    def test_scooter_logo_redirect_to_main_page(self, driver):
        main_page=MainPage(driver)

        main_page.open_order_page()
        main_page.click_scooter_logo()
        main_page.wait_for_main_page_url()

        assert main_page.is_main_page_opened(), "Переход на главную страницу не произошел"

    @allure.title("Проверка перехода после нажатия на ллоготип Яндекса")
    def test_yandex_logo_redirect_to_dzen(self, driver):

        main_page=MainPage(driver)
        main_page.open()
        old_window = main_page.get_current_window()

        main_page.click_yandex_logo()
        main_page.switch_to_new_window(old_window)
        main_page.wait_for_dzen_url()

        assert main_page.is_dzen_opened(), "Переход на Dzen.ru не произошел"        