class Lap:
    def __init__(self):
        self.speedX = []
        self.speedY = []
        self.speedZ = []
        self.time = 0.0 # secondi sul giro
        self.trackPos = []
        self.trackName = ""
        self.time_offtrack = 0.0 # secondi fuori pista
        self.acc = []

    def update_values(self, Sensors, R):
        self.speedX.append(Sensors['speedX'])
        self.speedY.append(Sensors['speedY'])
        self.speedZ.append(Sensors['speedZ'])
        self.trackPos.append(Sensors['trackPos'])
        self.acc.append(R['accel'])


    def set_time(self, time):
        self.time = time

    def get_time(self):
        return self.time

    def set_time_offtrack(self):
        t_off = 0.0
        for item in self.trackPos:
            if abs(item) > 0.95:
                t_off += 1
        self.time_offtrack = t_off*0.02 # tempo in secondi.

    def get_time_offtrack(self):
        return self.time_offtrack