#CS 175L
#Prof Gil
#Sophia Ramirez Velandia
#Chapter 5 - Calculate Average and Grade with Functions

def calc_average():
    grade1=float(input('Enter score 1: '))
    grade2=float(input('Enter score 2: '))
    grade3=float(input('Enter score 3: '))
    grade4=float(input('Enter score 4: '))
    grade5=float(input('Enter score 5: '))
    total=grade1+grade2+grade3+grade4+grade5
    test=5
    avg = total/test
    return grade1, grade2, grade3, grade4, grade5,avg

def determine_grade(numeric_grade):  
    if numeric_grade>=90 and numeric_grade<=100:
        return 'A'
    elif numeric_grade>=80 and numeric_grade<90:
        return 'B' 
    elif numeric_grade>=70 and numeric_grade<80:
        return 'C'
    elif numeric_grade>=60 and numeric_grade<70:
        return 'D'
    elif numeric_grade<60 and numeric_grade>=0:
        return 'F'


def main():
    question='yes'
    while question=='yes':
        grade1, grade2, grade3, grade4, grade5, avg=calc_average()
        print()
        print('Score', f'{"Numeric Grade   Letter Grade":>35}')
        print('---------------------------------------------------')
        print(f'score 1:  {grade1:>15}',f'{determine_grade(grade1):>7}')
        print(f'score 2:  {grade2:>15}',f'{determine_grade(grade2):>7}')
        print(f'score 3:  {grade3:>15}',f'{determine_grade(grade3):>7}')
        print(f'score 4:  {grade4:>15}',f'{determine_grade(grade4):>7}')
        print(f'score 5:  {grade5:>15}',f'{determine_grade(grade5):>7}')
    
        print(f'Average score: {avg:>10}', f'{determine_grade(avg):>7}')
        print()


        question=input('Enter "yes" if you would like to do another calculation: ')

main()

