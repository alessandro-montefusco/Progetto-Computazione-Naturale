import json
import numpy
import pickle


pso_f = ["../results/PSO/evoluzione_2"] #"../results/PSO/Pso_fit1"]
file_name = ["best_pso_parameters_", "_variant_"]
variants = ["lbest"]
seeds = list(range(1, 6))
super_list = []
arr = []
individui = []

for pso in pso_f:
    for var in variants:
        for seed in seeds:
            path = pso + "/" + file_name[0] + str(seed) + file_name[1] + var + ".txt"
            # print(path)
            super_list.append(path)

#print(len(super_list))
for i in super_list:
    P = json.load(open(i,'r'))
    for key in P:
        #print(P[key])
        arr.append(P[key])
    individui.append(arr)
    arr = []
print(individui)
print(len(individui[0]))

#print(super_list)

with open("../parameters_2/individui_fit2","wb") as file:
    print("0: ",len(individui[0]),"\n",len(individui))
    pickle.dump(individui,file)

#with open("../results/PSO/individui_fit2","rb") as file1:
#    print(pickle.load(file1))


# stabilire il minimo e massimo dei valori dei parametri
mins = []
maxs = []
for i in range(49):
    mins.append(10000)
    maxs.append(0)

for item in individui:
    for (elem,i) in zip(item,range(49)):
        if elem < mins[i]:
            mins[i] = elem
        if elem > maxs[i]:
            maxs[i] = elem

#print("MAX e MIN\n")
#print(len(mins),mins)
#print(len(maxs),maxs)


P = json.load(open("../parameters/our_parameters.txt","r"))
i=0
#Salva i lower_bound 
for key in P:
    P[key] = mins[i]
    i = i + 1
i=0

json.dump(P,open("../parameters_2/ev2_min_fit2.txt","w"))

#Salva gli upper_bound
for key in P:
    P[key] = maxs[i]
    i = i + 1
json.dump(P,open("../parameters_2/ev2_max_fit2.txt","w"))

'''
P = json.load(open("prova_rpm.txt", 'r'))


lower_list = list()
upper_list = list()

percent = 0.5

for key in P:
    if key.find("upsh") >= 0:
        upper_list.append(9700)
        lower_list.append(6500)
    elif key.find("dnsh") >= 0:
        upper_list.append(7000)
        lower_list.append(4000)
    else:
        lower_list.append(P[key] - P[key] * percent)
        upper_list.append(P[key] + P[key] * percent)
print("BOUND_OLD")

print(len(lower_list),lower_list)
print(len(upper_list),upper_list)

mins = numpy.array(mins)
maxs = numpy.array(maxs)
upper_list = numpy.array(upper_list)
lower_list = numpy.array(lower_list)

numpy.set_printoptions(suppress=True)
diff_min = abs(mins-lower_list)
diff_max = abs(maxs-upper_list)
print("Differenze")
print(diff_min.tolist())
print(diff_max.tolist())
'''



