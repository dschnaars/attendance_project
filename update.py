import csv

def update_teacher_una(filename, teacher_objects):
    """Function intended to update the una_students attribute for each teacher object"""
    missed_students = []

    with open(filename, 'r') as attendance:
        una_list = csv.reader(attendance)

        line_number = 0
        for line in una_list:
            line_number += 1
            missed = True #sets a variable that, if true at the end of the loop, will append the student in question to a list that gets reported at the end
            try:
                for teacher in teacher_objects:
                    if line[0] == teacher.name:
                        teacher.una_students.append((line[1], line[2], line[3]))
                        missed = False
                if missed:
                    missed_students.append((line[0], line[1], line[2], line[3], line_number))
            except IndexError:
                print("Line {}. Unable to send message to: {}".format(line_number, line))
    
    return missed_students, teacher_objects

