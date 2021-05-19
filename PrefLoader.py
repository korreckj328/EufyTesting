from logon_info import *
import sys
from pathlib import Path

class PrefLoader(object):
    _instance = None
    pref_path = ""

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(PrefLoader, cls).__new__(cls)
            home = str(Path.home())
            cls.pref_path = home + "/.config/Eufy_Testing.config"
            # Put any initialization here.
        return cls._instance

    def read_prefs(self):
        # pretend version
        try:
            file = open(self.pref_path, 'r')
            prefs = file.readlines()
            file.close()
            info = logon_info(user=prefs[0].strip("\n"), passwd=prefs[1])
        except:
            print("couldn't read prefs, getting info from user")
            e = sys.exc_info()[0]
            print("Error: " + str(e))
            info = self.get_prefs()
            _ = self.write_prefs(info=info)
        return info

    def write_prefs(self, info: logon_info):
        try:
            prefs = logon_info.username + "\n" + logon_info.password
            file = open(self.pref_path, 'w')
            file.write(prefs)
            file.close()
            print("prefs saved")
            return True
        except:
            print("prefs not saved successfully you will have to enter logon info next use")
            e = sys.exc_info()[0]
            print("Error: " + str(e))
            return False

    def get_prefs(self):
        user_name = input("Please Input a User Name: ")
        print()
        passwd = input("Please Input your password: ")
        print()
        info = logon_info(user=user_name, passwd=passwd)
        return info

    def load(self):
        print("Getting user preferences.")
        info = self.read_prefs()
        print("Preferences loaded successfully")
        return info
