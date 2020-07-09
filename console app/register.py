from course import course_detail
import student


# increase by 1 when student register
#id for student
count = 0

def register():
    print('\nRegistration: ')
    name = input('Enter you name: ')
    email = input('Enter you email: ')
    print('\n')
    course_detail()
    course = input('Enter the id of the course you have selected.')
    
    # age 
    while True:
        _age = input('Enter you age: ')
        try:
            age = int(_age)
            break
        except ValueError:
            print('Please enter valid integer.')

    # Amount paid
    while True:
        amount = int(input('Enter the amount(Toral 20,000) \nYou can pay in two installments with Rs. 10,000 each): '))
        if amount == 10000 or amount == 20000:
            break
        else:
            print('Sorry. You must pay 1000 or 2000')
    
    global count
    count += 1
    obj = student.Student(count, name, email,age, course, amount)
    obj.register()