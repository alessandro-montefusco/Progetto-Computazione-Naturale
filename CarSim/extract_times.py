import matplotlib.pyplot as plt

def obtain_fit_values(path_file):
    log = []
    with open(path_file, 'r') as fil:
        log = fil.read()

    log = log.split("\n")
    log_fit = []
    for i in range(0, len(log),2):
        fits = log[i][32:41].split(".")
        string = "0.00"+fits[0]+fits[1]
        log_fit.append(string)
    return log_fit

def extract_times(his_file, fit_vals):
    his = []
    with open(his_file, 'r') as history:
        his = history.read()

    times = []
    for item in fit_vals:
        index = his.find(item)
        times.append(his[index-107:index-18])
        #print(his[index-107:index-18])
    return times

def clear(hist):
    times = []
    for item in hist:
        indexes = [i for i in range(len(item)) if item.startswith('Time: ', i)]
        for i in indexes:
            times.append(float(item[i + 6:i + 11]))
    return times


log = obtain_fit_values("results/SADE/evoluzione_2/sade_fit2/console_log_seed_1_variant_8.txt")
hist = extract_times("results/SADE/evoluzione_2/sade_fit2/history.txt", log)
print(len(hist))
print(hist)
times = clear(hist)  #lista di 200 float (tempi di tutti gli individui)
#write the final file !!
chunks = [times[i:i+4] for i in range(0, len(times), 4)]
for c in chunks:
    with open("results/SADE/evoluzione_2/sade_fit2/his_time.txt", 'a') as f:
        f.write(str(c[0]) + "\t" + str(c[1]) + "\t" + str(c[2]) + "\t" + str(c[3]) + "\n")
