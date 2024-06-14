# 4.1 - Def Functions - Jon Tokarz - Areas Of A Square And Circle




def area_square(side):
#    side = int(input("What is the side of the square?"))  # from my original code, this line isn't necessary
    area_square = (side * side)
    print("The area of the square is " + str(area_square) + " square units.")

def area_circle(radius):
#    radius = int(input("What is the radius of the circle?")) # also from my original code, this line isn't necessary
    area_circle = (3.14 * (radius * radius))
    print("The area of the circle is " + str(area_circle) + " square units.")


# testing the functions (def)
area_square(4)
area_circle(5)



# 4.1 - Def Functions - Jon Tokarz - Areas Of A Square And Circle