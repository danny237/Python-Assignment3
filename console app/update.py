import csv
from course import course_detail

def update():

    print('Enter the id of the student to update.')
    update_id = int(input())
    name = input('Enter the name: ')
    email = input('Enter the email: ')
    course_detail()
    course = input('Enter the id of the course: ')
    age = input('Enter the age: ')
    pay_amount = int(input('Enter the total amount: '))
    remaining = 20000 - pay_amount

    student_update = [update_id, name, email, course, age, pay_amount, remaining]

    filename = 'student_detail.csv'

    
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        rows = []
        for row in csv_reader:
            if row[0] == update_id:
                rows.append(student_update)
            else:
                rows.append(row)

    with open(filename, 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(rows)