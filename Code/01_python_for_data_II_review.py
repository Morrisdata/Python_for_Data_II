###############################################################################
##                    READING AND WRITING TO FILES                           ##
###############################################################################
'''	
It's time to review the symbols and Python words you know and to try to pick up
 a few more for the next few lessons. I have written out all the Python symbols
 and keywords that are important to know.	
In this lesson take each keyword and first try to write out what it does from 
memory. Next, search online for it and see what it really does. This may be 
difficult because some of these are difficult to search for, but try anyway.	
If you get one of these wrong from memory, make an index card with the correct 
definition and try to "correct" your memory.	
Finally, use each of these in a small Python program, or as many as you can get
done. The goal is to find out what the symbol does, make sure you got it right, 
correct it if you do not, then use it to lock it in.	

Keyword	Description
and	Logical and.
as	Part of the with-as statement.
assert	Assert (ensure) that something is true.
break	Stop this loop right now.
class	Define a class.
continue	Don't process more of the loop, do it again.
def	Define a function.
del	Delete from dictionary.
elif	Else if condition.
else	Else condition.
except	If an exception happens, do this.
exec	Run a string as Python.
finally	Exceptions or not, finally do this no matter what.
for	Loop over a collection of things.
from	Importing specific parts of a module.
global	Declare that you want a global variable.
if	If condition.
import	Import a module into this one to use.
in	Part of for-loops. Also a test of X in Y.
is	Like == to test equality.
lambda	Create a short anonymous function.
not	Logical not.
or	Logical or.
pass	This block is empty.
print	Print this string.
raise	Raise an exception when things go wrong.
return	Exit the function with a return value.
try	Try this block, and if exception, go to except.
while	While loop.
with	With an expression as a variable do.
yield	Pause here and return to caller.
Data Types	
For data types, write out what makes up each one. For example, with strings write out how you create a string. For numbers write out a few numbers.	
Type	Description
TRUE	True boolean value.
FALSE	False boolean value.
None	Represents "nothing" or "no value".
strings	Stores textual information.
numbers	Stores integers.
floats	Stores decimals.
lists	Stores a list of things.
dicts	Stores a key=value mapping of things.
String Escape Sequences	
For string escape sequences, use them in strings to make sure they do what you think they do.	
Escape	Description
\\	Backslash
\'	Single-quote
\"	Double-quote
\a	Bell
\b	Backspace
\f	Formfeed
\n	Newline
\r	Carriage
\t	Tab
\v	Vertical tab
String Formats	
Same thing for string formats: use them in some strings to know what they do.	
Escape	Description
%d	Decimal integers (not floating point).
%i	Same as %d.
%o	Octal number.
%u	Unsigned decimal.
%x	Hexadecimal lowercase.
%X	Hexadecimal uppercase.
%e	Exponential notation, lowercase 'e'.
%E	Exponential notation, uppercase 'E'.
%f	Floating point real number.
%F	Same as %f.
%g	Either %f or %e, whichever is shorter.
%G	Same as %g but uppercase.
%c	Character format.
%r	Repr format (debugging format).
%s	String format.
%%	A percent sign.
Operators	
Some of these may be unfamiliar to you, but look them up anyway. 
Find out what they do, and if you still can't figure it out, save it for later.	
Operator	Description
+	Addition
-	Subtraction
*	Multiplication
**	Power of
/	Division
//	Floor division
%	String interpolate or modulus
<	Less than
>	Greater than
<=	Less than equal
>=	Greater than equal
==	Equal
!=	Not equal
<>	Not equal
( )	Parenthesis
[ ]	List brackets
{ }	Dict curly braces
@	At (decorators)
,	Comma
:	Colon
.	Dot
=	Assign equal
;	semi-colon
+=	Add and assign
-=	Subtract and assign
*=	Multiply and assign
/=	Divide and assign
//=	Floor divide and assign
%=	Modulus assign
**=	Power assign
Spend about a week on this, but if you finish faster that's great. 
The point is to try to get coverage on all these symbols and make sure they 

are locked in your head. What's also important is to find out what you do 
not know so you can fix it later.	
Reading Code	
Now find some Python code to read. You should be reading any Python code you 
can and trying to steal ideas that you find. You actually should have enough 
knowledge to be able to read, but maybe not understand what the code does. 
What this lesson teaches is how to apply things you have learned to understand 
other people's code.	
First, print out the code you want to understand. Yes, print it out, because 
your eyes and brain are more used to reading paper than computer screens. 
Make sure you print a few pages at a time.	
Second, go through your printout and take notes of the following:	
Functions and what they do.	
Where each variable is first given a value.	
Any variables with the same names in different parts of the program. These may 
be trouble later.	
Any if-statements without else clauses. Are they right?	
Any while-loops that might not end.	
Any parts of code that you can't understand for whatever reason.	
Third, once you have all of this marked up, try to explain it to yourself by 
writing comments as you go. Explain the functions, how they are used, what 
variables are involved and anything you can to figure this code out.	
Lastly, on all of the difficult parts, trace the values of each variable line 
by line, function by function. In fact, do another printout and write in the 
margin the value of each variable that you need to "trace."	
Once you have a good idea of what the code does, go back to the computer and 
read it again to see if you find new things. Keep finding more code and doing 
this until you do not need the printouts anymore.	
Study Drills	
Find out what a "flow chart" is and draw a few.	
If you find errors in code you are reading, try to fix them and send the 
author your changes.	
Another technique for when you are not using paper is to put # comments with 
your notes in the code. Sometimes, these could become the actual comments to 
help the next person.	
'''
###############################################################################
##                      STRINGS                               ##
###############################################################################
a ='hello'
# slicing
a[0]        # returns 'h' (works like list slicing)
a[1:3]      # returns 'el'
a[-1]       # returns 'o'

