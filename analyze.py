import csv, time

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