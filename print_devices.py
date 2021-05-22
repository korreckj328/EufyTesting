# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time

from eufydevice import *
from PrefLoader import *
from SupportedDevices import supported_devices


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
        if device.get("type") in supported_devices:
            try:
                bulb = EufyDevice(device.get("address"),
                                  device.get("code"),
                                  device.get("type"),
                                  device.get("name"),
                                  device.get("id"))
                print("bulb created")
                bulb_list.append(bulb)
            except:
                print("bulb creation failed")
                print("name: " + device.get("name"))
                print("type: " + device.get("type"))
        else:
            print("missing device type: " + device.get("type"))
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
