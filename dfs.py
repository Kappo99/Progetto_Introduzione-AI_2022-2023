from queue import Queue

def generate_moves(pos, N):
    row, col = pos # estrae la riga e la colonna della posizione
    moves = set() # insieme dei possibili movimenti
    for dr, dc in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]: # per ogni possibile mossa
        r, c = row + dr, col + dc # calcola la nuova posizione
        if 0 <= r < N and 0 <= c < N: # se la nuova posizione è valida
            moves.add((r, c)) # aggiunge la nuova posizione all'insieme dei movimenti
    return moves # restituisce l'insieme dei movimenti

def dfs(num_knights, positions, targets, N, visited):
    if all(pos == target for pos, target in zip(positions, targets)):
        # se tutte le posizioni obiettivo sono state raggiunte, restituisci le mosse effettuate
        return [positions]
    else:
        # altrimenti, esplora tutte le possibili mosse dei cavalieri
        min_moves = None
        for i in range(num_knights):
            for move in generate_moves(positions[i], N):
                if move not in visited:
                    visited.add(move)
                    new_positions = positions[:i] + (move,) + positions[i+1:]
                    # calcola ricorsivamente le mosse effettuate per raggiungere la soluzione ottimale
                    moves = dfs(num_knights, new_positions, targets, N, visited)
                    visited.remove(move)
                    if moves is not None:
                        # se la soluzione è valida, aggiungi la mossa corrente alla lista delle mosse effettuate
                        moves.append(new_positions)
                        if min_moves is None or len(moves) < len(min_moves):
                            # se questa è la soluzione più breve trovata finora, aggiorna la lista delle mosse effettuate
                            min_moves = moves
        return min_moves

positions = ((0, 0), (1, 0)) # posizioni iniziali dei cavalieri
targets = ((2, 2), (2, 1)) # posizioni obiettivo dei cavalieri
N = 3 # dimensione della scacchiera
# positions = ((0, 0), (1, 0), (2, 0)) # posizioni iniziali dei cavalieri
# targets = ((2, 2), (3, 2), (4, 2)) # posizioni obiettivo dei cavalieri
# N = 5 # dimensione della scacchiera
visited = set() # insieme delle posizioni visitate
moves = dfs(2, positions, targets, N, visited) # calcola le mosse effettuate per raggiungere la soluzione ottimale
print(moves) # stampa le mosse

