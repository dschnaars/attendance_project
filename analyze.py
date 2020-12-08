import csv, time, smtplib

def analyze_csv(filename):
    error = False #bool used to detect certain spreadsheet errors such as missing data or blank lines

    #bools used to check for the presence of each grade level as a means of error checking
    freshmen = 0 
    sophomores = 0 
    juniors = 0 
    seniors = 0 

    with open (filename, 'r') as attendance:
        check_list = csv.reader(attendance)

        for line in check_list:
            #loop will check each line for grade level and report back the grade levels present in the spreadsheet to the user
            if '9' in line and not freshmen:
                #print('This file has 9th graders.')
                freshmen = 9 
            if '10' in line and not sophomores:
                #print('This file has 10th graders.')
                sophomores = 10 
            if '11' in line and not juniors:
                #print('This file has 11th graders.')
                juniors = 11 
            if '12' in line and not seniors:
                #print('This file has 12th graders.')
                seniors = 12 
            #if all 4 grade levels are present the loop can end early
            if freshmen and sophomores and juniors and seniors:
                break

    #TODO: investigate a way to combine this analysis of the spreadsheet with the preceeding one
    with open (filename, 'r') as attendance:
        check_list = csv.reader(attendance)

        #loop will iterate through the spreadsheet again looking for lines with blank data and report back to the user that they must be deleted
        count = 1
        for line in check_list:
            if ('' in line or line == []) and not error:
                print('Error in spreadsheet. Lines with blank or missing data found on line {}.'.format(count))
                error = True
                break
            count += 1

    return error, [freshmen, sophomores, juniors, seniors]

def analyze_emails():
    """Function that will quickly run through teacher email .csv file and check
    that all email addresses are valid. Cannot use the smtpObj.verify() 
    function because it (likely) is disabled by our server. This simple checks 
    that the field in the teachers.csv file does not contain any obvious 
    invalidities."""
    with open('teachers.csv', 'r') as teachers:
        teacher_list = csv.reader(teachers)

        for teacher in teacher_list:
            if teacher[1] == '':
                print('Invalid username/email for', teacher[0], "\nFix error in teachers.csv before continuing.")
                return False
            #TODO: write a regex that wil check a username to confirm that it only contains letters and numbers
        return True
