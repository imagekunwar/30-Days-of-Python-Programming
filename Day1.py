2*2
print ('Hello World')
firstname ='image kunwar'
print(firstname)
a = 8
print(type(a))
print(type((6)))
print(type((6.5)))
print(type(3.14))
print(type(4-4j))
print(type(['image','kunwar']))
print(type('image'))
""" Day 1 
of the 
Python Programming """
# CHECKING THE DATA TYPES
print(type(['kathmandu','Pokhara','Biratnagar','Dhangadi','Lumbuni']))
print(type({'name':'Image','address':'Kathmandu'}))
print(type(('mango', 'apple', 'banana', 'pineapple', 'grapes')))
print(type({4,8,16,32,64}))

# Euclidean Distance (2,3) and (10,8)
import math
#Always declare the tuple first and unpack it later
point_1=(2,3)   #Tuple Decleration
point_2=(10,8)

(x1, y1)=point_1 #Unpacking Tuple
(x2,y2)=point_2
distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
print(distance)
