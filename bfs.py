from queue import Queue

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
    count = 0
    queue = Queue()
    queue.put((start, [])) # inserisce lo stato iniziale e un percorso vuoto nella coda
    visited = set() # insieme degli stati già visitati
    while not queue.empty(): # finché la coda non è vuota
        state, path = queue.get() # preleva lo stato e il percorso dalla testa della coda
        count += 1
        if count % 100000 == 0:
            print(count)
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

test_number = int(input("Test number: ")) - 1
start = [((0, 0), (1, 1)),
         ((0, 0), (1, 1)),
         ((0, 0), (0, 1), (1, 1)),
         ((0, 0), (0, 1), (1, 1), (1, 2)),
         ((0, 0), (0, 1), (1, 1), (1, 2)),
         ((0, 1), (2, 1), (3, 6), (4, 1), (5, 2), (6, 1), (7, 3)),
         ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9))]
goal  = [((4, 2), (3, 2)),
         ((1, 1), (0, 0)),
         ((4, 4), (4, 3), (3, 4)),
         ((4, 4), (4, 3), (3, 4), (3, 3)),
         ((4, 4), (4, 3), (3, 4), (3, 3)),
         ((2, 3), (4, 1), (1, 5), (6, 7), (1, 2), (5, 4), (0, 0)),
         ((9, 9), (8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0))]
k = len(start[test_number])
N = [5, 4, 5, 5, 7, 8, 10]
print("Start: ", start[test_number])
print("Goal: ", goal[test_number])
print("K: ", k)
print("N: ", N[test_number])
path = bfs(start[test_number], goal[test_number], k, N[test_number])
print("Path: ", path)

