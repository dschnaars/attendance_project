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
        try:
            for student in self.una_students:
                message += '\t\n' + student[0] + ', ' + student[1] + ', period ' + student[2]

            if username == 'mkaopuiki@sacs.k12.in.us':
            #if username == 'dschnaars@sacs.k12.in.us': 
                message += '\n\nThanks,\n\nMarcy Kaopuiki, Attendance/Discipline Secretary\t\nHomestead High School NGAP'
            elif username == 'randersen@sacs.k12.in.us':
                message += '\n\nThanks,\n\nRita Andersen, Attendance Secretary Grades 10-12\t\next. 2280\t\nHomestead High School NGAP'
            else:
                message += '\n\nThanks, HHS Attendance'
    
            smtpObj.sendmail(username, self.email, message)
        except smtplib.SMTPRecipientRefused:
            print(self.email)