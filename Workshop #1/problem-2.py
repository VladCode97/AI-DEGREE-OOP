import math

def calculate_perimeter_circle() -> float:
    input_circle: float = float(input('Type the radius of the circle: '))
    return 2 * math.pi * input_circle

def calculate_area_rectangle() -> float:
    input_width_rectangle:float =  float(input('Type the width of the rectangle or square: '))
    input_length_rectangle:float =  float(input('Type the length of the rectangle or square: '))
    return input_width_rectangle * input_length_rectangle

def calculate_volume_cube() -> float:
    #Pedir la base, la altura y la profundidad de un cubo y mostrar por consola el volumen de este.
    input_width_rectangle:float =  float(input('Type the base of the cube: '))
    input_height_rectangle:float =  float(input('Type the height of the cube: '))
    input_depth_rectangle:float =  float(input('Type the depth of the cube: '))
    return input_width_rectangle * input_height_rectangle * input_depth_rectangle

def geometric_figures() -> None:
    while(True):
        input_figure = input('Choose the type of calculation you want to do(circle, rectangle, cube or close): ').lower()
        if(input_figure == 'circle' ):
            print(f'The perimeter of a circle is: {calculate_perimeter_circle()}')
        elif(input_figure == 'rectangle'):
            print(f'The area of a circle is: {calculate_area_rectangle()}')
        elif(input_figure == 'cube'):
            print(f'The volume of the cube is: : {calculate_volume_cube()}')
        elif(input_figure == 'close'):
            break



geometric_figures()
