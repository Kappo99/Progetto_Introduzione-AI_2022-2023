import random

# Funzione di valutazione che calcola il numero di collisioni tra i cavalieri
def evaluate(board):
    collisions = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if abs(board[i] - board[j]) == j - i:
                collisions += 1
    return collisions

# Genera una soluzione casuale
def generate_solution(n):
    return [random.randint(0, n - 1) for _ in range(n)]

# Cerca la soluzione ottimale utilizzando l'algoritmo hill-climbing
def hill_climbing(n, max_iterations):
    # Genera una soluzione casuale come punto di partenza
    current = generate_solution(n)
    current_cost = evaluate(current)

    # Itera fino a quando non viene trovata una soluzione soddisfacente o viene raggiunto il limite di iterazioni
    for i in range(max_iterations):
        # Genera una lista di possibili mosse
        neighbors = [generate_solution(n) for _ in range(n)]

        # Valuta il costo di ogni vicino e scegli il migliore
        neighbor_costs = [evaluate(neighbor) for neighbor in neighbors]
        best_neighbor = min(neighbors, key=evaluate)
        best_neighbor_cost = evaluate(best_neighbor)

        # Se il vicino migliore ha un costo inferiore, aggiorna la soluzione corrente
        if best_neighbor_cost < current_cost:
            current = best_neighbor
            current_cost = best_neighbor_cost

    # Restituisci la soluzione ottimale trovata
    return current

# Esempio di utilizzo dell'algoritmo
n = 8 # Dimensione della scacchiera
max_iterations = 1000 # Limite di iterazioni
solution = hill_climbing(n, max_iterations)
print(solution) # Stampa la soluzione ottimale trovata
