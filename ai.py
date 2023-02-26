from queue import Queue
import heapq
import json
import time

def generate_moves(pos, N):
    row, col = pos
    moves = set()
    for dr in [-2, -1, 1, 2]:
        for dc in [-2, -1, 1, 2]:
            if abs(dr) + abs(dc) != 3:
                continue
            r, c = row + dr, col + dc
            if 0 <= r < N and 0 <= c < N:
                moves.add((r, c))
    return moves

def bfs(start, goal, k, N):
    queue = Queue()
    queue.put((start, [])) # inserisce lo stato iniziale e un percorso vuoto nella coda
    visited = set() # insieme degli stati già visitati
    while not queue.empty(): # finché la coda non è vuota
        state, path = queue.get() # preleva lo stato e il percorso dalla testa della coda
        if state == goal: # se lo stato è l'obiettivo, restituisce il percorso
            return path
        if state in visited: # se lo stato è già stato visitato, passa allo stato successivo
            continue
        visited.add(state) # marca lo stato come visitato
        for i in range(k): # per ogni cavallo
            moves = generate_moves(state[i], N) # genera tutti i movimenti validi
            for move in moves: # per ogni movimento valido
                if move not in state and move not in visited: # se la nuova posizione non è occupata e non è già stata visitata
                    new_state = tuple(state[:i] + (move,) + state[i+1:]) # crea il nuovo stato con il cavallo che si è mosso
                    new_path = path + [(i, move)] # aggiunge la mossa al percorso
                    queue.put((new_state, new_path)) # inserisce il nuovo stato e il percorso nella coda
    return None # se la coda è vuota e non è stato trovato un percorso, restituisce None

def heuristic(start, goal):
    return sum(max(abs(start[i][0]-goal[i][0]), abs(start[i][1]-goal[i][1])) for i in range(len(start)))

def a_star(start, goal, k, N):
    open_set = [(heuristic(start, goal), start, [])]
    closed_set = set()
    while open_set:
        f, state, path = heapq.heappop(open_set)
        if state in closed_set:
            continue
        if state == goal:
            return path
        closed_set.add(state)
        for i in range(k):
            moves = generate_moves(state[i], N)
            for move in moves:
                if move in state:
                    continue
                new_state = tuple(state[:i] + (move,) + state[i+1:])
                new_path = path + [(i, move)]
                new_f = len(new_path) + heuristic(new_state, goal)
                heapq.heappush(open_set, (new_f, new_state, new_path))
    return None

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
    bfs_path = bfs(start, goal, k, N) # esegue l'algoritmo
    bfs_end_time = time.time() # memorizza il tempo di fine
    bfs_duration = bfs_end_time - bfs_start_time # calcola la durata in secondi

    # dfs_start_time = time.time() # memorizza il tempo di inizio
    # dfs_path = dfs(start, goal, k, N) # esegue l'algoritmo
    # dfs_end_time = time.time() # memorizza il tempo di fine
    # dfs_duration = dfs_end_time - dfs_start_time # calcola la durata in secondi

    a_star_start_time = time.time() # memorizza il tempo di inizio
    a_star_path = a_star(start, goal, k, N) # esegue l'algoritmo
    a_star_end_time = time.time() # memorizza il tempo di fine
    a_star_duration = a_star_end_time - a_star_start_time # calcola la durata in secondi
    
    with open("output/"+str(test_number)+".txt", 'w') as f:
        f.write("BFS\n" + "Durata: " + str(bfs_duration) + " secondi\n" + str(bfs_path) + "\n\n")
        # f.write("DFS\n" + "Durata: " + str(dfs_duration) + " secondi\n" + str(dfs_path) + "\n\n")
        f.write("A*\n" + "Durata: " + str(a_star_duration) + " secondi\n" + str(a_star_path) + "\n\n")

test_number = int(input("Test number: "))
test_from_file(test_number)
