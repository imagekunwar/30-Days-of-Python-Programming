#Exercises: Level 1
#1)Iterate 0 to 10 using for loop, do the same using while loop.
numbers=[0,1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print(number)
    number +=1

    #while loop
number=0
while number <=10:
    print (number)
    number += 1

    # Best alternative way (look)
    """# for loop
for number in range(11):
    print(number)

# while loop
number = 0
while number <= 10:
    print(number)
    number += 1"""


#2)Iterate 10 to 0 using for loop, do the same using while loop.
for numbers in range(11,-1,-1):   # we have to use negative range in this problem.
 print(numbers)                   #indentation matters while using loop.

 #Using while loop
 num=10
 while num>= 0:
  print("numbers printed in reverse order using while loop",num)
  num -=1

  #using for loop
  for i in range(1,8):
     print("#" * i)
     
#3)Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######
numb=1
while numb <=7:
   print("#"* numb)
   numb +=1

#4)Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

#5)Print the following pattern:

"""0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100"""

#6)Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

#7)Use for loop to iterate from 0 to 100 and print only even numbers

#8)Use for loop to iterate from 0 to 100 and print only odd numbers