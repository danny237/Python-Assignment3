""" IT Academy Console App """

import csv
import StudentInfo
from course import course_detail




# function that append data to csv



with open('student_detail.csv', 'w') as file:
    fieldnames = ['name', 'emain', 'course', 'pay_ampunt', 'remaining_amount']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()







def main():
    """main function"""
    while True:
        print('\nSelect the following')
        print('---------------------')
        print('1.Course Detail.')
        print('2.Registration.')
        print('3.Display all student information.')
        print('4.Update the student information.')
        print('\nEnter the integer to select')

        
        while True:

            val = input('Select: ')
            try:
                choice = int(val)
                if choice < 5:
                    break
                else:
                    #validate for less than 5
                    print('\nSorry.Enter the value from 1-4')
            except ValueError:
                # validate for integer type
                print('Sorry.Enter the integer number from 1-4')

        if choice == 1:
            print('\n Course Details: ')
            course_detail()
            if input("Press 'y' to go back: ").lower() == 'y':
                main()
        elif choice == 2:
            
            
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

            obj = StudentInfo.Student(name, email, course, age, amount)
            obj.register()

            # with open('student_details.csv', 'w') as csv_file:
            #     csv_writer = csv.
        
        elif choice == 3:
            print('\nDisplaying all the information about student with pay and remaining.')

        elif choice == 4:
            print('Update about the student')

        elif choice == 5:
            print('Delete the student.')

        elif choice == 6:
            print('Return the deposited amount after successfully complete the course.')


        do_continue = input('Do you want to continue? y/n: ').lower()
        if do_continue != 'y':
            break
        else:
            continue



if __name__ == '__main__':
    main()