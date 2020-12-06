import smtplib
sacs_address = "@sacs.k12.in.us"

#class creating instances of teachers with attributes
class Teacher():
    """class to handle teachers as objects including their email address and list of UNA students"""

    def __init__(self, user, name):
        self.email = user + sacs_address 
        self.name = name
        self.una_students = []

    def send_emails(self, smtpObj, username, date_today):
        message = """Subject: UNA Students

Teachers,\n\nPlease verify that the following students were absent on {}:""".format(date_today)

        for student in self.una_students:
            message += '\n' + student[0] + ', ' + student[1] + ', period ' + student[2]

        if username == 'mkaopuiki':
            message += '\n\nThanks,\n\nMarcy Kaopuiki, Attendance/Discipline Secretary\nHomestead High School NGAP'
        elif username == 'randerson':
            message += '\n\nThanks,\n\nRita Anderson, Attendance Secretary Grades 10-12\nHomestead High School NGAP'
        else:
            message += '\n\nTest from Dan Schnaars'

        smtpObj.sendmail(username, self.email, message)
        #can raise an error if email address is invalid
        #smtplib.SMTPRecipientsRefused: {'@sacs.k12.in.us': (501, b'5.1.3 Invalid address')}
        #TODO: add a try/except to handle this possible error here