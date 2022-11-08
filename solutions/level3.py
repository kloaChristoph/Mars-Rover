import math

def convert_input(steering_angle_str: list[str]) -> list[int]:
    steering_angle_int = []
    for value in steering_angle_str:
        if float(value) == 0 and len(steering_angle_int) % 2 == 1:
            value = 360
        steering_angle_int.append(float(value))

    return steering_angle_int

def turn_radius(wheel_base: float, steering_angle: float) -> float:
    radius: float = wheel_base/math.sin(math.radians(steering_angle))
    print (f"{radius:.2f}")

    return radius

def get_position(distance: float, radius: float) -> tuple[float,float,float]:
    angle = (distance*180)/(math.pi*radius)
    y = (math.sin(math.radians(angle)) * radius)
    x = radius - (math.cos(math.radians(angle)) * radius)

    while angle < 0:
        angle = 360 + angle
    
    if angle == 360:
        angle = 0

    print(f"{x:.2f} {y:.2f} {angle:.2f}")
    return x, y, angle

def rotate_vectore(x: float, y: float, angle: float):
    new_x = math.cos(math.radians(angle))*x + math.sin(math.radians(angle))*y
    new_y =  math.sin(math.radians(angle))*-x + math.cos(math.radians(angle))*y
    return new_x, new_y
    
def fix_angle_value(angle:float) -> float:
    while angle < 0:
        angle = 360 + angle

    while angle >= 360:
        angle = angle - 360

    return angle


if __name__ == "__main__":
    wheel_base = 0.5
    n = 3
    steering_angle_str = "10.00 0.00 500.00 3.00".split(" ")

    current_position_x = 0
    current_position_y = 0
    angle = 0

    steering_angle_int = convert_input(steering_angle_str)

    while steering_angle_int:
        distance = steering_angle_int[0]
        steering_angle = steering_angle_int[1]

        radius = turn_radius(wheel_base ,steering_angle)
        x, y, new_direction = get_position(distance, radius)
        x2, y2 = rotate_vectore(x,y,angle)

        current_position_x = current_position_x + x2
        current_position_y = current_position_y + y2

        steering_angle_int.pop(0)
        steering_angle_int.pop(0)

        angle = angle + new_direction
        
    current_position_x = round(current_position_x, 2)
    current_position_y = round(current_position_y, 2)
    angle = round(angle, 2)

    angle = fix_angle_value(angle)
    print(f"{current_position_x:.2f} {current_position_y:.2f} {angle:.2f}")
   



        


