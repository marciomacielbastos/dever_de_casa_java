import time
from Email import Email
from Renew import Renew

books = {u'Introduction to analysis': 3, u'The elements of statistical learning': 3,
         u'Introduction to probability models': 3}

while True:
    e = Email()
    r = Renew()
    r.start()
    book_list = r.check_deadline_element_wise()
    try:
        if book_list:
            for book in book_list:
                if book not in books.keys():
                    books[book] = 4
                books[book] -= 1
            print "========================================================"
            for book in books.keys():
                print book, books[book]
            print "========================================================"
            time.sleep(86400)
        else:
            print "Too early"
            time.sleep(86400)

        for book in books.keys():
            if books[book] <= 1:
                books.pop(book, None)
                print "You have to renew inplace " + book
                e.send_email("Urgent", "You have to renew inplace " + book)

    except:
        e.send_email("Deu Pau", u'Deu pau no renovador de livro')