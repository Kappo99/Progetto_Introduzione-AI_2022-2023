import heapq

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

def heuristic(start, goal):
    return sum(max(abs(start[i][0]-goal[i][0]), abs(start[i][1]-goal[i][1])) for i in range(len(start)))

def manhattan_distance(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

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
path = a_star(start[test_number], goal[test_number], k, N[test_number])
print("Path: ", path)
