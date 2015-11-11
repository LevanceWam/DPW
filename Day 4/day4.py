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




