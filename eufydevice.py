import lakeside
from BulbStatus import BulbStatus


class EufyDevice:
    address = ""
    code = ""
    type = ""
    name = ""
    id = ""
    bulb = lakeside.bulb
    bulb_status = ""

    def connect(self):
        self.bulb = lakeside.bulb(self.address, self.code, self.type)

    def __init__(self, address, code, type, name, id):
        self.address = address
        self.code = code
        self.type = type
        self.name = name
        self.id = id
        self.connect()
        self.update_bulb_status()

    def update_bulb_status(self):
        # self.connect()
        power = self.bulb.get_status().bulbinfo.packet.bulbstate.power
        brightness = self.bulb.get_status().bulbinfo.packet.bulbstate.values.brightness
        self.bulb_status = BulbStatus(power, brightness)

    def bulb_status(self):
        # self.connect()
        status = self.bulb.get_status().bulbinfo.packet.bulbstate.power
        if status == 0:
            status = "Off"
        else:
            status = "On"
        print(self.name + " " + status)

    def turn_on(self):
        # self.connect()
        self.bulb.set_state(power=True)

    def turn_off(self):
        # self.connect()
        self.bulb.set_state(power=False)