# concatenating
a + ' there'        # use plus sign to combine strings
5 + ' there'        # error because they are different types
str(5) + ' there'   # cast 5 to a string in order for this to work

# uppercasing
a[0] = 'H'      # error because strings are immutable (can't overwrite characters)
a.upper()       # string method (this method doesn't exist for lists)

# checking length
len(a)      # returns 5 (number of characters)


## EXERCISE
'''
1. Load your name into the variable a
2. Load your last name into the variable b
3. Concatenate your first and last name
4. Capitalize your name
'''
##




###############################################################################
##                          LISTS                                            ##
###############################################################################
# creating
a = [1, 2, 3, 4, 5]     # create lists using brackets

# slicing
a[0]        # returns 1 (Python is zero indexed)
a[1:3]      # returns [2, 3] (inclusive of first index but exclusive of second)
a[-1]       # returns 5 (last element)

# appending
a[5] = 6        # error because you can't assign outside the existing range
a.append(6)     # list method that appends 6 to the end
a = a + [0]     # use plus sign to combine lists

# checking length
len(a)      # returns 7

# checking type
type(a)     # returns list
type(a[0])  # returns int

# sorting
sorted(a)               # sorts the list
sorted(a, reverse=True) # reverse=True is an 'optional argument'
sorted(a, True)         # error because optional arguments must be named



# Create a shopping list with prompts
shoplist=[]
item1 = input('Enter first item1:')
item2 = input('Enter first item2:')
item3 = input('Enter first item3:')
item4 = input('Enter first item4:')
shoplist.append(item1)
shoplist.append(item2)
shoplist.append(item3)
shoplist.append(item4)
shoplist


# List is like a grocery list and a list can create a list
color = ['red', 'yellow', 'blue']
color
color.append('black')
color











###############################################################################
##               FOR LOOPS AND LIST COMPREHENSIONS  INTRO                    ##
###############################################################################
'''
FOR LOOPS AND LIST COMPREHENSIONS
'''
odd = [1, 3, 5]       # create a list
for x in odd:         # name 'x' does not matter, not defined in advance
    print(x)          # this loop only executes 3 times (not 5)

# for loop to print 1 through 5
nums = range(1, 6)    # create a list of 1 through 5
for val in nums:      # num 'becomes' each list element for one loop
    print (val)

# While loops stop when a condition is met.
shopList = [] 
maxLengthList = 6
while len(shopList) < maxLengthList:
    item = input("Enter your Item to the List: ")
    shopList.append(item)
    print (shopList)
print ("That's your Shopping List")
print (shopList)


# for loop to create a list of 2, 4, 6, 8, 10
nums = range(1, 6)
doubled = []                # create empty list to store results
for num in nums:            # loop through nums (will execute 5 times)
    doubled.append(num*2)   # append the double of the current value of num
doubled                     # Why did this go to 10?

# equivalent list comprehension
nums =range(1,6)
doubled = [num*2 for num in nums]   # expression (num*2) goes first, brackets
                                    # indicate we are storing results in a list
doubled


##EXERCISE
'''
EXERCISE 1:
Given that: letters = ['a', 'b', 'c']
Write a list comprehension that returns: ['A', 'B', 'C']
'''
##
yes = True
count = 0
while yes:
    prompt = input('Do you want to continue Y/N?')
    if prompt == 'N':
        yes = False
        print('Goodbye')
    elif prompt =='Y':
        print('Continue')
        count+=1
        print (count)
    else: 'invalid entry'
    
