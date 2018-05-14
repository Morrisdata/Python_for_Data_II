###############################################################################
##                 OBJECT ORIENTED PROGRAMMING (OOP)                         ##
##        1. PROCEDURAL PROGRAMMING BRANCHES AND FUNCTIONS                   ##
##        2. CLASSES                                                         ##
##        3. METHODS                                                         ##
##        4. INHERITANCE                                                     ##
##        5. ENCAPSULATION                                                   ##
###############################################################################


###############################################################################
##                 BRANCHES AND FUNCTIONS                                    ##
###############################################################################

from sys import exit


def gold_room():
    print ("This room is full of gold.  How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print ("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")
def bear_room():
    print ("There is a bear here.")
    print ("The bear has a bunch of honey.")
    print ("The fat bear is in front of another door.")
    print ("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print ("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print ("I got no idea what that means.")


def cthulhu_room():
    print ("Here you see the great evil Cthulhu.")
    print ("He, it, whatever stares at you and you go insane.")
    print ("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print (why), ("Good job!")
    exit(0)

def start():
    print ("You are in a dark room.")
    print ("There is a door to your right and left.")
    print ("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()


###############################################################################
##                           CLASSES                                        ##
###############################################################################
'''
Zoltek

Class - a way we can model an object using a programming language
Objects - noun - a person, place or thing
Attributes - are the properties of an object
Car - make, model, year, color
Actions - Car - accelerate, brake, turn right, turn left
User Action - change the oil, drive, wash ...
'''

#class
class Car:
    #attributes
    make = ""
    model = ""
    year = ""
    color = ""
    # initialize the attributes using a function(constructor)
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def __str__(self):
        return self.make + "n" + self.model + "n" + self.year + "n" + self.color



###############################################################################
##                           METHODS                                         ##
###############################################################################
'''
METHOD - a function that is attatched to an object methods belong to and are 
defined in a class Example the length method returns the number of characters
in a string
'''
#class
class Car:
#attributes
    make = ""
    model = ""
    year = ""
    color = ""
    isMoving = False
# initialize the attributes using a function(constructor)
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def __str__(self):
        return self.make + "n" + self.model + "n" + self.year + "n" + self.color
#methods
    # Define Actions
    def accelerate(self):
        print("Car is speeding up")
        self.isMoving = True
    def brake(self):
        if self.isMoving:
            print("Car is slowing down")
            self.isMoving = False
        else:
            print("Car is already stopped")
    def turnLeft(self):
        print("Car is turning left")
    def turnRight(self):
        print("Car is turning right")
    # Define User Actions
    def changeOil(self):
        print("Car oil has been changed")
###############################################################################
##                     ENCAPSULATION                                         ##
###############################################################################
        # dounder - double underscore
'''
The idea behind encapsulation is locking variables to only be accessible inside
of a class and not outside. 
Lets imagine you are looking at a car. 
you would be able to see the car and its features and possible even be abl
to change some of them. However, you would not be able to see everything about
the car some things will be hidden and probably better if you did not get in 
and start changing for safety reasons. This is similiar to encapsulation. 

Going a step further imagine you are driving your car and you come to a red 
light. When you step on the brake that is all you really need to know, you do
not need to know the inner workings of the break. 

-Private __sportsCar - Access only you - in a safe you have the combination

-Protected _sportsCar - Access you and and

-Public sportsCar


This is known as setting variables to private but using a dunder at the start
of a variable.
#class
class Car:
#attributes
    __make = ""
    __model = ""
    __year = ""
    __color = ""
    __isMoving = False
        
'''        
        
###############################################################################
##                     INHERITANCE                                           ##
###############################################################################
# When you do an inheritance, the child class has an is-a relationship with the 
        # parent
class Animal: #Parent class
    pass
class Mammel(Animal): #Children class
    pass
class Bird(Animal):
    pass

#class
class Car:
#attributes
    make = ""
    model = ""
    year = ""
    color = ""
    isMoving = False
# initialize the attributes using a function(constructor)
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def __str__(self):
        return self.__make + "n" + self.__model + "n" + self.__year + "n" + self.__color
#methods
    # Define Actions
    def accelerate(self):
        print("Car is speeding up")
        self.isMoving = True
    def brake(self):
        if self.isMoving:
            print("Car is slowing down")
            self.isMoving = False
        else:
            print("Car is already stopped")
    def turnLeft(self):
        print("Car is turning left")
    def turnRight(self):
        print("Car is turning right")
    # Define User Actions
    def changeOil(self):
        print("Car oil has been changed")

class SportCar(Car):
    def __init__(self,make, model, year, color):
        self._Car__make = make
        self._Car__model = model
        self._Car__year = year
        self._Car__color = color
    def tune(self):
        print("Car's performance is now optimal")
        
        
###############################################################################
##                     ENCAPSULATION                                         ##
###############################################################################        
        
        
        
        Encapsulation
-This is the idea that Classes have objects and methods that work only withen
that class, 


instance - when you create a class - the wheel is created!

def - a function of the class - what does the wheel do?

self

inheritance - class inherits traits from another class 
            - make this wheel like that  previous wheel but  bigger

composition -class composed of classes - make this car from wheels, engine, seats, sunroof

attribute

is-a

has-a



object Two meanings: 
the most basic type of thing, 
and any instance of some thing.	


self 
Inside the functions in a class, self is a variable for the 
instance/object being accessed.	


attribute 	
A property classes have that are from composition and are 
usually variables.	

is-a	
A phrase to say that something inherits from another, as in a 
"toyota" is-a "car."	

has-a	
A phrase to say that something is composed of other things or has a 
trait, as in "a toyota has-a trunk."	
	
	
Phrase Drills	

Next I have a list of Python code snippets on the left, 
and the English sentences for them:	

class X(Y)	
	"Make a class named X that is-a Y."	

class X(object): def __init__(self, J)	
	"class X has-a __init__ that takes self and J parameters."	
class X(object): def M(self, J)	
    "class X has-a function named M that takes self and J parameters."	

foo = X()	
	"Set foo to an instance of class X."	

foo.M(J)	
	"From foo get the M function, and call it with parameters self, J."	

foo.K = Q	
	"From foo get the K attribute and set it to Q."	


In each of these where you see X, Y, M, J, K, Q, and foo you can treat those 
like blank spots. For example, I can also write these sentences as follows:	
	"Make a class named ??? that is-a Y."	
	"class ??? has-a __init__ that takes self and ??? parameters."	
	"class ??? has-a function named ??? that takes self and ??? parameters."	
	"Set foo to an instance of class ???."	
	"From foo get the ??? function, and call it with self=??? and parameters ???."	
	"From foo get the ??? attribute and set it to ???."	
	Again, write these on some flash cards and drill them. 
    Put the Python code snippet on the front and the sentence on the back. 
    You have to be able to say the sentence exactly the same every time 
    whenever you see that form. Not sort of the same, but exactly the same.	
	
Combined Drills	
	The final preparation for you is to combine the words drills with the 
    phrase drills. What I want you to do for this drill is this:	
	Take a phrase card and drill it.	
	Flip it over and read the sentence, and for each word in the sentence 
    that is in your words drills, get that card.	
	Drill those words for that sentence.	
	Keep going until you are bored, then take a break and do it again.	
	A Reading Test	
	I now have a little Python hack script that will drill you on these words 
    you know in an infinite manner. This is a simple script you should be able 
    to figure out, and the only thing it does is use a library called urllib 
    to download a list of words I have. Here's the script, which you should 
    enter into oop_test.py to work with it:	
'''
import random
from urllib import urlopen
import sys
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

"PHRASES = {
"class %%%(%%%):":
"Make a class named %%% that is-a %%%.",
"class %%%(object):\n\tdef __init__(self, ***)" :
"class %%% has-a __init__ that takes self and *** parameters.",
"class %%%(object):\n\tdef ***(self, @@@)":
"class %%% has-a function named *** that takes self and @@@ parameters.",
	15	    "*** = %%%()":
	16	      "Set *** to an instance of class %%%.",
	17	    "***.***(@@@)":
	18	      "From *** get the *** function, and call it with parameters self, @@@.",
	19	    "***.*** = '***'":
	20	      "From *** get the *** attribute and set it to '***'."
	21	}
	22	
	23	# do they want to drill phrases first
	24	if len(sys.argv) == 2 and sys.argv[1] == "english":
	25	    PHRASE_FIRST = True
	26	else:
	27	    PHRASE_FIRST = False
	28	
	29	# load up the words from the website
	30	for word in urlopen(WORD_URL).readlines():
	31	    WORDS.append(word.strip())
	32	
	33	
	34	def convert(snippet, phrase):
	35	    class_names = [w.capitalize() for w in
	36	                   random.sample(WORDS, snippet.count("%%%"))]
	37	    other_names = random.sample(WORDS, snippet.count("***"))
	38	    results = []
	39	    param_names = []
	40	
	41	    for i in range(0, snippet.count("@@@")):
	42	        param_count = random.randint(1,3)
	43	        param_names.append(', '.join(random.sample(WORDS, param_count)))
	44	
	45	    for sentence in snippet, phrase:
	46	        result = sentence[:]
	47	
	48	        # fake class names
	49	        for word in class_names:
	50	            result = result.replace("%%%", word, 1)
	51	
	52	        # fake other names
	53	        for word in other_names:
	54	            result = result.replace("***", word, 1)
	55	
	56	        # fake parameter lists
	57	        for word in param_names:
	58	            result = result.replace("@@@", word, 1)
	59	
	60	        results.append(result)
	61	
	62	    return results
	63	
	64	
	65	# keep going until they hit CTRL-D
	66	try:
	67	    while True:
	68	        snippets = PHRASES.keys()
	69	        random.shuffle(snippets)
	70	
	71	        for snippet in snippets:
	72	            phrase = PHRASES[snippet]
	73	            question, answer = convert(snippet, phrase)
	74	            if PHRASE_FIRST:
	75	                question, answer = answer, question
	76	
	77	            print question
	78	
	79	            raw_input("> ")
	80	            print "ANSWER:  %s\n\n" % answer
	81	except EOFError:
    print "\nBye"
	Run this script and try to translate the "object-oriented phrases" into English translations. You should see that the PHRASES dict has both forms and you just have to enter the correct one.	
	Practice English to Code	
	Next you should run the script with the "english" option so that you drill the inverse operation:	
	$ python oop_test.py english	
	Remember that these phrases are using nonsense words. Part of learning to read code well is to stop placing so much meaning on the names used for variables and classes. Too often people will read a word like "Cork" and suddenly get derailed because that word will confuse them about the meaning. In the above example, "Cork" is just an arbitrary name chosen for a class. Don't place any other meaning on it, and instead treat it like the patterns I've given you.	
	Reading More Code	
	You are now to go on a new quest to read even more code, to read the phrases you just learned in the code you read. You will look for all the files with classes, and then do the following:	
	For each class give its name and what other classes it inherits from.	
	Under that, list every function it has and the parameters they take.	
	List all of the attributes it uses on its self.	
	For each attribute, give the class this attribute is.	
	The goal is to go through real code and start learning to "pattern match" the phrases you just learned against how they're used. If you drill this enough you should start to see these patterns shout at you in the code whereas before they just seemed like vague blank spots you didn't know.	






###############################################################################
##    CLASSES
###############################################################################

Classes
class Employee:
    pass
emp_1 = Employee()
emp_2 = Employee()
print(emp_1)
print(emp_2)

emp_1.first = 'Corey'
emp_1.last = 'Shafer'
emp_1.email = 'Corey.Shafer@gmail.com'
emp_1.pay= 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@gmail.com'
emp_2.pay= 60000
print (emp_1.email)
print (emp_2.email)


a better way

class Employee:
        def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = pay
            self.email = first + '.' + last + '@company.com'
emp_1 = Employee('Corey', 'Shafer', 50000 )
emp_2 = Employee('Test', 'User', 60000)

print (emp_1.email)
print (emp_2.email)

print('{}{'.format()})

#Classes putting functions together for use in other projects
class myClass():
    def method1(self):
        print "myClass method1"
    def method2(self, someString):
        print "myclass method2: "+ someString
        
# class that inherits from other classes
class anotherClass(myClass):
    def method2(self):
        print "anotherClass method2"
    def method1(self):
        myClass.method1(self)
        print "anotherClass method1"
        
def main():
        #exercise the class methods
    c= myClass()
    c.method1()
    c.method2("This is a string")
    c2 = anotherClass()
    c2.method1()
    c2.method2("different string")

if __name__ == "__main__":
  main()








###############################################################################
## DESIGN DEBUG                                                              ##
###############################################################################
'''
Designing and Debugging
Now that you know if-statements, I'm going to give you some rules for for-loops
 and while-loops that will keep you out of trouble. I'm also going to give you 
some tips on debugging so that you can figure out problems with your program. 
Finally, you will design a little game similar to the last exercise, but with a
slight twist.
Rules for If-Statements
Every if-statement must have an else.
If this else should never run because it doesn't make sense, then you must use 
a die function in the elsethat prints out an error message and dies, 
just like we did in the last exercise. This will find many errors.
Never nest if-statements more than two deep and always try to do them one deep.
Treat if-statements like paragraphs, where each if-elif-else grouping is like a
set of sentences. Put blank lines before and after.
Your boolean tests should be simple. If they are complex, move their 
calculations to variables earlier in your function and use a good name for 
the variable.
If you follow these simple rules, you will start writing better code than most 
programmers. Go back to the last exercise and see if I followed all of these 
rules. If not, fix my mistakes.
Warning
Never be a slave to the rules in real life. For training purposes you need to 
follow these rules to make your mind strong, but in real life sometimes these 
rules are just stupid. If you think a rule is stupid, try not using it.
Rules for Loops
Use a while-loop only to loop forever, and that means probably never. This only
applies to Python; other languages are different.
Use a for-loop for all other kinds of looping, especially if there is a fixed 
or limited number of things to loop over.
Tips for Debugging
Do not use a "debugger." A debugger is like doing a full-body scan on a 
sick person. You do not get any specific useful information, and you find a 
whole lot of information that doesn't help and is just confusing.
The best way to debug a program is to use print to print out the values of 
variables at points in the program to see where they go wrong.
Make sure parts of your programs work as you work on them. Do not write massive 
files of code before you try to run them. Code a little, run a little, fix a 
little.
Homework
Now write a similar game to the one that I created in the last exercise. It can 
be any kind of game you want in the same flavor. Spend a week on it making it 
as interesting as possible. For Study Drills, use lists, functions, and modules 
(remember those from Exercise 13?) as much as possible, and find as many new 
pieces of Python as you can to make the game work.

Before you start coding you must draw a map for your game. Create the rooms, 
monsters, and traps that the player must go through on paper before you code.
Once you have your map, try to code it up. If you find problems with the map 
then adjust it and make the code match.
The best way to work on a piece of software is in small chunks like this:
On a sheet of paper or an index card, write a list of tasks you need to 
complete to finish the software. This is your to do list.
Pick the easiest thing you can do from your list.
Write out English comments in your source file as a guide for how you would 
accomplish this task in your code.
Write some of the code under the English comments.
Quickly run your script so see if that code worked.
Keep working in a cycle of writing some code, running it to test it, and fixing 
it until it works.
Cross this task off your list, then pick your next easiest task and repeat.
This process will help you work on software in a methodical and consistent 
manner. As you work, update your list by removing tasks you don't really need 
and adding ones you do.
'''


#Use a loop over a list of abbreviated day names

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for d in days:
     print d


# use hte break and continue statements
def main():
    x = 0

for x in range(5,10):
    #if (x == 7): break # breaks an execution of a loop if a condition is made
    if (x % 2 == 0): continue #if x divided by 2 = zero, dont end start back 
    #at top this will skip even numbers
    print x
if __name__ == "__main__":
    main()

#using enumerate() function to get index
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for i, d in enumerate(days):
    print i,d
if __name__ == "__main__":
  main() 



