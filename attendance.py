import csv, smtplib, getpass, time, sys
import analyze, teacher_class, update

sacs_address = "@sacs.k12.in.us"

filename = input("Enter the name of the file to analyze.\nLeave out the extension (.csv)\nFilename: ").strip()
filename += '.csv'
errors, grades_present = analyze.analyze_csv(filename)

if errors:
    print("Fix errors is spreadsheet before continuing.")
    sys.exit()

print('This spreadsheet contains the following grade levels: {}'.format(grades_present))

teacher_objects = []

#iterating through the teacher email database and creating class instances of each teacher
with open('teachers.csv', 'r') as teachers:
    teacher_list = csv.reader(teachers)

    for teacher in teacher_list:
        teacher[1] = teacher_class.Teacher(teacher[1], teacher[0])
        teacher_objects.append(teacher[1])

missed_students, teacher_objects = update.update_teacher_una(filename, teacher_objects)

smtpObj = smtplib.SMTP('smtp.office365.com', 587)
smtpObj.ehlo()
smtpObj.starttls()

date_today = input("Enter the date for attendance data uploaded:\nDate: ").strip()
authenticated = True
while authenticated:
    try: #try entering a correct username and password; will loop until the user chooses to quit or is able to authenticate
        username = input("Username: ").strip().lower() + sacs_address
        password = getpass.getpass("Password: ").strip()
    
        tic = time.time()
    
        smtpObj.login(username, password)

        count = 1 #variable for providing visual feedback that the program is running
        for teacher in teacher_objects:
            if teacher.una_students != []:
                #pass
                teacher.send_emails(smtpObj, username, date_today)
            if count % 3 == 0:
                pass
                #print("Sending emails...") 
            count += 1
    
        smtpObj.quit()
    
        for student in missed_students:
            print("Line {}. No teacher email on file for {} {} {}.".format(student[3], student[0], student[1], student[2]))
        if missed_students != []:
            print("\nBe sure to follow up with this teacher or these teachers individually.")
    
        toc = time.time() #end time for program execution
    
        print("Program execution time:", round(toc-tic, 4), "seconds") #print the time taken to complete sending all emails, rounded to 4 decimals
        authenticated = False
    
    except smtplib.SMTPAuthenticationError:
        print("Looks like your username or password was incorrect.")
        smtpObj.quit()
