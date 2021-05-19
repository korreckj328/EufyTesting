# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time

from eufydevice import *
from logon_info import *
import os


def main():
    bulb_list = []
    # print("about to get devices")
    devices = lakeside.get_devices(username, password)
    # print(len(devices))
    # print("got devices successfully")
    for device in devices:
        if device.get("type") == "T1011":
            bulb = EufyDevice(device.get("address"), device.get("code"), device.get("type"), device.get("name"), device.get("id"))
            # print("bulb created")
            bulb_list.append(bulb)
    if len(bulb_list) == 0:
        print("no bulbs in bulb list")
        exit(-1)

    quit = False
    while quit == False:
        os.system("clear")
        print("Welcome to the light center")
        print("Please Select a Bulb or Q to exit")
        count = 1
        for bulb in bulb_list:
            print(count + " " + bulb.name)
            count += 1
        myinput = int(input())
        bulbscreen = True
        while bulbscreen:
            if


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
