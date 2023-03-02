def DFS(G):
    for all v 2 V
        v:col = W
        v: = NIL
    time = 0
    for all v 2 V
        if v:col == W
            DFS_VISIT (v)

def DFS_VISIT (u):
    time += 1
    u:d = time
    u:col = G
    for all v 2 Adj[u]
        if v:col == W
            v: = u
            DFS_VISIT (v)
    v:col = B
    time ++
    v:f = time