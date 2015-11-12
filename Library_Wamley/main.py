import library

class MainHandler:
    def __init__(self):
        self.display = library.Printer()
        self.library = library.Library()

        fahrenheit = int(raw_input("Enter the degrees in Fahrenheit."))
        celsius = self.library.fahrenheit_to_celsius(fahrenheit)

        self.display.fahrenheit = fahrenheit
        self.display.celsius = celsius

        milliliters = int(raw_input("Enter the volume of the cup in Milliliters"))
        gallons = self.library.milliliters_to_gallons(milliliters)

        self.display.milliliters = milliliters
        self.display.gallons = gallons

        self.display.calc()
main = MainHandler()
