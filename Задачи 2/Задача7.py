import math

def distance_between_points(point_a, point_b):
    x1, y1 = point_a['x'], point_a['y']
    x2, y2 = point_b['x'], point_b['y']
    x_diff = x2 - x1
    y_diff = y2 - y1
    distance = math.sqrt(x_diff**2 + y_diff**2)

    return round(distance, 3)

point_a = {'x': 3, 'y': 4} 
point_b = {'x': 0, 'y': 0}
result = distance_between_points(point_a, point_b)
print(f"Расстояние между точками: {result}")