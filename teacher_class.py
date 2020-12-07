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
                message += '\n' + student[0] + ', ' + student[1] + ', period ' + student[2]
                message += '\n\nThanks,\n\nMarcy Kaopuiki, Attendance/Discipline Secretary\nHomestead High School NGAP'
    
            #TODO: this structure could be placed at the beginning of the function in order to avoid running each time through the for loop
            if username == 'mkaopuiki':
                print(username, 'if')
                #message += '\n\nThanks,\n\nMarcy Kaopuiki, Attendance/Discipline Secretary\nHomestead High School NGAP'
            elif username == 'randersen':
                print(username, 'elif')
                #message += '\n\nThanks,\n\nRita Andersen, Attendance Secretary Grades 10-12\next. 2280\nHomestead High School NGAP'
            else:
                print(username, 'else')
                #message += '\n\nTest from Dan Schnaars'
    
            smtpObj.sendmail(username, self.email, message)
        except smtplib.SMTPRecipientRefused:
            print(self.email)