from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver=driver

    def open_url(self, url):
        self.driver.get(url)

    def click_element(self, locator, timeout=3):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)).click()
        
    def set_text(self, locator, text, timeout=3):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)).send_keys(text)
    
    def get_text(self, locator, timeout=3):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)).text
    
    def wait_for_visible(self, locator, timeout=3):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))
        
    def wait_for_clickable(self, locator, timeout=3):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))
    
    def scroll_to_element(self, locator, timeout=3):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_url_to_be(self, url, timeout=3):
        WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(url))
        
    def wait_for_url_contains(self, text, timeout=3):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(text))
        
    def get_current_url(self):
        return self.driver.current_url
    
    def get_current_window(self):
        return self.driver.current_window_handle

    def wait_for_number_of_windows(self, number, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.number_of_windows_to_be(number))
        
    def get_window_handles(self):
        return self.driver.window_handles
    
    def switch_to_window(self, windows):
        self.driver.switch_to.window(windows)