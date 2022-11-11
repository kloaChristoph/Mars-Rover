import requests
import json


def get_uuid(map:str, user:str, contestid:str) -> str:
    response = requests.get(f"https://rover.codingcontest.org/rover/create?map={map}&username={user}&contestId={contestid}")

    uuid = response.content.decode('utf-8')
    return uuid

def get_specification(uuid: str):
    response = requests.get(f"https://rover.codingcontest.org/rover/{uuid}")

    specification = response.content.decode('utf-8').split(" ")


    wheel_base = int(specification[0])
    max_steering_angle = int(specification[1])
    target_x = int(specification[2])
    target_y = int(specification[3])
    target_radius = int(specification[4])
    return specification



if __name__ == "__main__":
    map = "L4_MFJS3487"
    user = "kloaChristoph"
    contestid = "practice"

    uuid = get_uuid(map,user,contestid)
    print(uuid)

    specification = get_specification(uuid)

    print(specification)