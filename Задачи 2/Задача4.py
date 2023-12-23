import math

def calculate_water_mass(radius, height):
    density_water = 1 
    volume_water = math.pi * radius**2 * height 
    water_mass = volume_water * density_water 
    return round(water_mass, 2)

radius_cylinder = 5 
height_cylinder = 10 

water_mass = calculate_water_mass(radius_cylinder, height_cylinder)
print(f"Масса воды в цилиндре: {water_mass} кг")