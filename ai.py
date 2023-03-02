import algorithm
import pprint
import json
import time

def path_to_list(path):
    list = [] # lista di tuple (chiave, valore)
    for key, value in path: # per ogni tupla (chiave, valore) nella lista path
        found = False # flag che indica se la chiave è già presente nella lista
        for group in list: # per ogni tupla (chiave, lista) nella lista list
            if group[0] == key: # se la chiave è già presente
                group[1].append(value) # aggiunge il valore alla lista
                found = True # imposta il flag a True
                break # esce dal ciclo
        if not found: # se la chiave non è già presente
            list.append((key, [value])) # aggiunge la tupla (chiave, lista) alla lista
    return sorted(list, key=lambda x: x[0]) # ordina la lista per chiave e la restituisce

def test_from_file(test_number):
    with open("config/"+str(test_number)+".json", "r") as f: # apre il file di test
        data = json.load(f) # carica i dati dal file

    start = tuple(map(tuple, data["start"])) # converte la lista di liste in una tupla di tuple
    goal = tuple(map(tuple, data["goal"])) # converte la lista di liste in una tupla di tuple
    k = int(data["k"]) # converte la stringa in un intero
    N = int(data["N"]) # converte la stringa in un intero

    print("Start: ", start) # stampa lo stato iniziale
    print("Goal: ", goal) # stampa lo stato finale
    print("K: ", k) # stampa il numero di cavalli da muovere
    print("N: ", N) # stampa la dimensione della scacchiera

    bfs_start_time = time.time() # memorizza il tempo di inizio
    bfs_path = algorithm.bfs(start, goal, k, N) # esegue l'algoritmo
    bfs_end_time = time.time() # memorizza il tempo di fine
    bfs_duration = bfs_end_time - bfs_start_time # calcola la durata in secondi

    # dfs_start_time = time.time() # memorizza il tempo di inizio
    # dfs_path = algorithm.dfs(start, goal, k, N, set()) # esegue l'algoritmo
    # dfs_end_time = time.time() # memorizza il tempo di fine
    # dfs_duration = dfs_end_time - dfs_start_time # calcola la durata in secondi

    a_star_manhattan_start_time = time.time() # memorizza il tempo di inizio
    a_star_manhattan_path = algorithm.a_star(start, goal, k, N, algorithm.manhattan_distance) # esegue l'algoritmo
    a_star_manhattan_end_time = time.time() # memorizza il tempo di fine
    a_star_manhattan_duration = a_star_manhattan_end_time - a_star_manhattan_start_time # calcola la durata in secondi

    a_star_chebyshev_start_time = time.time() # memorizza il tempo di inizio
    a_star_chebyshev_path = algorithm.a_star(start, goal, k, N, algorithm.chebyshev_distance) # esegue l'algoritmo
    a_star_chebyshev_end_time = time.time() # memorizza il tempo di fine
    a_star_chebyshev_duration = a_star_chebyshev_end_time - a_star_chebyshev_start_time # calcola la durata in secondi

    with open("output/"+str(test_number)+".txt", "w") as f: # apre il file di output
        f.write("BFS\n" + "Durata: " + str(bfs_duration) + " secondi\n") # scrive la durata dell'algoritmo
        pprint.pprint(path_to_list(bfs_path), width=15, stream=f) # scrive il percorso
        f.write("\n\n") # aggiunge una riga vuota

        # f.write("DFS\n" + "Durata: " + str(dfs_duration) + " secondi\n") # scrive la durata dell'algoritmo
        # pprint.pprint(path_to_list(dfs_path), width=15, stream=f) # scrive il percorso
        # f.write("\n\n") # aggiunge una riga vuota

        f.write("A* Manhattan\n" + "Durata: " + str(a_star_manhattan_duration) + " secondi\n") # scrive la durata dell'algoritmo
        pprint.pprint(path_to_list(a_star_manhattan_path), width=15, stream=f) # scrive il percorso
        f.write("\n\n") # aggiunge una riga vuota

        f.write("A* Chebyshev\n" + "Durata: " + str(a_star_chebyshev_duration) + " secondi\n") # scrive la durata dell'algoritmo
        pprint.pprint(path_to_list(a_star_chebyshev_path), width=15, stream=f) # scrive il percorso
        f.write("\n\n") # aggiunge una riga vuota

test_number = int(input("Test number: ")) # legge il numero del test
test_from_file(test_number) # esegue il test
