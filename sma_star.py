from heapq import heappush, heappop
from typing import List, Tuple

class Node:
    def __init__(self, state: List[Tuple[int, int]], g: int, f: int):
        self.state = state
        self.g = g
        self.f = f

    def __lt__(self, other):
        return self.f < other.f

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heappush(self.elements, (priority, item))

    def get(self):
        return heappop(self.elements)[1]

def heuristic(state: List[Tuple[int, int]], goals: List[Tuple[int, int]]) -> int:
    # Calcola la distanza di Chebyshev tra la posizione attuale dei cavalieri e le posizioni obiettivo
    return max(abs(s[0]-g[0]) + abs(s[1]-g[1]) for s, g in zip(state, goals))

def get_successors(state: List[Tuple[int, int]], m: int, N: int) -> List[List[Tuple[int, int]]]:
    # Genera tutte le possibili combinazioni di m movimenti dei cavalieri
    successors = []
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            for dx, dy in [(2,1), (1,2), (-2,1), (-1,2), (2,-1), (1,-2), (-2,-1), (-1,-2)]:
                new_state = list(state)
                new_state[i] = (state[i][0] + dx, state[i][1] + dy)
                if new_state[i] in new_state[:i] + new_state[i+1:j] + new_state[j+1:]:
                    continue
                new_state[j] = (state[j][0] - dx, state[j][1] - dy)
                if new_state[j] in new_state[:i] + new_state[i+1:j] + new_state[j+1:]:
                    continue
                if all(0 <= s[0] < N and 0 <= s[1] < N for s in new_state):
                    successors.append(new_state)
    return successors

def sma_star(initial_state: List[Tuple[int, int]], goals: List[Tuple[int, int]], m: int, N: int) -> List[List[Tuple[int, int]]]:
    start_node = Node(initial_state, 0, heuristic(initial_state, goals))
    open_set = PriorityQueue()
    open_set.put(start_node, start_node.f)
    closed_set = set()

    while not open_set.empty():
        current_node = open_set.get()
        if current_node.state == goals:
            # Soluzione trovata, restituisce il percorso
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return list(reversed(path))

        closed_set.add(tuple(current_node.state))
        successors = get_successors(current_node.state, m, N)
        for successor_state in successors:
            if tuple(successor_state) in closed_set:
                continue
            g = current_node.g + 1
            f = g + heuristic(successor_state, goals)
            successor_node = Node(successor_state, g, f)
            successor_node.parent


# Esempio di utilizzo
start = [(0, 0), (1, 0), (2, 0)]
goal = [(7, 7), (6, 7), (5, 7)]
print(sma_star(start, goal, 1, 8))

# start = ((0, 0), (1, 1))
# goal = ((4, 2), (3, 2))
# print(sma_star(start, goal, 2, 5))

