import requests
import math


def get_uuid(map:str, user:str, contestid:str) -> str:
    response = requests.get(f"https://rover.codingcontest.org/rover/create?map={map}&username={user}&contestId={contestid}")

    uuid = response.content.decode('utf-8')
    return uuid


def get_specification(uuid: str):
    response = requests.get(f"https://rover.codingcontest.org/rover/{uuid}")

    specification = response.content.decode('utf-8').split(" ")

    wheel_base = float(specification[0])
    max_steering_angle = float(specification[1])
    target_x = float(specification[2])
    target_y = float(specification[3])
    target_radius = float(specification[4])
    return wheel_base, max_steering_angle, target_x, target_y, target_radius


def get_radius(target_x, target_y):
    s = math.sqrt(target_x**2 + target_y**2)
    alpha = math.degrees(math.atan(target_y/target_x))
    gamma = 90 - alpha
    d = s/math.sin(math.radians(gamma))
    turn_radius = d/2
    return turn_radius


def get_steering_angle(turn_radius,wheel_base, max_steering_angle):
    steering_angle = math.degrees(math.asin(wheel_base/turn_radius))

    if -max_steering_angle <= steering_angle and steering_angle <= max_steering_angle:
        return steering_angle
    else:
        print("Cant reach this point with one move")
        exit()

        
def get_distance(turn_radius, target_x, target_y):
    alpha = math.degrees(math.atan(target_y/target_x))

    angle = 180 - 2*alpha

    distance = math.pi * turn_radius * angle/180
    return distance


def check_distance(distance:float) -> list[float]:
    remaining_distances = []

    while distance:

        if distance > 100:
            distance = distance - 100
            distance_to_drive = 100
            remaining_distances.append(distance_to_drive)
        
        elif distance < -100:
            distance = distance + 100
            distance_to_drive = -100
            remaining_distances.append(distance_to_drive)

        else:
            remaining_distances.append(distance)
            distance = 0
    return remaining_distances


def drive_rover(uuid, distance, steering_angle):
    response = requests.get(f"https://rover.codingcontest.org/rover/move/{uuid}?distance={distance}&steeringAngle={steering_angle}")
    
    message = response.content.decode('utf-8').split(" ")

    match message[0]:
        case "OK":
            print(f"rover drove {message[1]}m")
            return
    
        case "ERROR":
            error_message = " ".join(message[1:])
            print(error_message)
            return 

        case "PASS":
            passkey = message[1]
            total_distance = message[2]
            print(f"passkey: {passkey}")
            return passkey


if __name__ == "__main__":
    map = "L5_MAF3401R"
    user = "kloaChristoph"
    contestid = "practice"

    uuid = get_uuid(map,user,contestid)
    print(uuid)

    wheel_base, max_steering_angle, target_x, target_y, target_radius = get_specification(uuid)
    print(wheel_base, max_steering_angle, target_x, target_y, target_radius)

    turn_radius = get_radius(target_x,target_y)

    steering_angle = get_steering_angle(turn_radius, wheel_base, max_steering_angle)
    distance = get_distance(turn_radius,target_x,target_y)

    remaining_distances = check_distance(distance)

    for distance in remaining_distances:
        drive_rover(uuid, distance, steering_angle)