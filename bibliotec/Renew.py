from datetime import date, timedelta
from Login import Login
from selenium import webdriver
from RenewEngine import RenewEngine


class Renew:
    def __init__(self):
        self.wd = webdriver
        self.driver = self.wd.Firefox()
        self.renew_object = RenewEngine(self.driver)

    def login(self):
        l = Login(self.driver)
        l.log_in()

    def start(self):
        self.login()
        self.renew_object.load_rented_books()
        self.renew_object.get_table_of_rented_books()

    def check_deadline(self):
        today = date.today() + timedelta(days=2)
        deadline = self.renew_object.get_older_book()
        if today >= deadline:
            self.renew_object.check_all()
            self.renew()
            self.driver.quit()
            return True
        else:
            self.driver.quit()
            return False

    def check_deadline_element_wise(self):
        today = date.today() + timedelta(days=0)
        expired_books = self.renew_object.get_list_of_expired_books(today)
        books = []
        if expired_books:
            for book in expired_books:
                self.renew_object.check_one(book)
                books.append(self.renew_object.get_name_of_a_book(book))
            self.renew()
            self.driver.quit()
            return books
        else:
            self.driver.quit()
            return books

    def renew(self):
        self.renew_object.submit_renew()
