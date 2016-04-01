import smtplib


class Email:
    def __init__(self):
        self.fromaddr = 'biblioteca.fgv@gmail.com'
        self.toaddrs = 'marciomacielbastos@hotmail.com'
        self.username = 'biblioteca.fgv@gmail.com'
        self.password = ''
        self.server = smtplib.SMTP('smtp.gmail.com:587')
        self.server.ehlo()
        self.server.starttls()

    def send_email(self, subject, msg):
        msg = "\r\n".join([
                "From: biblioteca.fgv@gmail.com",
                "To: marciomacielbastos@hotmail.com",
                "Subject: "+subject,
                "",
                msg
                ])
        self.server.login(self.username, self.password)
        self.server.sendmail(self.fromaddr, self.toaddrs, msg)
        self.server.quit()

