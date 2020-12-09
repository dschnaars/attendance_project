# attendance_project
Attendance project started for HHS attendance clerks to help automate emails to teachers concerning UNA students.

Instructions for use:
1. Generate the UNA report and ensure that it contains 4 fields in the following order:
    a. Teacher (Last, First)
    b. Student (Last, First)
    c. Grade Level
    d. Class Period i.e. 5(A-E)
2. Save the spreadsheet as a .csv (MS-DOS) file type.
    a. Remove any blank lines at the beginning or end of the data.
3. Reload the repl "attendance_project" (F5 will do this)
    a. Delete out any old .csv files to avoid confusion.
4. Upload the .csv file, paying close attention to the file name.
5. Click 'Run' at the top of the page.
6. Enter the filename. You do NOT need to include the .csv extension. This will be added by the program.
    a. The program will return the grade levels found in the file. Examine this closely before continuing.
7. Enter the date to be displayed in the message to teachers. Any date format is fine.
8. Authenticate to the email server using your standard SACS username and password. Username does not need to include '@sacs.k12.in.us'.
9. The program will now generate and send emails to teachers of UNA students found in the .csv file specified in step 4.
10. Report any errors to Mr. Schnaars, dschnaars@sacs.k12.in.us. A screenshot of the error may be helpful. Do NOT reload the repl if possible.