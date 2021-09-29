import pygmo as pg
import numpy as np
import json
from my_algorithms.torcs_problem import TorcsProblem
from Server import start_multiple_server
from Server import start_server_single
import matplotlib.pyplot as plt
import time
import pickle

def custom_sade(problem, n_gens, variant, pop_size, seed, start_param_file, output_param_file):
    prob = pg.problem(problem)
    uda = pg.sade(gen=n_gens, variant=variant, variant_adptv=1, memory=False, seed=seed, ftol=1e-20, xtol=1e-20)
    algo = pg.algorithm(uda)

    global_results = []
    logs = []
    results_trial = []
    algo.set_verbosity(1)
    #pop = pg.population(prob, pop_size)

    with open("../parameters_2/new_population","rb") as f:
        samples = pickle.load(f)
    pop = pg.population(prob, 10)
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
    variants = [8] #[7, 9, 8]
    variants_name = ["rand-to-best/1/bin"] #["rand/1/bin", "best/2/bin", "rand-to-best/1/bin"]
    p_size = 20
    n_gens = 30
    D = 49
    initial_file = "../results/SADE/evoluzione_1/sade_fit1/seed_1/best_sade_parameters_1_variant_7.txt"
    seeds = np.loadtxt('../seeds.txt', delimiter=',')
    pg.set_global_rng_seed(seed=32)

    history_file = "../results/SADE/history.txt"
    history_time = "../results/SADE/history_time.txt"
    problem = TorcsProblem(D, n_gens, initial_file, history_file, history_time, p_size)
    #start_multiple_server(visual=False)
    start_server_single()

    i = 1
    for seed in seeds[:5]:
        print("################# Inizio seed n." + str(i) + " #################")
        plt.figure(i)
        plt.title("SADE: results trial n." + str(i))
        prev_seed = time.time()

        for (variant, variant_name) in zip(variants, variants_name):
            prev_variant = time.time()
            print("################# Inizio variante " + variant_name + " #################")
            final_file = "../results/SADE/best_sade_parameters_" + str(i) + "_variant_" + str(variant) + ".txt"
            # salvataggio del log corrispondente alla variante corrente con un dato seme (TOT: 15 file)
            with open("../results/SADE/console_log_seed_" + str(i) + "_variant_" + str(variant) + ".txt", "w") as outfile:
                avg_log = custom_sade(problem, n_gens, variant, p_size, int(seed), initial_file, final_file)
                outfile.write(str(avg_log))
                plt.plot(avg_log[:, 0], avg_log[:, 2], label='variante: ' + str(variant_name))
                plt.legend(loc='upper right')
                plt.grid()
            print("################# Fine ", str(variant_name), ". Tempo trascorso: ", str((time.time() - prev_variant) / 60), " minuti #################")
        plt.savefig('../results/SADE/figures/seed_'+str(i)+".png")
        print("################# Fine trial n.", str(i), ". Tempo trascorso: ", str((time.time() - prev_seed) / 60), " minuti #################")

        i += 1

    plt.show()
