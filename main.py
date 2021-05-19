# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time

from eufydevice import *
from PrefLoader import *
import os


def main():
    login = PrefLoader().load()


    quitter = False
    while quitter == False:
        devices = lakeside.get_devices(login.username, login.password)
        bulb_list = []
        for device in devices:
            if device.get("type") == "T1011":
                bulb = EufyDevice(device.get("address"), device.get("code"), device.get("type"), device.get("name"),
                                  device.get("id"))
                # print("bulb created")
                bulb_list.append(bulb)
        if len(bulb_list) == 0:
            print("no bulbs in bulb list")
            exit(-1)
        os.system("clear")
        print("Welcome to the light center")
        print("Please Select a Bulb or Q to exit")
        count = 1
        for bulb in bulb_list:
            print(str(count) + " " + bulb.name)
            count += 1
        try:
            myinput = int(input())
            bulbscreen = True
        except:
            quitter = True
            bulbscreen = False
        while bulbscreen:
            os.system("clear")
            print("Bulb Info")
            power_str = str(bulb.bulb_status.power)
            brightness_str = str(bulb.bulb_status.brightness)
            print("Name: " + str(bulb_list[myinput - 1].name))
            print("Power: " + power_str)
            print("Brightness: " + brightness_str)
            print("1: Toggle Power")
            print("Any other selection to go back")
            try:
                myinput2 = int(input())
                if myinput2 == 1:
                    if power_str == "1":
                        bulb_list[myinput - 1].turn_off()
                    else:
                        bulb_list[myinput - 1].turn_on()
                    bulbscreen = False
                else:
                    bulbscreen = False
            except:
                bulbscreen = False



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
