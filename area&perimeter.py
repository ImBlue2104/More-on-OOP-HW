#import necessary modules
import math

pi = math.pi

class Circle:
    '''The purpose of this class is to compute the area and circumference of a circle 
    by using the given radius by the user!!!'''
        
    #method to calc circumference
    def compute_circumference(self, rad):
        circumference = 2*rad*pi
        print(f"The circunference of a circle with a radius of {rad}{measure} is {round(circumference, 2)}{measure}")

    #method to calc area
    def compute_area(self, rad):
        area = pi*rad**2
        print(f"The circunference of a circle with a radius of {rad}{measure} is {round(area, 2)}{measure}")


print('\n' + Circle.__doc__)

#Choose a measure:
measure = input("\nChoose a measure for computation; a)cm, b)in, c)m, d)ft: ")
if measure.strip().lower() == 'a':
    measure = 'cm'
elif measure.strip().lower() == 'b':
    measure = 'in'
elif measure.strip().lower() == 'c':
    measure = 'm'
elif measure.strip().lower() == 'd':
    measure = 'ft'
else:
    print("Invalid Input!")

#get desired input
radius = int(input("\nEnter desired radius: "))

#create obj
Circle1 = Circle()

#Call necessary funcs
Circle1.compute_circumference(radius)
Circle1.compute_area(radius)

del Circle1