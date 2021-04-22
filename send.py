import smtplib, getpass, time, progress.bar

def send_emails(missed_students, teacher_objects, sacs_address):
    """Function that generates emails to each teacher who has students listed in their una attribute."""

    date_today = input("Enter the date for attendance data uploaded:\nDate: ").strip()

    authenticated = True
    while authenticated:
        try: #try entering a correct username and password; will loop until the user chooses to quit or is able to authenticate
            username = input("Username: ").strip().lower() + sacs_address
            password = getpass.getpass("Password: ").strip()
            
            tic = time.time()
        
            smtpObj = smtplib.SMTP('smtp.office365.com', 587)
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login(username, password)

            bar = progress.bar.ChargingBar('Sending Emails', max = len(teacher_objects))

            count = 0
            for teacher in teacher_objects:
                if teacher.una_students != []:
                    #pass
                    teacher.send_emails(smtpObj, username, date_today)
                    bar.next()
                if count % 10 == 0:
                    break
                    #print("Sending...")
                count += 1

            bar.finish()
        
            smtpObj.quit()
        
            for student in missed_students:
                print("Line {}. No teacher email on file for {} {} {}.".format(student[3], student[0], student[1], student[2]))
            if missed_students != []:
                print("\nBe sure to follow up with this teacher or these teachers individually.")
        
            authenticated = False

            toc = time.time() #end time for program execution

            print("Program execution time:", round(toc-tic, 0), "seconds") #print the time taken to complete sending all emails, rounded to 4 decimals
        
        except smtplib.SMTPAuthenticationError:
            print("Looks like your username or password was incorrect.")
            smtpObj.quit()