class BulbStatus:
    power = ""
    brightness = ""

    def __init__(self, power, brightness):
        self.power = power
        self.brightness = brightness

    def __int__(self):
        self.power = ""
        self.brightness = ""