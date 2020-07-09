"""Registration for student"""

"""  """
import csv
class Student:
    college = ''
    def __init__(self, name, email,course, age, pay_ampunt):
        """Constructor"""

        self.name = name
        self.email = email
        self.age = age
        self.paid_amount = pay_ampunt
        self.remaining = 20000 - pay_ampunt
    def register(self):
        
        student = [self.name, self.email, self.age, self.paid_amount, self.remaining]

        with open('student_detail.csv', 'a') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(student)
        print('Thank you. Your information has been registered.')
        


    
