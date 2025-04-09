#First we create the Circle class, setting the attribute __pi and creating the __init__ method
class Circle:
    __pi = 3.14 # class attribute

    def __init__(self,diameter):
        self.diameter = diameter
        self.radius = diameter / 2 # We will be given the diameter, so the radius will be the diameter divided by 2

    def calculate_circumference(self): # method that calculates the circumference (обиколка)
        return Circle.__pi * self.diameter

    def calculate_area(self): #the method that calculates and returns the area of the circle
        return Circle.__pi * self.radius * self.radius

    def calculate_area_of_sector(self,angle):  #the method that calculates the area of a particular sector
        return (angle/360) * Circle.__pi * self.radius * self.radius