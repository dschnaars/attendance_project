
sacs_address = "@sacs.k12.in.us"

#class creating instances of teachers with attributes
class Teacher():
    """class to handle teachers as objects including their email address and list of UNA students"""

    def __init__(self, user, name):
        self.email = user + sacs_address 
        self.name = name
        self.una_students = []

    def send_emails(self):
        message = """Subject: UNA Students

Teachers,\n\nPlease verify that the following students were absent on {}:""".format(date_today)

        for name in self.una_students:
            message += '\n' + name[0] + ', ' + name[1]

        message += '\n\nThanks,\n\nMarcy Kaopuiki, Attendance/Discipline Secretary\nHomestead High School NGAP'
        smtpObj.sendmail(username, self.email, message)
        #can raise an error if email address is invalid
        #smtplib.SMTPRecipientsRefused: {'@sacs.k12.in.us': (501, b'5.1.3 Invalid address')}
        #TODO: add a try/except to handle this possible error here