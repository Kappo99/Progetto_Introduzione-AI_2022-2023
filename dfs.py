from queue import Queue

def generate_moves(position, max_moves, N):
    row, col = position
    moves = []
    for i, j in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]:
        new_row, new_col = row + i, col + j
        # print(max(abs(i), abs(j)), max_moves)
        if 0 <= new_row < N and 0 <= new_col < N and max(abs(i), abs(j)) <= max_moves:
            moves.append((new_row, new_col))
    return moves


def dfs(state, goal, max_moves, k, N, path=[]):
    # print("Max moves: ", max_moves)
    if state == goal:
        return path
    if max_moves == 0:
        return None
    for i in range(k):
        for j in range(2, max_moves+1):
            moves = generate_moves(state[i], j, N)
            # print("MOVES: ", moves)
            for move in moves:
                if move not in state:
                    new_state = tuple(state[:i] + (move,) + state[i+1:])
                    new_path = path + [(i, move)]
                    result = dfs(new_state, goal, max_moves-1, k, N, new_path)
                    if result is not None:
                        return result
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
path = dfs(start[test_number], goal[test_number], 8, k, N[test_number])
print("Path: ", path)
