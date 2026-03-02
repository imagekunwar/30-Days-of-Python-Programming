#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length=float(input("Enter the length of a rectangle:"))
width=float(input("Enter the width of a rectangle:"))
area= length * width
print("The area of rectangle is:", area)

#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius=float(input("Enter the radius of the circle:"))
pi=3.14
area_circle=pi*radius*radius
print("Area of the circle is:",area_circle)
#Calculate the slope, x-intercept and y-intercept of y = 2x -2
m=2
c=-2
y_intercept=c
x_intercept=-c/m
print("slope",m)
print("y_intercept",y_intercept)
print("X-intercept",x_intercept)


#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
first_point=(2,2)
second_point=(6,10)
(x1,y1)=first_point
(x2,y2)=second_point
m1=y2-y1/x2-x1
print("Slope is:",m1)

#Euclidean distance
distance=((x2-x1)**2 + (y2-y1)**0.5)
print("Distance",distance)
# Compare the slopes in tasks 8 and 9
print("comparision")
if m==m1:
    print("Both the slopes are equal and lines are parallel.")
else:
    print("Slopes are different.")
#Calculate the value of y (y = x^2 + 6x + 9). 
# Try to use different x values and figure out at what x value y is going to be 0.(look)
# Try different x values
for x in range(-6, 3):
    y = x**2 + 6*x + 9
    print("x =", x, " y =", y)

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.(look)
word1="python"
word2="dragon"
print("Length of python:",len(word1))
print("Length of dragon:",len(word2))

print(len(word1)!=len(word2))
print(len("python") > len("dragon"))   # False
print(len("python") < len("dragon"))   # False

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

print("I hope this course is not full of jargon:",'jargon'in 'I hope this course is not full of jargon')

#There is no 'on' in both dragon and python (look)
print('on' in 'dragon')   
print('on' in 'python')  
#Find the length of the text python and convert the value to float and convert it to string
text1=len("python")
print('Length of the word python is:',float(text1))
print('Length of the word python in string is',str(text1))
#Even numbers are divisible by 2 and the remainder is zero. 
# How do you check if a number is even or not using python?
number=int(input("Enter the number:"))
if(number%2==0):
    print("This is an even number")
else:
    print("This is not even number")
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division=7//3
converted=int(2.7)
if(floor_division==converted):
    print("Equal")
else:
    print("Unequal")
    

#Check if type of '10' is equal to type of 10
# Compare types
if type('10') == type(10):
    print("Equal")
else:
    print("Unequal")


#Check if int('9.8') is equal to 10
#print("Equal" if int(float('9.8')) == 10 else "Unequal")

""""Write a script that prompts the user to enter hours and rate per hour. 
Calculate pay of the person?
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120"""
hours=float(input("Enter the hours:"))
rate=float(input("Enter the rate:"))
pay=hours*rate
print("The total pay of the person is:",pay)

"""Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125 """