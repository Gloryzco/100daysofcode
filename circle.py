#Python class named Circle constructed by a radius and two methods which 
#will compute the area and the perimeter of a circle.

class Circle():
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r**2*3.14
    
    def perimeter(self):
        return 2*self.r*3.14

radius = int(input("Enter the radius of the circle: "))
myCircle = Circle(radius)

#outputting the area and the perimeter

print("The area of the circle is: " + str(myCircle.area()))
print("\nThe perimeter of the circle is: " + str(myCircle.perimeter()))
