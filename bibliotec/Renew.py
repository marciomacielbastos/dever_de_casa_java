from datetime import date, timedelta
from Login import Login
from selenium import webdriver
from RenewEngine import RenewEngine


class Renew:
    def __init__(self):
        self.wd = webdriver
        self.driver = self.wd.PhantomJS()
        self.renew_object = RenewEngine(self.driver)

    def login(self):
        l = Login(self.driver)
        l.log_in()

    def start(self):
        self.login()
        self.renew_object.load_rented_books()
        self.renew_object.get_table_of_rented_books()

    def check_deadline(self):
        date_now = date.today() + timedelta(days=2)
        deadline = self.renew_object.get_older_book()
        if date_now >= deadline:
            self.renew()
            self.driver.quit()
            return True
        else:
            self.driver.quit()
            return False

    def renew(self):
        self.renew_object.check_all()
        self.renew_object.submit_renew()

