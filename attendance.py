import csv, smtplib, getpass, time, sys
import analyze, create

sacs_address = "@sacs.k12.in.us"

filename = input("Enter the name of the file to analyze.\nLeave out the extension (.csv)\nFilename: ").strip()
filename += '.csv'
errors, grades_present = analyze.analyze_csv(filename)

if errors:
    print("Fix errors is spreadsheet before continuing.")
    sys.exit()

#TODO: add a print statement listing the grade levels present and give the user the option to quit here if incorrect grade levels have been included

teacher_objects = []

#iterating through the teacher email database and creating class instances of each teacher
with open('teachers.csv', 'r') as teachers:
    teacher_list = csv.reader(teachers)

    for teacher in teacher_list:
        teacher[1] = create.Teacher(teacher[1], teacher[0])
        teacher_objects.append(teacher[1])

missed_students = []
date_today = input("Enter the date for attendance data uploaded:\nDate: ").strip()

with open(filename, 'r') as attendance:
    una_list = csv.reader(attendance)

    line_number = 0
    for line in una_list:
        #TODO: add a checker to see if there are empty fields in CSV file, indicating there is an error and should NOT proceed with the remainder of the program
        #TODO: check line for presence of grade 9, 10, 11, or 12 and report grades present before sending emails to wrong grade-level teachers
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
                pass
                #teacher.send_emails()
            if count % 3 == 0:
                print("Sending emails...") 
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
