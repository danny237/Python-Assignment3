
import csv


def student_info():
    with open('student_detail.csv', 'r') as file:
        csv_reader = csv.reader(file)
        count = 0
        for row in csv_reader:
            if count == 0:
                print('------------------------------------------------------------------------------------')
                print(f'  {row[0]}  |  {row[1]}  |  {row[2]}  |  {row[3]}  |  {row[4]}  |  {row[5]}  |  {row[6]}')
                print('====================================================================================')
                count += 1
            else:
                print(f'  {row[0]}  |  {row[1]}  |  {row[2]}  |  {row[3]}  |  {row[4]}  |  {row[5]}  |  {row[6]}')