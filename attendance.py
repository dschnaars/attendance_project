import csv, smtplib, time, sys
import analyze, teacher_class, update, send

tic = time.time()

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

send.send_emails(missed_students, teacher_objects, sacs_address)

toc = time.time() #end time for program execution

print("Program execution time:", round(toc-tic, 4), "seconds") #print the time taken to complete sending all emails, rounded to 4 decimals