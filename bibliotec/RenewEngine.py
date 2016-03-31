import time
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

__author__ = 'marcio'


class RenewEngine:
    def __init__(self, driver):
        self.driver = driver
        self.subbase_path = '//*[@class="divMain"]/div[4]/table/tbody/tr[2]/td/table[2]/tbody/tr/td/form/'
        self.basepath = self.subbase_path+'table[3]/tbody/'
        self.table_books = []

    def load_rented_books(self):
        page = 'https://sb.fgv.br/catalogo-rj'
        self.driver.get(page)
        mainframe = self.driver.find_element_by_name("mainFrame")
        self.driver.switch_to.frame(mainframe)
        element = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "tab_principal")))
        element.find_element_by_xpath('//*[@class="centro"]/span[5]/a').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@class="div-servicos"]/span[2]/a').click()
        time.sleep(2)

    def check_all(self):
        self.driver.find_element_by_xpath(self.basepath+'tr/td[2]/input').click()

    def check_one(self, row):
        table_row = self.table_books[row]
        table_row.find_elements_by_tag_name('td')[1].click()

    def submit_renew(self):
        self.driver.find_element_by_xpath(self.subbase_path+'/table[2]/tbody/tr/td/a').click()

    def get_table_of_rented_books(self):
        self.table_books = table_rows = self.driver.find_elements_by_xpath(self.basepath+'tr')
        return table_rows

    def get_date_of_a_book(self, row):
        book = self.table_books[row]
        return book.find_elements_by_tag_name('td')[7].text

    def get_name_of_a_book(self, row):
        book = self.table_books[row]
        return book.find_elements_by_tag_name('td')[2].text.strip()

    @staticmethod
    def str_to_date(str_date):
        return datetime.datetime.strptime(str_date.strip(), '%d/%m/%y').date()

    def get_older_book(self):
        num_books = len(self.table_books)
        date_min = self.str_to_date(self.get_date_of_a_book(1))
        for i in range(1, num_books-2):
            d = self.str_to_date(self.get_date_of_a_book(i + 1))
            if date_min >= d:
                date_min = d
        return date_min

    def get_list_of_expired_books(self, today):
        expired_books = []
        for book in range(1, len(self.table_books)):
            expire_date = self.str_to_date(self.get_date_of_a_book(book))
            if today >= expire_date:
                expired_books.append(book)
            else:
                pass
        return expired_books
