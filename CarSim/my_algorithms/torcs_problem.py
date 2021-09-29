import json
from fitness_functions import speed_pos_fitness
from fitness_functions import speed_fitness
from client import pool_threads
import time

class TorcsProblem:
    def __init__(self, dimension, n_gens, start_param_file, history_file, history_time, pop_size):
        self.dimension = dimension
        self.n_gens = n_gens
        self.current_gen = 0
        self.start_param_file = start_param_file
        self.history_file = history_file
        self.history_time = history_time
        self.list_times = []
        self.pop_size = pop_size
        self.time_per_gen = time.time()
        self.current_element = 0

    def fitness(self, decision_vector):
        print("Individuo #", self.current_element,"   Generazione #", self.current_gen)

        self.current_element = self.current_element + 1
        if (self.current_element - 1 == self.pop_size):
            now = time.time()
            print("################# Fine generazione n.", str(self.current_gen),
                  ". Tempo trascorso: ", str((now - self.time_per_gen) / 60)," minuti #################")
            self.current_gen = self.current_gen + 1
            self.current_element = 0
            self.time_per_gen = time.time()

        P = json.load(open(self.start_param_file, 'r')) # individuo di partenza
        i = 0
        for key in P:
            P[key] = decision_vector[i]
            i = i + 1
        # parallelismo
        track_results = pool_threads(path_params=self.start_param_file, P=P)
        current_fscore = 0
        str_info = ""
        str_lap = ""
        for result in track_results:
            Laps = result["laps"]
            score, info, info_lap = speed_pos_fitness(Laps, self.current_gen, self.n_gens)
            current_fscore += score # fitness su un tracciato
            # speed_pos_fitness(Laps, self.current_gen, self.n_gens)

            str_info += info
            str_lap += info_lap

            self.list_times.append(info_lap)

        current_fscore = current_fscore/len(track_results) #media fitness sui tracciati totali
        print(str_info)
        str_fitness = "\nMedium fscore: " + str(current_fscore) + "\n"
        print("Medium f_score: " + str(current_fscore)+"\n_______")

        #logs
        with open(self.history_file, 'a') as outfile:
            outfile.write(str_info)
            outfile.write(str_fitness)
            outfile.write('___________________________PARAMETERS___________________________\n')
            json.dump(P, outfile)
            outfile.write('_________________________________________________________________\n')

        return [current_fscore]

    '''
    def get_bounds(self):
    
        Implementazione necessaria per la definizione del problema. Defisce i range di variazione dei parametri da
        evolvere.
        :return: una tupla di liste con i range dei valori [min; max].
        
        P = json.load(open(self.start_param_file, 'r'))
        # dn_bounds = json.load(open("../my_algorithms/Parametri/down_bounds.txt", 'r'))
        # up_bounds = json.load(open("../my_algorithms/Parametri/up_bounds.txt", 'r'))

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
        # print("lower_list",lower_list)
        # print("upper_list",upper_list)
        return (lower_list, upper_list)
    '''

    def get_bounds(self):
        '''
        Implementazione necessaria per la definizione del problema. Defisce i range di variazione dei parametri da
        evolvere.
        :return: una tupla di liste con i range dei valori [min; max].
        '''
        # P = json.load(open(self.start_param_file, 'r'))
        # dn_bounds = json.load(open("../my_algorithms/Parametri/down_bounds.txt", 'r'))
        # up_bounds = json.load(open("../my_algorithms/Parametri/up_bounds.txt", 'r'))

        dn_bounds = json.load(open("../parameters_2/ev2_min_fit2.txt", 'r'))
        up_bounds = json.load(open("../parameters_2/ev2_max_fit2.txt", 'r'))

        lower_list = list()
        upper_list = list()

        percent = 0.3

        for key in dn_bounds:
            if key.find("upsh") >= 0:
                upper_list.append(9700)
                lower_list.append(6500)
            elif key.find("dnsh") >= 0:
                upper_list.append(7000)
                lower_list.append(4000)
            else:
                lower_list.append(dn_bounds[key] - dn_bounds[key] * percent)
                upper_list.append(up_bounds[key] + up_bounds[key] * percent)
        # print("lower_list",lower_list)
        # print("upper_list",upper_list)
        return (lower_list, upper_list)