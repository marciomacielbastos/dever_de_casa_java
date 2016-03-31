import time

from Renew import Renew

while True:
    r = Renew()
    r.start()
    if r.check_deadline():
        print "Next Hotch Tchopic"
        time.sleep(86400)
    else:
        print "Too early"
        time.sleep(86400)
