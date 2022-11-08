import math

def turn_radius(wheel_base, steering_angle):
    radius: float = wheel_base/math.sin(math.radians(steering_angle))
    print (f"{radius:.2f}")

    return radius

def get_position(distance, steering_angle, radius):
    angle = (distance*180)/(math.pi*radius)
    y = (math.sin(math.radians(angle)) * radius)
    x = radius - (math.cos(math.radians(angle)) * radius)

    while angle < 0:
        angle = 360 + angle
    
    if angle == 360:
        angle = 0

    print(f"{x:.2f} {y:.2f} {angle:.2f}")

if __name__ == "__main__":
    wheel_base = 2.7
    distance = 45
    steering_angle = -34

    if steering_angle == 0:
        steering_angle = 360

    radius = turn_radius(wheel_base ,steering_angle)
    get_position(distance, steering_angle, radius)