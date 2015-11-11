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


