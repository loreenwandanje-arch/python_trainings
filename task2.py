# TASK 2: Using Python or PHP or Java or Ruby or JavaScript
# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
# Once you learn functions,revisit this and write this code inside a function.
def check_number (number) :
     if number % 4==0 :
        return f'{number} is divisible by 4 '
     elif number % 2 ==0:
        return f'{number} is even'
   
     else:
        return f'{number} is odd'

number = int(input('Enter a number:'))
result = check_number(number)
print(result)