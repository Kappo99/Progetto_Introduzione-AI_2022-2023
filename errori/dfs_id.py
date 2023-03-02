from collections import deque

# definiamo la classe per il nodo dello spazio di ricerca
class Nodo:
    def __init__(self, stato, genitore=None, azione=None, profondita=0):
        self.stato = stato
        self.genitore = genitore
        self.azione = azione
        self.profondita = profondita

    # metodo che restituisce il percorso dal nodo radice fino a questo nodo
    def percorso(self):
        nodo, perc = self, [self]
        while nodo.genitore:
            perc.append(nodo.genitore)
            nodo = nodo.genitore
        return list(reversed(perc))

# definiamo la funzione per l'algoritmo DFS-ID
def dfs_id(stato_iniziale, goal_test, successori, max_profondita, m):
    for profondita in range(max_profondita):
        print(f"Profondità massima: {profondita}")
        soluzione, costo_soluzione = dfs(Nodo(stato_iniziale), goal_test, successori, profondita, m)
        if soluzione is not None:
            return soluzione, costo_soluzione
    return None, None

# definiamo la funzione per l'algoritmo DFS ricorsivo
def dfs(nodo, goal_test, successori, profondita, m):
    if goal_test(nodo.stato):
        return nodo.percorso(), 0  # abbiamo trovato la soluzione

    if profondita == 0:
        return None, float('inf')  # raggiunta profondità massima, terminiamo

    costo_minimo = float('inf')
    for azione, nuovo_stato in successori(nodo.stato, m):
        figlio = Nodo(nuovo_stato, nodo, azione, nodo.profondita + 1)
        soluzione, costo_soluzione = dfs(figlio, goal_test, successori, profondita - 1, m)
        if soluzione is not None and costo_soluzione < costo_minimo:
            costo_minimo = costo_soluzione
            miglior_percorso = soluzione
    
    if costo_minimo != float('inf'):
        return miglior_percorso, costo_minimo  # abbiamo trovato la soluzione
    else:
        return None, float('inf')  # nessuna soluzione trovata

# esempio di utilizzo
if __name__ == '__main__':
    N = 8
    k = 4
    s = [(1,1), (2,2), (3,3), (4,4)]
    g = [(8,8), (7,7), (6,6), (5,5)]

    def goal_test(stato):
        return all(stato[i] == g[i] for i in range(k))

    def successori(stato, m):
        # generiamo tutte le mosse possibili per m cavalieri
        mosse = [(dx, dy) for dx in [-2, -1, 1, 2] for dy in [-2, -1, 1, 2] if abs(dx) != abs(dy)]
        for i in range(k):
            x, y = stato[i]
            for mossa in mosse:
                dx, dy = mossa
                nuovo_x, nuovo_y = x + dx, y + dy
                if 1 <= nuovo_x <= N and 
