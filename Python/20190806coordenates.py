#20190806 Convert cartesian coordenates to polars coordinates and viceversa
import math
print ('This program converts cartesian coordinates in polars coordinates and viceversa')
while input !=0:
    coordinates = int (input ('Please write' '\n 1 : to convert cartesian coordinates to polar coordinates in radians'
                              '\n 2 : to convert cartesian coordinates to polar coordinates in degrees''\n 3 : to convert polar coordinates (theta in radians) to cartesian coordinates'
                              '\n 4 : to convert polar coordinates (theta in degrees) to cartesian coordinates''\n 0 : to exit of the program '))
    if coordinates == 1:
        x = float (input ('Please write x coordinate and press ENTER : '))
        y = float (input ('Please write Y coordinate and press ENTER : '))
        r = math.sqrt((pow (x,2)) + (pow(y,2)))
        theta = math.atan(y/x)         
        print('\n Cartesian Coordinates :')
        print('\n x : %0.10f' %x)
        print('\n y : %0.10f' %y)
        print('\n')
        print('\n Polar Coordinates : ')
        print('\n r : %0.10f' %r)
        print('\n theta : %0.10f' %theta)
        print ('\n')

    elif coordinates == 2:
        x = float (input ('Please write x coordinate and press ENTER : '))
        y = float (input ('Please write Y coordinate and press ENTER : '))
        r = math.sqrt((pow (x,2)) + (pow(y,2)))
        theta = math.atan(y/x)
        theta = theta * 180/math.pi
        print('\n Cartesian Coordinates :')
        print('\n x : %0.10f' %x)
        print('\n y : %0.10f' %y)
        print('\n')
        print('\n Polar Coordinates : ')
        print('\n r : %0.10f' %r)
        print('\n theta : %0.10f' %theta)
        print ('\n')        
    elif coordinates == 3:
        r = float (input ('Please write r coordinate and press ENTER : '))
        theta = float (input ('Please write theta angle in radian and press ENTER : '))
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        print('\n Polar Coordinates : ')
        print('\n r : %0.10f' %r)
        print('\n theta : %0.10f' %theta)
        print ('\n')
        print('\n Cartesian Coordinates (radian):')
        print('\n x : %0.10f' %x)
        print('\n y : %0.10f' %y)
        print('\n')
    elif coordinates == 4:
        r = float (input ('Please write r coordinate and press ENTER : '))
        theta = float (input ('Please write theta angle in degrees and press ENTER : '))
        theta = theta * math.pi/180
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        print('\n Polar Coordinates : ')
        print('\n r : %0.10f' %r)
        print('\n theta : %0.10f' %theta)
        print ('\n')
        print('\n Cartesian Coordinates (radian):')
        print('\n x : %0.10f' %x)
        print('\n y : %0.10f' %y)
        print('\n')
    elif coordinates == 0:
        print('Have a good day!!!')
        break
        
        
