""" IT Academy Console App """

import csv
from register import register
from course import course_detail
from student_info import student_info

# creation of csv file with headers
with open('student_detail.csv', 'w') as file:
    fieldnames = ['Id', 'name', 'emain','age', 'course', 'pay_ampunt', 'remaining_amount']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()


def main():
    """main function"""
    
    # continue the program while true
    while True:
        print('\nSelect the following')
        print('---------------------')
        print('1.Course Detail.')
        print('2.Registration.')
        print('3.Display all student information.')
        print('4.Update the student information.')
        print('\nEnter the integer to select')

        # runs until user give integer value
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
                print('\nSorry.Enter the integer number from 1-4')
        
        # Selection of course details
        if choice == 1:
            print('\n Course Details: ')
            course_detail()
            if input("Press 'y' to go back: ").lower() == 'y':
                main()
        
        #registration
        elif choice == 2:
            register()
        
        elif choice == 3:
            student_info()

        elif choice == 4:
            student_info()
            print('\nUpdate about the student.')


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