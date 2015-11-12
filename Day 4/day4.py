import random
class Soda():
    def __init__(self, n):
        self.color = ""
        self.name = n
        self.id = random.randrange(0,100000)
        brand = "Pepsi"

        def explode(self):
            print self.color

        def fizz(self):
            pass


dew = Soda("Dew")
print dew.name

dr = Soda("dr. Pepper")
print dr.name
pallet = []
for i in range(100):
    soda = Soda("Mountain Dew")
    pallet.append(soda)
    print str[i]+" "+ soda.name+" "+ str(soda.id)
print "the id  of the 10th soda is: "+ str(pallet[9].id)

class Bird(object):
    def __init__(self, n):
        print "Bird Created"
        self.name = n
        self.size = ""

    def fly(self):
        return self.name + " is flying."

class Duck(Bird):
    def __init__(self, n):
        print "Duck Created"
        super(Duck, self).__init__(n)
        # print super(Duck, self).fly() this works too
        self.wings = True
    def quack(self):
        return self.name + " is quacking!"


class Daffy(Duck):
    def __init__(self):
        self.movies = "Space Jam"
        super(Daffy,self).__init__()

duck = Duck("Daffy")
print duck.name
print duck.quack()
print duck.fly()

import random

# x = 4
# y = 2
# z = 3
# w = 5
#
# total = x + y + z
# avg = total / 3
#
# print avg
#
# def get_avg(amount):
#     total = 0
#     for i in amount:
#         total+= i
#
#     avg = total / len(amount)
#     return avg
#
# print get_avg([10,20,30])

class Dog:
    def __init__(self):
        print "Dog Created"
        self.color = ""
        self.name = ""
        self.age = 0
    def bark(self):
        return "Woof!"

# my_dog = Dog()
# # dog2 = Dog()
# my_dog.name = "Max"
# print my_dog.name
#
# joesDog = Dog()
# joesDog.name = "Oscar"
# print joesDog.name

kenel = []
names = ["fido", "rover", "coco", "marley", "snoopy"]
for d in range(100):
    dog = Dog()
    dog.name = names[random.randrange(0, len(names))]
    kenel.append(dog)
    print dog.name
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

ice_cream = raw_input("What's your flavor: ")

print "Tom was walking down the street and wanted a "+ice_cream+" Ice cream cone"

friends = ["Monster", "T-Rex", "Jello"]
print "Tom's friends wanted Ice cream too and they all had the same amount of money, Tom already has $5.00"

for f in friends:
    print f + ", Has $2.00 on with them."

quest = raw_input("Please put in a random word: ")
print "The group decided to go to "+quest+ ", for Ice cream"

print "At "+quest+" their ultimate Ice cream  Sundae cost $25"
print "Tom know's that he has money in his piggy bank but can't remember how much was in there but he know's it's no greater than 5"
print "Tom's friends also have some extra money but they have $2 less than he has"
print "Tom goes and checks the piggy bank"

#
piggy = raw_input("How much money was in the bank: ")
piggy = int(piggy)
if 5 < piggy:
    raw_input("Please check again")
else:
    print "Tom has $" + str(piggy)
#function to find how much money toms friends have
    def all (a):
        b = a - 2
        return b
#toms friends money
returnb = all(piggy)
print "Tom's friends individually have $" + str(returnb)

#All of toms friends money all together
extra_friend_money_all = int(returnb) * 3 + 6
print extra_friend_money_all

tom_money_all = int(piggy) + 5

print "after going counting all of the money Tom had $"+str(tom_money_all)+", and his friends had $"+str(extra_friend_money_all)

tom_money_all
print "When they added it together it totaled out to $"+str(final_amount)
final_amount = int(final_amount)

if final_amount < 25 or None:
    print"Sorry No Ice cream for you"
else:
    print"Yay For Ice Cream"






