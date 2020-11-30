import csv, smtplib, getpass, time

sacs_address = "@sacs.k12.in.us"
username = input("Username: ").strip().lower() + sacs_address
password = getpass.getpass("Password: ").strip()

teacher_objects = []

#class creating instances of teachers with attributes
class Teacher():
    """class to handle teachers as objects including their email address and list of UNA students"""

    def __init__(self, user, name):
        self.email = user + sacs_address 
        self.name = name
        self.una_students = []

    def send_emails(self):
        '''
        smtpObj = smtplib.SMTP('smtp.office365.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()

        smtpObj.login(username, password)
        '''
        message = """Subject: UNA Students

Teachers,\n\nPlease verify that the following students were absent today:"""

        for name in self.una_students:
            message += '\n' + name[0] + name[1]

        message += '\n\nThanks,\n\nMarcy Kaopuiki, NGAP Attendance Clerk'
        smtpObj.sendmail(username, 'dschnaars@sacs.k12.in.us', message)

        #smtpObj.quit()

#iterating through the teacher email database and creating class instances of each teacher
with open('teachers.csv', 'r') as teachers:
    teacher_list = csv.reader(teachers)

    for teacher in teacher_list:
        teacher[1] = Teacher(teacher[1], teacher[0])
        teacher_objects.append(teacher[1])

with open('Attendance.csv', 'r') as attendance:
    una_list = csv.reader(attendance)

    for line in una_list:
        #TODO: add a check in here that will return a message if the teacher in question is not found in the list of teacher objects
        for teacher in teacher_objects:
            if line[0] == teacher.name:
                teacher.una_students.append((line[1], line[2]))

tic = time.time()
smtpObj = smtplib.SMTP('smtp.office365.com', 587)
smtpObj.ehlo()
smtpObj.starttls()

smtpObj.login(username, password)

for teacher in teacher_objects:
    if teacher.una_students != []:
        teacher.send_emails()

smtpObj.quit()
toc = time.time()

print(round(toc-tic, 4))