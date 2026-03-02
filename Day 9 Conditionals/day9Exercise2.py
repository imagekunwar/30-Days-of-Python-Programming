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
    
# 2) Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, 
# the season is Autumn. December, January or February,
#  the season is Winter. March, April or May, the season is Spring June,
#  July or August, the season is Summer.
