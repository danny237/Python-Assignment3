"""Registration for student"""

"""  """
import csv
class Student:

    count = 0
    def __init__(self, student_id, name, email,course, age, pay_ampunt, update_id = 0):
        """Constructor"""
        self.update_id = update_id
        self.id = student_id
        self.name = name
        self.email = email
        self.course = course
        self.age = age
        self.paid_amount = pay_ampunt
        self.remaining = 20000 - pay_ampunt
    def register(self):
        
        student = [self.id, self.name, self.email, self.age, self.course, self.paid_amount, self.remaining]

        with open('student_detail.csv', 'a') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(student)
        print('Thank you. Your information has been registered.')

    

    
