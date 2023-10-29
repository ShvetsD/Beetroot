from rectangle_base_area import base_area
width = int(input('Please enter the parallelepiped base width: '))
length = int(input('PLease enter the parallelepiped base length: '))
par_height = int(input('Please enter the parallelepiped height: '))
par_volume = par_height*base_area(width, length)
print(f'The parallelepiped volume is: {par_volume} m3')
