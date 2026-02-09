# TASK 7: Using Python or PHP or Java or Ruby or JavaScript
# Write that prompts the user to input student marks. The input should be between 0 and 100.
# Then output the correct grade: 
# A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40

marks = float(input('Enter students marks:'))

if marks <0 or marks > 100 :
    print ('Invalid! Marks must be between 0 and 100')

else:
    if marks > 79 :
        grade= 'A'
    elif marks >= 60 :
        grade='B'
    elif marks >= 50 :
        grade='C'
    elif marks >= 40 :
        grade= 'D'
    else:
        grade='E'

print (f'Marks:{marks}')   
print(f'Grade:{grade}')         

        