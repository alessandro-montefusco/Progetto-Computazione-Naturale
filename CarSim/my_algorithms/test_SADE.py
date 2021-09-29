import matplotlib.pyplot as plt
import numpy as np
import os
import pickle
import json

def get_data(path):
    with open(path, 'r') as f:
        my_list = []
        list_gbst = []
        righe = f.readlines()
        for index in range(0, len(righe), 2):
            elems = righe[index].split(" ")
            if len(elems) == 5:
                my_elem = elems[4]
                gbest = elems[3]
            else:
                my_elem = elems[3]
                gbest = elems[2]
            list_gbst.append(float(gbest))
            my_list.append((float(my_elem)))
    return (list_gbst, my_list)

def get_cr(path):
    with open(path, 'r') as f:
        list_cr = []
        righe = f.readlines()
        for index in range(0, len(righe), 2):
            elems = righe[index+1].split(" ")
            if len(elems) == 5:
                cr = elems[3]
            else:
                cr = elems[2]
            list_cr.append(float(cr))
    return list_cr

sade_f = ["../results/PSO/evoluzione_2/Pso_fit_2/"]
file_name = ["console_log_seed_","_variant"]

variants = ["lbest"]

seeds = []
for i in range(5):
 seeds.append(i+1)

super_list = []
means = []
means2 = []
means3 = []
stds = []
super_gbest = []
super_speed = []

for sade in sade_f:
    for var in variants:
        for seed in seeds:
            path = sade + file_name[0] + str(seed) + file_name[1] + str(var) + ".txt"
            super_list.append(get_cr(path))
            gbest, speed = get_data(path)
            super_gbest.append(gbest)
            super_speed.append(speed)

print(len(super_speed[1]))


for i in range(len(variants)):
    tmp_list = super_gbest[i * 5: (i + 1) * 5]
    tmp_list2 = super_speed[i * 5: (i + 1) * 5]
    tmp_list3 = super_list[i * 5: (i + 1) * 5]

    tmp_np = np.array(tmp_list)
    tmp_np2 = np.array(tmp_list2)
    tmp_np3 = np.array(tmp_list3)

    means.append(np.mean(tmp_np, axis=0))
    means2.append(np.mean(tmp_np2, axis=0))
    means3.append(np.mean(tmp_np3, axis=0))

    #stds.append(np.std(tmp_np, axis=0))

colors = ['orange'] # 9
labels = ['Fattore F', 'Fattore CR'] # 9

plt.figure(figsize=(8,5))
for i in range(len(colors)):
    plt.title("Andamento medio di mean lbest in PSO con fitness " + chr(966) + "2")
    #plt.plot(means[i] + stds[i], color='yellow')
    #plt.plot(means[i] - stds[i], color='yellow')

    #plt.plot(means[i], label='gbest' , color ='orange')
    #plt.plot(means2[i], label='Mean Vel.', color='green')
    plt.plot(means3[i], label='Avg lbest.', color='blue')


plt.grid()
plt.xlabel("Generazioni")
plt.ylabel("Andamento medio su 5 trial")
plt.legend(loc='upper right')
plt.show()






'''
#print(means[0])
with open("../results/PSO/evoluzione_2/Pso_fit_2/analisi.txt","w") as analisi:
    for i in range(len(means)):
        analisi.write(str(means[i]))

#tmp_str = ["Sade_variant7_fit1", "Sade_variant8_fit1","Sade_variant9_fit1"]


sade = []
pso = []

plt.title("SADE vs PSO - fitness 2")
plt.plot(sade, label="SADE", color='blue')
plt.plot(pso, label="PSO", color='orange')

plt.grid()
plt.xlabel("# Generazioni")
plt.ylabel("Fitness media su 5 trial")
plt.legend()
plt.savefig("sade2_vs_pso2.png")
plt.show()


for sade in sade_f:
    for var in variants:
        for seed in seeds:
            path = sade + "/" + file_name[0] + str(seed) + file_name[1] + str(var) + ".txt"
            super_list.append(path)

for path in super_list:
    pfile = open(path, 'r')
    P = json.load(pfile)
    i = 0
    for key in P:
        sample.append(P[key])
        i = i + 1
    samples.append(sample)
    sample = []

i = 0
tmp_list = samples[i * 5: (i + 1) * 5]
tmp_np = np.array(tmp_list)
#print(tmp_np,"\n\n")
sample.append(np.mean(tmp_np, axis=0))
sample = sample[0]

print(sample)
i = 0
for key in P:
    P[key] = sample[i]
    i += 1

with open("../results/PSO/evoluzione_2/Pso_fit_2/mean_parameters.txt", 'w') as outfile:
    json.dump(P, outfile)
'''

