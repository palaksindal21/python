Length = int(input("enter length of rectangle:")) 
Breadth = int(input(" Enter breadth of rectangle:")) 
side = int(input(" Enter side of square "))

area_of_rectangle = Length*Breadth
area_of_square = side*side

if area_of_rectangle>area_of_square :
    print(area_of_rectangle," Area of rectangle is greater") 
else : 
    print(area_of_square," Area of square is greater") 

