import constants
from pages.main_page import MainPage
from locators import MainPageLocators
import pytest
import allure

@allure.feature("Важные вопросы о сервисе")
class TestImportantQuestions:

    @allure.title("Проверка раскрытия ответов на вопрос о сервисе")
    @allure.description("Проверяем, что при клике на вопрос открывается соответствующий текст ответа.")

    @pytest.mark.parametrize(
        "question_locator, answer_locator, expected_text",
        [(
                MainPageLocators.QUESTION_PRICE,
                MainPageLocators.QUESTION_PRICE_ANSWER,
                constants.TEXT_QUESTION_PRICE),
            (
                MainPageLocators.MULTIPLE_SCOOTERS,
                MainPageLocators.MULTIPLE_SCOOTERS_ANSWER,
                constants.TEXT_MULTIPLE_SCOOTERS),
            (
                MainPageLocators.RENTAL_TIME,
                MainPageLocators.RENTAL_TIME_ANSWER,
                constants.TEXT_RENTAL_TIME),
            (
                MainPageLocators.RENT_RIGHT_NOW,
                MainPageLocators.RENT_RIGHT_NOW_ANSWER,
                constants.TEXT_RENT_RIGHT_NOW),
            (
                MainPageLocators.EXTEND_OR_RETURN_EARLIER,
                MainPageLocators.EXTEND_OR_RETURN_EARLIER_ANSWER,
                constants.TEXT_EXTEND_OR_RETURN_EARLIER),
            (
                MainPageLocators.QUESTION_CHARGER,
                MainPageLocators.QUESTION_CHARGER_ANSWER,
                constants.TEXT_QUESTION_CHARGER),
            (   MainPageLocators.HOW_TO_CANCEL,
                MainPageLocators.HOW_TO_CANCEL_ANSWER,
                constants.TEXT_HOW_TO_CANCEL),
            (
                MainPageLocators.BRING_IT_FAR,
                MainPageLocators.BRING_IT_FAR_ANSWER,
                constants.TEXT_BRING_IT_FAR),])
    def test_important_question(self, driver, question_locator, answer_locator, expected_text):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_question(question_locator)

        assert expected_text in main_page.get_answer_text(answer_locator)
