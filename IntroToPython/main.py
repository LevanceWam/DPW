# variables
first_name = "Vance"
last_name = "Wamley"
year_born = 1999

# print first_name +" "+ last_name

#casting;
#str(x) converts x to string
#int(x) converts x to interger
# print "you are " + str(2015 - year_born) + " years old"


#Conditionals Statements

# if year_born < 1994:
#     print "they are old enough to embibe"
# elif year_born < 1996:
#     print "I WANT FOOD!"
# else:
#     print "too young for anything"

# Logical Operators
parents_with_them = True
# && and
# || or
# ! not

if year_born < 1994 or parents_with_them:
    print "they can drink"

# Loops
# no ++ or -- in python, instead use += -=
# for NUM in range(start,stop,inc amt)

students = ["Lindsay", "Clay", "James", "John", "Sergej", "Sean", "Vance", "Selena"]
students.append("Karl")

# for i in range(0,9):
#     print students[i]+", you are going to do awesome in this class!"
    #print "hello There!"
    #print "happy birthday"

# for s in students:
#     print s + ", you are going to do awesomr in this class"
#
# i=0
# while i<9:
#     print students[i]
#     i+=1

# dictionary
# dictionary name = {'key': value, 'key':value}
student_movie = {'Selena':'American History X','James':"The Patriot", 'Clay':"Bourne Identify"}
# print student_movie['Selena']

# Functionns
def area(x,y):
    a = x * y
    print a
# area(20, 60)
#function invocation

#User Input
# age = raw_input("Please enter your age: ")
# print str(2015 - int(age)) + ", was the year you were born"
# print name + ", it is very nice to meet you!"

names = ['vance', 's', 'e', 'd']
print names[2]