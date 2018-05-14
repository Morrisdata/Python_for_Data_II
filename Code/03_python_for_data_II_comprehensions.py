############################################################################### 
##                       COMPREHENSIONS
##               1. Basic syntax
##               2. Filtering
##               3. Set and Dictionary                                       ##
###############################################################################
'''
List comprehensions can make your current code more powerful and 
easier to read. You can still code the regular way but this is compressed.
'''
###############################################################################
##                       BASIC SYNTAX                                        ##
###############################################################################
'''
lets say you want to add 2% to a list of numbers and load them into a new 
list
'''

(values) = [(expression) for (value) in (collection)]

# standard for loop
nums = [1,2,3,4,5]
values=[]
for num in nums:
    values.append(num*.02)
print (values)    

# for loop converted into comprehension
nums=[1,2,3,4,5]
values= [num*.02 for num in nums] 
print (values)

## EXERCISE 
# convert the code into a comprehension
##
squares=[]
for x in range(10):
    squares.append(x**x)



## EXERCISE
# convert comphrension to standard For Loop
##
nums=[1,2,3,4,5]
cubes = [num**3 for num in nums]

###############################################################################
##                          FILTERING                                        ##
###############################################################################

(values) = [(expression) for (value) in (collection) if (condition)]

# standard for loop with a filter
nums = [1,2,3,4,5]
values=[]
for num in nums:
    if num <3: 
        values.append(num)
print (values)    


# comprehension
nums = [1,2,3,4,5]
values=[num for num in nums if num <3]
print (values)


## EXERCISE
# 1. filter to only show numbers that are less than 20 
# 2. convert your code into a comprhension

squares=[]
for x in range(100):
    squares.append(x**x) 
    
   
## EXERCISE
# Convert into a list comprhension
##
# for loop to cube even numbers and square odd numbers
nums = [1,2,3,4,5]
cubes_and_squares = []
for num in nums:
    if num % 2 == 0:
        cubes_and_squares.append(num**3)
    else:
        cubes_and_squares.append(num**2)
print (cubes_and_squares)

###############################################################################
##                 SET & DICTIONARY COMPREHENSIONS                           ##
###############################################################################

# set comprehension 
fruits = {'apple', 'banana', 'cherry', 'apple','lemon'}
fruits
unique_lengths = {len(fruit) for fruit in fruits}
fruits
unique_lengths

# dictionary comprehension
a = [x for x in range(5)]
a

b = {x : x for x in range(5)}
b

b = {x: x**3 for x in range(5)}
b

# filters with dictionaries
b = {x: x**3 for x in range(10) if x %2==0}
b

names =['Denise', 'Blake', 'Aaron', 'Jacqueline']
c = {x: x.upper() for x in names}
c

###############################################################################
##                  Best practices                                           ##
###############################################################################
'''
Make it readable
while you can next comprehensions withen comprehensions its not a good idea
longer comprehensions can be broken down with carriage returns to make them 
easier to read
'''
fruits = {'apple', 'banana', 'cherry', 'apple','lemon'}
short_name = {len(fruit) for fruit in fruits if len(fruit) ==5}
short_name

fruits = {'apple', 'banana', 'cherry', 'apple','lemon'}
short_name = {len(fruit) 
              for fruit in fruits 
              if len(fruit) ==5}
short_name



## EXERCISE
# Convert to comprehensions
##
# 1
for color in ['red', 'blue', 'green']:
    print (color.upper())
color

# 2
for color in ['red', 'blue', 'green']:
    print (color.capitalize())

# 3
for color in ['red', 'blue', 'green']:
    print (str.title(color))
color


# 4
for count in [1, 2, 3]:
    print(count)
    print('Yes' * count)
print('Done counting.')

# 5
for color in ['red', 'blue', 'green']:
    if (color) is 'red':
        print ('Red')
    elif(color) == 'blue':
        print ('Blue')
    else: print('Green')
    print(color)

# 6 
def count(numbers):
    total = 0
    for n in numbers:
        if n == 'WA':
            total = total + 1
    return total

x = ['WA', 'ID', 'OR', 'WA','NOTWA','wa', 'WASHINGTON','OR','CA','WA' ]
y = count(x)
print (y)





