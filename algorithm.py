from queue import Queue
import heapq


def generate_moves(pos, N):
    row, col = pos # estrae la riga e la colonna della posizione
    moves = set() # insieme dei possibili movimenti
    for dr, dc in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]: # per ogni possibile mossa
        r, c = row + dr, col + dc # calcola la nuova posizione
        if 0 <= r < N and 0 <= c < N: # se la nuova posizione è valida
            moves.add((r, c)) # aggiunge la nuova posizione all'insieme dei movimenti
    return moves # restituisce l'insieme dei movimenti


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


def chebyshev_distance(start, goal):
    return sum(max(abs(start[i][0]-goal[i][0]), abs(start[i][1]-goal[i][1])) for i in range(len(start)))

def manhattan_distance(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

def a_star(start, goal, k, N):
    open_set = [(chebyshev_distance(start, goal), start, [])] # inserisce lo stato iniziale e un percorso vuoto nella coda
    closed_set = set() # insieme degli stati già visitati
    while open_set: # finché la coda non è vuota
        f, state, path = heapq.heappop(open_set) # preleva lo stato e il percorso dalla testa della coda
        if state in closed_set: # se lo stato è già stato visitato, passa allo stato successivo
            continue
        if state == goal: # se lo stato è l'obiettivo, restituisce il percorso
            return path
        closed_set.add(state) # marca lo stato come visitato
        for i in range(k): # per ogni cavallo
            moves = generate_moves(state[i], N) # genera tutti i movimenti validi
            for move in moves: # per ogni movimento
                if move in state: # se il movimento è già stato effettuato
                    continue
                new_state = tuple(state[:i] + (move,) + state[i+1:]) # genera lo stato successivo
                new_path = path + [(i, move)] # genera il percorso successivo
                new_f = len(new_path) + chebyshev_distance(new_state, goal) # calcola la funzione di valutazione
                heapq.heappush(open_set, (new_f, new_state, new_path)) # inserisce lo stato e il percorso nella coda
    return None # se la coda è vuota e non è stato trovato un percorso, restituisce None
