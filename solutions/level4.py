import requests


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


def drive_rover(uuid, distance, steering_angle):
    response = requests.get(f"https://rover.codingcontest.org/rover/move/{uuid}?distance={distance}&steeringAngle={steering_angle}")
    
    message = response.content.decode('utf-8').split(" ")

    match message[0]:
        case "OK":
            x = message[2]
            y = message[3]
            angle = message[4]
            return x, y, angle
    
        case "ERROR":
            print("rover crashed")
            return "rover crashed"

        case "PASS":
            passkey = message[1]
            total_distance = message[2]
            print(f"passkey: {passkey}")
            return passkey, total_distance
        
         
if __name__ == "__main__":
    map = "L4_MFJS3487"
    user = "kloaChristoph"
    contestid = "practice"

    uuid = get_uuid(map,user,contestid)
    print(uuid)

    wheel_base, max_steering_angle, target_x, target_y, target_radius = get_specification(uuid)

    drive_rover(uuid, 100, 0)
    drive_rover(uuid, -100, 0)