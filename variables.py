#Day 2 Excersise 1
first_name= "Image"
last_name="Kunwar"
full_name="Image Kunwar"
country="Nepal"
city="Kathmandu"
age= 26
year=2026
is_married=False
is_true= False
is_light_on=False


#Exercise 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

"""Exercises: Level 2
Check the data type of all your variables using type() built-in function
Using the len() built-in function, find the length of your first name
Compare the length of your first name and your last name
Declare 5 as num_one and 4 as num_two
Add num_one and num_two and assign the value to a variable total
Subtract num_two from num_one and assign the value to a variable diff
Multiply num_two and num_one and assign the value to a variable product
Divide num_one by num_two and assign the value to a variable division
Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
Calculate num_one to the power of num_two and assign the value to a variable exp
Find floor division of num_one by num_two and assign the value to a variable floor_division
The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.
Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords """

print('First name :',len(first_name))
First_name_length=len(first_name)
Last_name_length=len(last_name)
print(First_name_length)
print(Last_name_length)
if First_name_length > Last_name_length:
    print("Length of first name is greater:",First_name_length)
elif First_name_length < Last_name_length:
    print("Length of second name is greater:",Last_name_length)
else:
    print(("Both are same length"))


num_one=5
num_two=4
total=num_one + num_two
diff=num_two - num_one
product=num_one * num_two
division= num_one/num_two
remainder=num_two % num_one
exp=pow(num_one, num_two)                  #num 1 power num 2
floor_division=num_one//num_two
