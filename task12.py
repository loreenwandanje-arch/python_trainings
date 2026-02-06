# #TASK 12: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prints the largest of 4 inputs taken as input from a user.

def largest_number (input1,input2,input3,input4) :
    if input1 > input2 and input1 > input3 and input1 > input4 :
        return f'{input1} is the largest number'
    elif input2 > input1 and input2>input3 and input2>input4:
        return f'{input2} is the largest number'
    elif input3 > input1 and input3>input2 and input3>input4:
        return f'{input3} is the largest number'
    else:
        return f'{input4} is the largest number'
    
input1=int(input('Enter first number:'))
input2=int(input('Enter second number:'))
input3=int(input('Enter third number:'))
input4=int(input('Enter fourth number:'))

result=largest_number(input1,input2,input3,input4)
print(result)

