import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

__author__ = 'marcio'


class Login:
    def __init__(self, driver):
        self.driver = driver

    def log_in(self):
        page = 'https://sb.fgv.br/catalogo-rj'
        self.driver.get(page)
        mainframe = self.driver.find_element_by_name("mainFrame")
        self.driver.switch_to.frame(mainframe)
        element = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "tab_principal")))
        element.find_element_by_xpath('//*[@class="centro"]/span[6]/a').click()
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="div_area_iframe"]/iframe'))
        user_login = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.NAME, 'codigo')))
        user_login.send_keys("")
        password = self.driver.find_element_by_name('senha')
        password.send_keys("")
        self.driver.find_element_by_xpath('//*[@id="button1"]').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@class="button_login"]').click()
