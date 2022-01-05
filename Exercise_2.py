l=[30,40,50]   #list of given lengths
b=20          
h=15
lis=sorted([30,40,50,b,h])   #sorting of given all inputs
big_area=lis[-1]*lis[-2]     #calculating bigget area
print('area of one of the biggest faces is ', big_area)
for i in l:                  #calculating and printing area for all the given lengths
    vol=i*b*h
    print('volume of a rectangular cuboid is with length',i,'is',vol)
