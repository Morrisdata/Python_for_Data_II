'''
The lambda operator or lambda function is a way to create small anonymous 
functions, i.e. functions without a name. ... Lambda functions are mainly used 
in combination with the functions filter(), map() and reduce(). The lambda 
feature was added to Python due to the demand from Lisp programmers
'''

anonyous_function = lambda


########Lambda############
'''
lambda is a python keyword that says what follows is an anonyomous funciton
in order to call the lambda function you can load its output into a variable
and call the variable. What follows is an example of a standard function and 
then that same function using lambda.

lambda 0 or more inputs:expression

'''


# standard function
def a(x): 
  return 3*x
a(8)
#lamda function
a = lambda x: 3*x
a(8)

# hours and rate calculator - standard
def pay (hr, r):
    return hr * r
pay(8,15)

# hours and rate calculator - lambda
pay = lambda hr, r: hr *r
pay(8,15)

# Review the two lambda's below for putting first and last name together
full_name = lambda fn, ln: fn + ln
full_name("    eric    ", "IDLE")


full_name = lambda fn, ln: fn.strip().title()+" "+ ln.strip().title()
full_name("    michael     ","PALIN")

## EXERCISE 
''' 
Convert these functions into lambda functions
'''
def sum (x,y):
    return x + y
(sum(30,85))



a=10
b=5
def subtract(a, b):
   return a - b
subtract(a,b)


def divide(a, b):
    a=10
    b=5
    return a/b
divide(a,b)



# what can be beneficial is using a lambda function inside a function
def main(hr, r):
     global pay
     pay = hr * r 
     return pay
def expense():
    x = .1
    return pay * x
net = main(8,15) - expense()
(net)



def main():
    pay = lambda hr,r: hr*r
    return pay(8,15)
    expense = lambda: pay * .1
    return pay(8,15)-expense()
main()


## EXERCISE
'''
A very common calculation is finding the percentage of change or difference
There are several calcs but the most common is looking at
your new value subtracting from your old value and then dividing by the old 
value

(This year - Last year )/ Last year *100

Create a function called main that calculates this year verses last year
'''
##





# Lambda and lists
a = lambda x:x[1:3]
a([0,1,2,3,4,5,6,7])
a(['apple','pear', 'blueberry', 'banana', 'apricot'])

# sort data

#sorted(iterable,key)
list1 = ['one', 'two','three','four','five','six','seven','eight','nine','ten']
sorted(list1)
sorted(list1, key=lambda x:x[-1])
sorted(list1, key=lambda x:x[1])

# sorting tuples within lists
list2 = [(1,'one'),(2,'two'),(3,'three'),(4,'four'), (5,'five')]
sorted(list2)

# sort by the second value in the key
sorted(list2, key=lambda x:[1])


## EXERCISE
'''
create a list with tuples that put together an index skills you have learned 
and how you would rate yourself.  [(index,skill,rating),index,skill,rating]
Sort the list alphabetically by the skills. Create a seperate sort by rating
finally resort by index.
'''
##




# Map - mapping functions  with lists

'''
map will apply a function to each individual item in a list
much like a for loop
'''
#example
def uppercase(string):
    return string.upper()
values = ['abc', 'def', 'ghi']
print(list(map(uppercase, values)))

# Compare a for loop with a Map function
nums =[1,2,3,4,5,6,7,8,9]
values=[]
def squared():
    for i in nums:
        squared = i**2
        values.append(squared)
    print(values)
squared()

# map example
nums =[1,2,3,4,5,6,7,8,9]
def squared(i):
    return i**2
list(map(squared,nums))

# take this a step further with lambda
nums =[1,2,3,4,5,6,7,8,9]
list(map(lambda i: i**2,nums))

# another example
sentence = 'It is raining cats and dogs'
words = sentence.split()
(words)

lengths = list(map(lambda word: len(word), words))
(lengths)


list((map(lambda word: len(word), 'It is raining cats and dogs'.split())))




## EXERCISE
'''
Create a map function that will create title case for the following list 
of names
'''
names = ['graham','eric', 'terry', 'catherine']




# FILTER similiar to map thi asks for a function and a list
nums =[1,2,3,4,5,6,7,8,9]
def greater_than_three(x):
    return x >3
print(list(filter(greater_than_three, nums)))

##EXERCISE
# Convert the above code using lambda
##


# REDUCE
# reduce simply put can create a running total. 
nums =[1,2,3,4,5,6,7,8,9]
from functools import reduce
print(reduce(lambda x, y, x+y, nums))


##EXERCISE
'''
convert the code below into pseudocode, explaining what each piece is
'''
from functools import reduce
reduce(lambda x, y: x + y, range(4))



'''
In summary lambda, map, reduce and filter are all faster ways to write code.
to learn these functions better, try writing code the way you currently know
and then revisist your code looking for ways to improve using
comprehensions, lambda, map, reduce, filter

Try revisiting python for data I or even the previous units and look for ways
to improve the code.
'''


