# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time

from eufydevice import *
from PrefLoader import *

def main():
    bulb_list = []
    print("about to get devices")
    login = PrefLoader().load()
    print(login.username)
    print(login.password)
    devices = lakeside.get_devices(login.username, login.password)
    print(len(devices))
    print("got devices successfully")
    for device in devices:
        if device.get("type") == "T1011":
            bulb = EufyDevice(device.get("address"), device.get("code"), device.get("type"), device.get("name"), device.get("id"))
            print("bulb created")
            bulb_list.append(bulb)
    if len(bulb_list) == 0:
        print("no bulbs in bulb list")
        exit(-1)
    for bulb in bulb_list:
        print(bulb.name)
        power_str = str(bulb.bulb_status.power)
        brightness_str = str(bulb.bulb_status.brightness)
        print("Power: " + power_str)
        print("Brightness: " + brightness_str)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
