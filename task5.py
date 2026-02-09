# TASK 5: Using Python or PHP or Java or Ruby or JavaScript
# Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us.. Return the largest of the three. Do this without using the the inbuilt max () function!

input1=int(input('Please enter input1:'))
input2=int(input('Please enter input2:'))
input3=int(input('Please enter input3:'))

if input1 > input2 and input1 > input3 :
   print('input1 is the largest')
elif input2 > input1 and input2 > input3 :
    print('input2 is the largest')
else :
     print('input3 is the largest')
   
