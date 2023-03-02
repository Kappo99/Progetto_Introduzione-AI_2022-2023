class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.g = 0
        self.f = 0


def is_goal(state):
    for i, g in enumerate(goals):
        if state[i] != g:
            return False
    return True


def is_valid_move(state, i, j):
    x1, y1 = state[i]
    x2, y2 = state[j]
    for k, (x, y) in enumerate(state):
        if k not in (i, j) and (x, y) == (x2, y2):
            return False
    if abs(x1 - x2) == 2 and abs(y1 - y2) == 1:
        return x2 >= 0 and y2 >= 0 and x2 < N and y2 < N
    elif abs(x1 - x2) == 1 and abs(y1 - y2) == 2:
        return x2 >= 0 and y2 >= 0 and x2 < N and y2 < N
    else:
        return False


def expand(node, m=2):
    successors = []
    for i in range(len(node.state)):
        for j in range(i + 1, len(node.state)):
            if is_valid_move(node.state, i, j):
                new_state = node.state.copy()
                new_state[i], new_state[j] = new_state[j], new_state[i]
                successors.append(Node(new_state, node))
                if len(successors) == m:
                    return successors
    return successors


def cost(state1, state2):
    cost = 0
    for i in range(len(state1)):
        if state1[i] != state2[i]:
            cost += 1
    return cost


def manhattan_distance(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

def rbfs(node, f_limit, heuristic=manhattan_distance):
    if is_goal(node.state):
        return node.state, 0
    successors = expand(node)
    if not successors:
        return None, float('inf')
    for s in successors:
        s.g = node.g + cost(node.state, s.state)
        s.f = max(s.g + heuristic(s.state), node.f)
    while True:
        successors.sort(key=lambda x: x.f)
        best = successors[0]
        if best.f > f_limit:
            return None, best.f
        alternative = successors[1].f if len(successors) > 1 else float('inf')
        result, best.f = rbfs(best, min(f_limit, alternative))
        if result is not None:
            result.insert(0, best.state)
            return result, best.f

N = 5