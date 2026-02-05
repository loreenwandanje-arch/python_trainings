# TASK 1: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prompts the user to enter the base and height of a triangle and returns its area.
# Once you learn functions,revisit this and write this code inside a function.
def area_triangle():
    base=float(input('Enter the base of the triangle'))
    height=float(input('Enter the height of the triangle'))
    area=1/2 * base *height
    return area
x=area_triangle()
print(f'The area of the triangle is {x}')
