#import necessary modules
import math

pi = math.pi

class Circle:
    '''The purpose of this class is to compute the area and circumference of a circle 
    by using the given radius by the user!!!'''
        
    #method to calc circumference
    def compute_circumference(self, rad,measure):
        circumference = 2*rad*pi
        print(f"The circumference of a circle with a radius of {rad}{measure} is {round(circumference, 2)}{measure}.")

    #method to calc area
    def compute_area(self, rad, measure):
        area = pi*rad**2
        print(f"The area of a circle with a radius of {rad}{measure} is {round(area, 2)}{measure} squared.")


print('\n' + Circle.__doc__)

#Choose a measure:
measure_dict={'a':'cm',
             'b':'m',
             'c':'in',
             'd':'ft'}
print(measure_dict)

selection = input("\nChoose the measure's letter for computation: ").strip().lower()

if selection  in measure_dict:
    measure = measure_dict[selection]
else:
    print('Invalid Input')
    exit()
#get desired input
radius = float(input("\nEnter desired radius: "))

#create obj
Circle1 = Circle()

#Call necessary funcs
Circle1.compute_circumference(radius, measure)
Circle1.compute_area(radius, measure)

