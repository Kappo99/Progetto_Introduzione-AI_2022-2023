def generate_moves(pos, N):
    row, col = pos # estrae la riga e la colonna della posizione
    moves = set() # insieme dei possibili movimenti
    for dr, dc in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]: # per ogni possibile mossa
        r, c = row + dr, col + dc # calcola la nuova posizione
        if 0 <= r < N and 0 <= c < N: # se la nuova posizione è valida
            moves.add((r, c)) # aggiunge la nuova posizione all'insieme dei movimenti
    return moves # restituisce l'insieme dei movimenti


def dfs(k, positions, targets, N, visited):
    if k == len(positions):
        return []
    moves = []
    for i, pos in enumerate(positions):
        if i not in visited:
            visited.add(i)
            for move in generate_moves(pos, N):
                if move == targets[k]:
                    new_positions = positions[:i] + (move,) + positions[i+1:]
                    res = dfs(k+1, new_positions, targets, N, visited)
                    if res is not None:
                        moves.append((i, move))
                        moves.extend(res)
            visited.remove(i)
    return moves


positions = ((0, 0), (1, 1))
targets = ((4, 2), (3, 2))
N = 5
visited = set()
moves = dfs(0, positions, targets, N, visited)
print(moves)

# positions = ((0, 0), (1, 0)) # posizioni iniziali dei cavalieri
# targets = ((2, 2), (2, 1)) # posizioni obiettivo dei cavalieri
# N = 3 # dimensione della scacchiera
# # positions = ((0, 0), (1, 0), (2, 0)) # posizioni iniziali dei cavalieri
# # targets = ((2, 2), (3, 2), (4, 2)) # posizioni obiettivo dei cavalieri
# # N = 5 # dimensione della scacchiera
# visited = set() # insieme delle posizioni visitate
# moves = dfs(2, positions, targets, N, visited) # calcola le mosse effettuate per raggiungere la soluzione ottimale
# print(moves) # stampa le mosse

# start = ((0, 0), (1, 0), (2, 0)) # posizioni iniziali dei cavalieri
# goal = ((2, 2), (3, 2), (4, 2)) # posizioni obiettivo dei cavalieri
# N = 5 # dimensione della scacchiera
# path = algorithm.dfs(start, goal, 3, N, set()) # calcola il costo minimo della soluzione
# print(path) # stampa il costo minimo della soluzione

