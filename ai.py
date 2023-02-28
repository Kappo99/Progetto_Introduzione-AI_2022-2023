import algorithm
import pprint
import json
import time

def path_to_list(path):
    list = []
    for key, value in path:
        found = False
        for group in list:
            if group[0] == key:
                group[1].append(value)
                found = True
                break
        if not found:
            list.append((key, [value]))
    return sorted(list, key=lambda x: x[0])

def test_from_file(test_number):
    with open("config/"+str(test_number)+".json", "r") as f:
        data = json.load(f)

    start = tuple(map(tuple, data["start"]))
    goal = tuple(map(tuple, data["goal"]))
    k = int(data["k"])
    N = int(data["N"])

    print("Start: ", start)
    print("Goal: ", goal)
    print("K: ", k)
    print("N: ", N)

    bfs_start_time = time.time() # memorizza il tempo di inizio
    bfs_path = algorithm.bfs(start, goal, k, N) # esegue l'algoritmo
    bfs_end_time = time.time() # memorizza il tempo di fine
    bfs_duration = bfs_end_time - bfs_start_time # calcola la durata in secondi

    # dfs_start_time = time.time() # memorizza il tempo di inizio
    # dfs_path = algorithm.dfs(start, goal, k, N, set()) # esegue l'algoritmo
    # dfs_end_time = time.time() # memorizza il tempo di fine
    # dfs_duration = dfs_end_time - dfs_start_time # calcola la durata in secondi

    a_star_start_time = time.time() # memorizza il tempo di inizio
    a_star_path = algorithm.a_star(start, goal, k, N) # esegue l'algoritmo
    a_star_end_time = time.time() # memorizza il tempo di fine
    a_star_duration = a_star_end_time - a_star_start_time # calcola la durata in secondi
    
    with open("output/"+str(test_number)+".txt", 'w') as f:
        f.write("BFS\n" + "Durata: " + str(bfs_duration) + " secondi\n")
        pprint.pprint(path_to_list(bfs_path), width=15, stream=f)
        f.write("\n\n")
        # f.write("DFS\n" + "Durata: " + str(dfs_duration) + " secondi\n")
        # pprint.pprint(path_to_list(dfs_path), width=15, stream=f)
        # f.write("\n\n")
        f.write("A*\n" + "Durata: " + str(a_star_duration) + " secondi\n")
        pprint.pprint(path_to_list(a_star_path), width=15, stream=f)
        f.write("\n\n")

test_number = int(input("Test number: "))
test_from_file(test_number)
