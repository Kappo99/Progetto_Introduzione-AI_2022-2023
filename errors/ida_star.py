import sys
from typing import List, Tuple

# Definizione della scacchiera
N = 5
board = [[0] * N for _ in range(N)]

# Definizione dei possibili movimenti dei cavalieri
moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

# Funzione per controllare se una posizione sulla scacchiera è valida
def is_valid(x: int, y: int, visited: List[Tuple[int, int]]) -> bool:
    return 0 <= x < N and 0 <= y < N and (x, y) not in visited

# Funzione per trovare la soluzione usando l'algoritmo IDA*
def ida_star(start: List[Tuple[int, int]], goal: List[Tuple[int, int]], depth: int, g: int) -> Tuple[bool, int]:
    # Controlla se lo stato attuale corrisponde allo stato finale
    if start == goal:
        return True, g

    # Calcola l'euristica (distanza di Manhattan) per ogni cavallo
    h = sum(abs(s[0] - g[0]) + abs(s[1] - g[1]) for s, g in zip(start, goal))

    # Controlla se la profondità massima è stata raggiunta
    if depth == 0:
        return False, sys.maxsize

    # Scansiona tutti i possibili movimenti
    min_f = sys.maxsize
    for i in range(0, len(start), m):
        next_start = start[:]
        for j in range(i, min(i + m, len(start))):
            x, y = start[j]
            for dx, dy in moves:
                new_x, new_y = x + dx, y + dy
                if is_valid(new_x, new_y, next_start):
                    # next_start[j] = (new_x, new_y)
                    new_next_start = []
                    for i in range(len(next_start)):
                        if i == j:
                            new_next_start.append((new_x, new_y))
                        else:
                            new_next_start.append(next_start[i])
                    break
        found, f = ida_star(new_next_start, goal, depth - 1, g + 1)
        if found:
            return True, f
        min_f = min(min_f, f + h)

    return False, min_f


# Funzione per risolvere il problema degli spostamenti dei cavalieri
def solve(k: int, start: List[Tuple[int, int]], goal: List[Tuple[int, int]]) -> int:
    global m
    m = k  # numero di cavalli che si possono muovere contemporaneamente
    depth = 1
    while True:
        found, f = ida_star(start, goal, depth, 0)
        if found:
            return f
        depth += 1


# Esempio di utilizzo
# start = [(0, 0), (1, 0), (2, 0)]
# goal = [(7, 7), (6, 7), (5, 7)]
# print(solve(len(start), start, goal))  # Output: 6

start = ((0, 0), (1, 1))
goal = ((4, 2), (3, 2))
print(solve(len(start), start, goal))

