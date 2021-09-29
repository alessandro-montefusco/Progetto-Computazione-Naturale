import numpy as np
import math
import matplotlib.pyplot as plt
import pickle

'''
def plot_speed(laps):
    speeds = []
    for lap in laps:
        for j in range(lap.speedX.__len__()):
            speeds.append(math.sqrt(math.pow(lap.speedX[j], 2) + math.pow(lap.speedY[j], 2) + math.pow(lap.speedZ[j], 2)))
    chunks = [speeds[i:i+50] for i in range(0, len(speeds), 50)]
    mean_speeds = [] #velocità medie secondo per secondo
    for c in chunks:
        mean_speeds.append(float(np.sum(c)/len(c)))
    time = np.arange(0, len(mean_speeds)) # secondi nel range [0; end 2 giri]
    scaley = [] # scala delle velocità
    scalex = [] # scala del tempo
    for i in range(15):
        scaley.append(i * 20)
    for i in range(18):
        scalex.append(i * 5)
    plt.plot(time, mean_speeds, color="blue") #axis x: time - axis y: speed
    plt.title("PSO: mean velocity in CG Speedway n.1")
    #plt.title("PSO: mean velocity in Forza")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Mean velocity (km/h)")
    plt.yscale('linear')
    plt.yticks(scaley)
    plt.xticks(scalex)
    plt.show()

def plot_trackPos(laps):
    t_off = 0.0
    for lap in laps:
        t_off += lap.get_time_offtrack()
    positions = np.append(laps[0].trackPos, laps[1].trackPos)
    chunks = [positions[i:i + 3] for i in range(0, len(positions), 3)] # media di ogni 40 ms
    mean_pos = []
    for c in chunks:
        mean_pos.append(float(np.sum(c) / len(c)))
    time = np.arange(0, len(mean_pos)*60,60)

    up_bound_x = [0, len(mean_pos)*60]
    up_bound_y = [0.95, 0.95]
    down_bound_x = [0, len(mean_pos)*60]
    down_bound_y = [-0.95, -0.95]
    middle_bound_x = [0, len(mean_pos)*60]
    middle_bound_y = [0, 0]

    plt.plot(time, mean_pos, color="black")  # axis x: time - axis y: speed
    plt.plot(up_bound_x, up_bound_y, color="blue")
    plt.plot(middle_bound_x, middle_bound_y, color="red")
    plt.plot(down_bound_x, down_bound_y, color="blue")
    plt.title("Profilo di posizione di CarSim in Forza")
    plt.xlabel("Tempo (millisec)")
    legend = 'Fuori pista: '+str(round(t_off,2))+' secondi.'
    plt.legend([legend], loc='lower left')
    plt.ylabel("Posizione nella pista (metri)")
    plt.yscale('linear')
    plt.yticks(np.arange(-1.5, 7.5, 0.5))
    plt.show()
'''

path = ['laps_info/']
vars = ['carsim_']
tracks = ['forza'] #'forza'
super_list = []
for p in path:
    for v in vars:
        for t in tracks:
            info = p + v + t
            with open(info, "rb") as f:
                print(info)
                super_list.append(pickle.load(f))

i = 0
colors = ['black']# 'red', 'green']
labels = ['CarSim']# 'SADE', 'PSO']

for laps in super_list:
    t_off = 0.0
    for lap in laps:
        t_off += lap.get_time_offtrack()
    positions = np.append(laps[0].trackPos, laps[1].trackPos)
    chunks = [positions[i:i + 3] for i in range(0, len(positions), 3)]  # media di ogni 40 ms
    mean_pos = []
    for c in chunks:
        mean_pos.append(float(np.sum(c) / len(c)))
    time = np.arange(0, len(mean_pos) * 60, 60)

    up_bound_x = [0, len(mean_pos) * 60]
    up_bound_y = [0.95, 0.95]
    down_bound_x = [0, len(mean_pos) * 60]
    down_bound_y = [-0.95, -0.95]
    middle_bound_x = [0, len(mean_pos) * 60]
    middle_bound_y = [0, 0]

    plt.plot(up_bound_x, up_bound_y, color="blue")
    plt.plot(middle_bound_x, middle_bound_y, color="red")
    plt.plot(down_bound_x, down_bound_y, color="blue")

    plt.plot(time, mean_pos, label="Fuori pista " + labels[i] + ": " + str(round(t_off, 2)) + " secondi.", color=colors[i])  # axis x: time - axis y: speed
    plt.title("Profilo di posizione CarSim in Forza")


    i+=1



plt.xlabel("Tempo (millisec)")
plt.ylabel("Posizione nella pista (metri)")
plt.yscale('linear')
plt.yticks(np.arange(-3.0, 8.0, 0.5))
plt.legend(loc='lower left')
plt.show()