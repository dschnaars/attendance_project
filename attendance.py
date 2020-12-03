import csv, smtplib, getpass, time

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

teacher_objects = []

#iterating through the teacher email database and creating class instances of each teacher
with open('teachers.csv', 'r') as teachers:
    teacher_list = csv.reader(teachers)

    for teacher in teacher_list:
        teacher[1] = Teacher(teacher[1], teacher[0])
        teacher_objects.append(teacher[1])

missed_students = []
filename = input("Enter the name of the file to analyze.\nLeave out the extension (.csv)\n").strip()
filename += '.csv'
date_today = input("Enter the date for attendance data uploaded: ".strip())

with open(filename, 'r') as attendance:
    una_list = csv.reader(attendance)

    line_number = 0
    for line in una_list:
        line_number += 1
        missed = True #sets a variable that, if true at the end of the loop, will append the student in question to a list that gets reported at the end
        try:
            for teacher in teacher_objects:
                if line[0] == teacher.name:
                    teacher.una_students.append((line[1], line[2]))
                    missed = False
            if missed:
                missed_students.append((line[0], line[1], line[2], line_number))
        except IndexError:
            print("Line {}. Unable to send message to: {}".format(line_number, line))

smtpObj = smtplib.SMTP('smtp.office365.com', 587)
smtpObj.ehlo()
smtpObj.starttls()

try: #try entering a correct username and password; will loop until the user chooses to quit or is able to authenticate
    username = input("Username: ").strip().lower() + sacs_address
    password = getpass.getpass("Password: ").strip()

    tic = time.time()

    smtpObj.login(username, password)

    for teacher in teacher_objects:
        if teacher.una_students != []:
            pass
            teacher.send_emails()

    smtpObj.quit()

    for student in missed_students:
        print("Line {}. No teacher email on file for {} {} {}.".format(student[3], student[0], student[1], student[2]))
    if missed_students != []:
        print("\nBe sure to follow up with this teacher or these teachers individually.")

    toc = time.time() #end time for program execution

    print("Program execution time:", round(toc-tic, 4), "seconds") #print the time taken to complete sending all emails, rounded to 4 decimals

except smtplib.SMTPAuthenticationError:
    print("Looks like your username or password was incorrect.")
    smtpObj.quit()