## EXERCISE 
'''
The above is a while loop
Create a for loop that capitalizes a list of lower case names
''''
###############################################################################
##                          LIST EXAMPLES                                    ##
###############################################################################
'''
Doing things to lists
You have learned about lists. When you learned about while-loops you 
"appended" numbers to the end of a list and printed them out. There were also 
Study Drills where you were supposed to find all the other things you can do to 
lists in the Python documentation. That was a while back, so review those 
topics if you do not know what I'm talking about.
Found it? Remember it? Good. When you did this you had a list, and you "called" 
the function append on it. However, you may not really understand what's going 
on so let's see what we can do to lists.
When you write mystuff.append('hello') you are actually setting off a chain of 
events inside Python to cause something to happen to the mystuff list. Here's 
how it works:
Python sees you mentioned mystuff and looks up that variable. It might have to 
look backward to see if you created with =, if it is a function argument, or 
if it's a global variable. Either way it has to find the mystufffirst.
Once it finds mystuff it reads the . (period) operator and starts to look at 
variables that are a part of mystuff. Since mystuff is a list, it knows that 
mystuff has a bunch of functions.
It then hits append and compares the name to all the names that mystuff says 
it owns. If append is in there (it is) then Python grabs that to use.
Next Python sees the ( (parenthesis) and realizes, "Oh hey, this should be a 
function." At this point it calls (runs, executes) the function just like 
normally, but instead it calls the function with an extra argument.
That extra argument is ... mystuff! I know, weird, right? But that's how 
Python works so it's best to just remember it and assume that's the result. 
What happens, at the end of all this, is a function call that looks 
like: append(mystuff, 'hello') 
instead of what you read which is mystuff.append('hello').
For the most part you do not have to know that this is going on, 
but it helps when you get error messages from Python like this:
$ python
Python 2.6.5 (r265:79063, Apr 16 2010, 13:57:41)
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> class Thing(object):
...     def test(message):
...             print message
...
>>> a = Thing()
>>> a.test("hello")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: test() takes exactly 1 argument (2 given)
>>>
What was all that? Well, this is me typing into the Python shell and showing 
you some magic. You haven't seen class yet but we'll get into that later. 
For now you see how Python said test() takes exactly 1 argument (2 given). 
If you see this it means that Python changed a.test("hello") 
to test(a, "hello") and that somewhere someone messed up and didn't add the 
argument for a.
This might be a lot to take in, but we're going to spend a few exercises 
getting this concept firm in your brain. To kick things off, here's an exercise 
that mixes strings and lists for all kinds of fun.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
What You Should See
$ python ex38.py
Wait there are not 10 things in that list. Let's fix that.
Adding:  Boy
There are 7 items now.
Adding:  Girl
There are 8 items now.
Adding:  Banana
There are 9 items now.
Adding:  Corn
There are 10 items now.
There we go:  ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 
'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']
Let's do some things with stuff.
Oranges
Corn
Corn
Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
Telephone#Light
What Lists Can Do
Let's say you want to create a computer game based on Go Fish. If you don't 
know what Go Fish is, take the time now to go read up on it on the internet. 
To do this you would need to have some way of taking the concept of a 
"deck of cards" and put it into your Python program. You then have to 
write Python code that knows how to work this imaginary version of a deck 
of cards so that a person playing your game thinks that it's real, even if 
it isn't. What you need is a "deck of cards" structure, and programmers call 
this kind of thing a "data structure".
What's a data structure? If you think about it, a "data structure" is just a 
formal way to structure (organize) some data (facts). It really is that simple, 
even though some data structures can get insanely complex, all they are is just
 a way to store facts inside a program so you can access them in different ways. 
 They structure data.
I'll be getting into this more in the next exercise, but lists are one of the 
most common data structures programmers use. They are simply ordered lists of 
facts you want to store and access randomly or linearly by an index. What?! 
Remember what I said though, just because a programmer said "list is a list" 
doesn't mean that it's any more complex than what a list already is in the 
real world. Let's look at the deck of cards as an example of a list:
You have a bunch of cards with values.
Those cards are in a stack, list, or list from the top card to the bottom card.
You can take cards off the top, the bottom, the middle at random.
If you want to find a specific card, you have to grab the deck and go through 
it one at a time.
Let's look at what I said:
"An ordered list"
Yes, deck of cards is in order with a first, and a last.
"of things you want to store"
Yes, cards are things I want to store.
"and access randomly"
Yes, I can grab a card from anywhere in the deck.
"or linearly"
Yes, if I want to find a specific card I can start at the beginning and go 
in order.
"by an index"
Almost, since with a deck of cards if I told you to get the card at index 19 
you'd have to count until you found that one. In our Python lists the computer 
can just jump right to any index you give it.
That is all a list does, and this should give you a way to figure out concepts 
in programming. Every concept in programming usually has some relationship to 
the real world. At least the useful ones do. If you can figure out what the 
analog in the real world is, then you can use that to figure out what the data 
structure should be able to do.
When to Use Lists
You use a list whenever you have something that matches the list data 
structure's useful features:
If you need to maintain order. Remember, this is listed order, not sorted 
order. Lists do not sort for you.
If you need to access the contents randomly by a number. Remember, this is 
using cardinal numbers starting at 0.
If you need to go through the contents linearly (first to last). Remember, 
that's what for-loops are for.
Then that's when you use a list.
Study Drills
Take each function that is called, and go through the steps for function calls 
to translate them to what Python does. For example, more_stuff.pop() 
is pop(more_stuff).
Translate these two ways to view the function calls in English. For example, 
more_stuff.pop() reads as, "Call pop on more_stuff." Meanwhile, pop(more_stuff) 
means, "Call pop with argument more_stuff." Understand how they are really the 
same thing.
Go read about "object-oriented programming" online. Confused? I was too. 
Do not worry. You will learn enough to be dangerous, and you can slowly learn 
more later.
Read up on what a "class" is in Python. Do not read about how other languages 
use the word "class." That will only mess you up.
Do not worry If you do not have any idea what I'm talking about. Programmers 
like to feel smart so they invented object-oriented programming, named it OOP, 
and then used it way too much. If you think that's hard, you should try to use 
"functional programming."
Find 10 examples of things in the real world that would fit in a list. 
Try writing some scripts to work with them.
'''
    
