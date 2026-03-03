# 1 ) Write a code which gives grade to students accourding to their scores:
"""90-100, A
80-89, B
70-79, C
60-69, D
0-59, F"""
score=int(input("Enter your score::"))
if(90<=score<=100):
     print("Your Grade is : A") #look
elif(80<=score<=89):
 print("Your Grade is : B")
elif(60<=score<=69):
      print("Your Grade is : C")
elif(60<=score<69):
    print("Your Grade is : D")
elif(0<=score<60):
    print("Your Grade is: F")
else:
    print("Invalid score. Please enter a value between o and 100.")

#*********************    
# 2) Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, 
# the season is Autumn. December, January or February,
#  the season is Winter. March, April or May, the season is Spring June,
#  July or August, the season is Summer.

month=input("Enter the month:")
"""if (month == September or October or November):    #wrong
    print("This a the Autumn Season")
elif(month == December or January or Feburary):
    print ("This month is Winter")
elif(month == March or April or May):
print("This month is winter")
else:
print ("This is Summer:")"""

month = input("Enter the month: ").strip().lower()

if month == "september" or month == "october" or month == "november":
    print("The season is Autumn.")
elif month == "december" or month == "january" or month == "february":
    print("The season is Winter.")
elif month == "march" or month == "april" or month == "may":
    print("The season is Spring.")
elif month == "june" or month == "july" or month == "august":
    print("The season is Summer.")
else:
    print("Invalid month name.")

# best alternative way
month = input("Enter the month: ").strip().lower()

if month in ("september", "october", "november"):
    print("The season is Autumn.")
elif month in ("december", "january", "february"):
    print("The season is Winter.")
elif month in ("march", "april", "may"):
    print("The season is Spring.")
elif month in ("june", "july", "august"):
    print("The season is Summer.")
else:
    print("Invalid month name.")


#3)The following list contains some fruits:
#fruits = ['banana', 'orange', 'mango', 'lemon']
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
 
 