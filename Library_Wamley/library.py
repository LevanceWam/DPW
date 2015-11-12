class Library():
    def __init__(self):
        pass
    #this is were al the math happens

    def fahrenheit_to_celsius(self,fahrenheit):#Fahrenheit to celsius
        return fahrenheit * 9 / 5 + 32

    def milliliters_to_gallons(self,milliliters):#mL to gal
        return milliliters * 0.00026417

    def gallons_to_milliliters(self,gallons):#gal to mL
        return gallons / 0.00026417

#sets all of the variables to zero so that they can be changed upon input
class Printer():
    def __init__(self):
        self.fahrenheit = 0
        self.celsius = 0
        self.milliliters = 0
        self.gallons = 0

#shows work
    def calc(self):
        print str(self.fahrenheit) + "fahrenheit = " + str(self.celsius)+ " celsius"
        print str(self.milliliters) + "mL = " + str(self.gallons)+ " gal"