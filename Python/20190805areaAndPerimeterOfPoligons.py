#20190805 Calculate area and perimeter of a circle
import math 
print('Area and Perimeter Calculator')
str = "poligonType"
#poligonType = int (input('Please write 1 for circle or 2 for square and press ENTER:'))
while input != 0:
  poligonType = int (input('Please write''\n 1 for circle''\n 2 for square''\n 0 for exit''\n and press ENTER:')) 
  if poligonType == 1:
    radio = float(input ('Please write the RADIO of the circle and press ENTER:'))
    area = math.pi * pow(radio,2)
    perimeter = math.pi * 2 * radio
    print('\n Area of the circle = %0.1f' %area)
    print ('\n Perimeter of the circle = %0.1f' %perimeter)
    
  elif poligonType == 2:
    length = float (input ('Please write the LENGTH of the square and press ENTER:'))
    area = pow(length,2)
    perimeter = 4 * length
    print('\n Area of the square = %0.1f' %area)
    print ('\n Perimeter of the square = %0.1f' %perimeter)
  elif poligonType == 0:
    print('\n Have a good day!')
    break
 
