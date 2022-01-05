#input of length, breadth and height of rectangular cuboid
l=int(input('Enter the value of length: '))
b=int(input('Enter the value of breadth: '))
h=int(input('Enter the value of height: '))

lis=sorted([l,b,h])  #list for sorting lenghts
big_area=lis[-1]*lis[-2]  #calculating biggest face area
volume=l*b*h  #calculating volume
print('area of one of the biggest faces is ', big_area)
print('volume of a rectangular cuboid is', volume)