###############################################################################
##                          DICTIONARIES                                     ##
###############################################################################


glossary = {'>>>':'default in most shells often is a prompt to enter data',
            'argument':'extra information used to peform commands',
            'assignment':['giving a valuable to a variable', 'x=1'],
            'break': 'used to exit a for loop or a while loop',
            'oop': 'object oriented programming',
            'oop':{'block':'A secion of code that is grouped together',
            'statement':'A statement is part of a suite (a "block" of code).'},
            
            
            'class': 'a template for creating user defined objects',
            'function': ['a parametized squence of statements','def i ():'],
            'method':'a method is like a function but it runs on an object',
            'object':'Any data with state (attributes or value) and defined' \
            'behavior (methods).',
            'object oriented':'allows users to manipulate data structures ' \
            'called objects in order to build and execute programs',
            'module': 'The basic unit of code reusability in Python. A block'\
            'of code imported by some other code.' }
glossary.keys(oop)
glossary.values()
glossary['assignment']


## EXERCISE
'''
1. Continue building glossary
2. Group like terms together in a dictionary withen the dictionary
3. Build a glossary term look. Where a client can type in a word it looks it up
and then produces results from your glossary. you will need input and use of 
variables. 
##


a = prompt for client
b = dictionary[key]
b
'''
glossary('oop')












###############################################################################
##                          ARGUMENTS                                        ##
###############################################################################
# Define variables a and b
a=10
b=5

# Define function add 
def add(a, b):
    return a + b
add(a,b)
# does not have to be a and b
a=10
b=5
def add(a, b):
    return a + b
add(a,4)

# What is int doing below
a=int(input('Enter Value one :'))
b=int(input('Enter value two :'))
def add(a, b):
    return a + b
add(a,b) 


'''
Exercise:
    Create a function for first and last name
    1. Use a prompt for first name
    2. use a prompt for last name
    3. Concate the name with a space
'''


###############################################################################    
##  BONUS Dictionaries and functions with lists                              ##
###############################################################################
    
webster = {

    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}
for items in webster:
    print (webster[items]) 

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for items in a:
    if items % 2== 0:
        print (items)

## EXERCISE
'''
1. create a random list of numbers
2. Bring back only the odd numbers
3. Write into a seperate list called odd
'''
##


##EXERCISE
'''
1. Run the code below
2. Use what you have learned to document what this code is doing
'''
##
def count(numbers):
    total = 0
    for n in numbers:
        if n == 'WA':
            total = total + 1
    return total

x = ['WA', 'ID', 'OR', 'WA','NOTWA','wa', 'WASHINGTON','OR','CA','WA' ]
y = count(x)
print (y)







