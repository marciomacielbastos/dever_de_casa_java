import time
from Email import Email
from Renew import Renew

books = {u'Introduction to analysis': 3, u'The elements of statistical learning': 3,
         u'Introduction to probability models': 3}

while True:
    email = Email()
    renewer = Renew()
    renewer.start()
    try:
        book_list = renewer.check_deadline_element_wise()
        if book_list:
            for book in book_list:
                if book not in books.keys():
                    books[book] = 4
                books[book] -= 1
            print "========================================================"
            for book in books.keys():
                print book, books[book]
            print "========================================================"
            b = "========================================================\n"
            for book in book_list:
                b += book+'\n'
            b += "========================================================\n"
            email.send_email("Books renewed", b)
            renewer.quit()
            time.sleep(60000)
        else:
            print "Too early"
            email.send_email("Too early", renewer.get_early_date(1))
            renewer.quit()
            time.sleep(60000)

        for book in books.keys():
            if books[book] < 1:
                books.pop(book, None)
                print "You have to renew inplace " + book
                email.send_email("Urgent", "You have to renew inplace " + book)
    except Exception as e:
        email.send_email("Deu Pau", u'Deu pau no renovador de livro\n' + e.message)
