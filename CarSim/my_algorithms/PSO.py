import pygmo as pg
import numpy as np
import json
from my_algorithms.torcs_problem import TorcsProblem
from Server import start_multiple_server
import matplotlib.pyplot as plt
import time
import pickle

def custom_pso(problem, n_gens, variant, pop_size, seed, start_param_file, output_param_file):
    prob = pg.problem(problem)
    uda = pg.pso(gen = n_gens, omega=0.7298, eta1=1.49618, eta2=1.49618, variant=5, neighb_type=variant, memory=True, seed=seed)
    algo = pg.algorithm(uda)

    global_results = []
    logs = []
    results_trial = []
    algo.set_verbosity(1)

    with open("../parameters_2/individui_fit2","rb") as f:
        samples = pickle.load(f)
    pop = pg.population(prob, 15)
    for i in samples:
        pop.push_back(i)
    pop = algo.evolve(pop)

    logs.append(algo.extract(type(uda)).get_log())
    logs = np.array(logs)
    results_trial.append(np.min(logs[:, logs.shape[1] - 1, 2]))
    avg_log = np.average(logs, 0)
    global_results.append(np.min(results_trial, 0))

    pfile = open(start_param_file, 'r')
    P = json.load(pfile)

    i = 0
    for key in P:
        P[key] = pop.champion_x[i]
        i = i + 1
    with open(output_param_file, 'w') as outfile:
        json.dump(P, outfile)

    return avg_log

if __name__ == "__main__":
    neigh_type = [2]
    neigh_name = ['lbest']
    p_size = 20
    n_gens = 30
    D = 49
    initial_file = "../default_parameters"
    seeds = np.loadtxt('../seeds.txt', delimiter=',')
    pg.set_global_rng_seed(seed=32)

    history_file = "../results/PSO/history.txt"
    history_time = "../results/PSO/history_time.txt"
    problem = TorcsProblem(D, n_gens, initial_file, history_file, history_time, p_size)
    start_multiple_server(visual=False)

    i = 1
    for seed in seeds[:5]:
        print("################# Inizio seed n." + str(i) + " #################")
        plt.figure(i)
        plt.title("PSO: results trial n." + str(i))
        prev_seed = time.time()
        for (type, name) in zip(neigh_type, neigh_name):
            prev_variant = time.time()
            print("################# Inizio variante " + name + " #################")
            final_file = "../results/PSO/best_pso_parameters_" + str(i) + "_variant_" + str(name) + ".txt"
            # salvataggio del log corrispondente alla variante corrente con un dato seme (TOT: 10 file)
            with open("../results/PSO/console_log_seed_" + str(i) + "_variant_" + str(name) + ".txt", "w") as outfile:
                avg_log = custom_pso(problem, n_gens, type, p_size, int(seed), initial_file, final_file)
                outfile.write(str(avg_log))
                plt.plot(avg_log[:, 0], avg_log[:, 2], label='variante: ' + str(name))
                plt.legend(loc='upper right')
                plt.grid()
            print("################# Fine ", str(name), ". Tempo trascorso: ", str((time.time() - prev_variant) / 60), " minuti #################")
        plt.savefig('../results/PSO/figures/seed_'+str(i)+".png")
        print("################# Fine trial n.", str(i), ". Tempo trascorso: ", str((time.time() - prev_seed) / 60), " minuti #################")

        i += 1

    plt.show()
