# Progetto di Introduzione all'Intelligenza Artificiale 2022/2023
Università degli Studi di Milano Bicocca\
Studente: Cappone Andrea\
Matricola: 869012
Linguaggio: Python 3.11.2
## Problema
Consideriamo il problema dello spostamento di k cavalieri degli scacchi da k caselle di partenza s1, …, sk a k caselle obiettivo g1, …, gk, su una scacchiera N x N, soggetta alla regola che due cavalli non possono occupare contemporaneamente la stessa casa. Ogni azione permette di muovere fino a m cavalieri contemporaneamente. L'obiettivo è completare la manovra nel minor numero di azioni.

## Domande di teoria
### Calcolare la dimensione dello spazio degli stati in funzione di N e m
Il problema del trasferimento di k cavalieri da k posizioni di partenza a k posizioni obiettivo su una scacchiera N x N può essere formulato come un problema di ricerca nello spazio degli stati. La dimensione dello spazio degli stati dipende dal numero di possibili posizioni di partenza dei cavalieri e dal numero di possibili azioni per ogni stato. In particolare, ci sono (N^2 choose k) possibili posizioni di partenza per k cavalieri su una scacchiera NxN e ogni stato può generare fino a m^k nuovi stati.\
Quindi, la dimensione totale dello spazio degli stati è pari a: (N^2 choose k) * (m^k)\
dove choose denota il coefficiente binomiale.

### Qual è il massimo fattore di ramificazione in questo spazio degli stati, espresso in funzione di k?
In ogni stato, ogni cavaliere ha al massimo 8 possibili mosse. Quindi il massimo fattore di ramificazione in questo spazio degli stati è pari a 8^k.

### Definire delle euristiche ammissibili
La funzione euristica è una funzione che stima il costo rimanente per arrivare alla soluzione ottimale partendo dallo stato corrente. In altre parole, l'euristica cerca di fornire una stima della distanza tra lo stato corrente e lo stato obiettivo. Questa stima viene utilizzata dall'algoritmo A\* per selezionare la prossima mossa da effettuare.

In generale, l'euristica deve essere ammissibile, ovvero non deve mai sovrastimare il costo reale per raggiungere la soluzione. Ad esempio, se consideriamo il problema del labirinto, l'euristica potrebbe essere la distanza euclidea tra la posizione corrente e la posizione obiettivo, ma questa euristica potrebbe sovrastimare il costo reale se ci sono pareti o ostacoli nel mezzo.

Le seguenti euristiche ammissibili possono essere utilizzate per risolvere il problema:
- **Distanza di Manhattan**: questa euristica stima la distanza tra la posizione attuale di ogni cavallo e la sua posizione obiettivo come la somma delle distanze orizzontali e verticali tra le due posizioni.
- **Distanza di Chebyshev**: questa euristica stima la distanza tra la posizione attuale di ogni cavallo e la sua posizione obiettivo come la massima delle distanze orizzontali e verticali tra le due posizioni.
- **Euristica di clustering**: questa euristica raggruppa i cavalieri in cluster in modo che ogni cluster abbia almeno un cavallo che è già nella posizione obiettivo. Quindi, l'euristica stima il numero di cluster che devono ancora essere spostati.

### Implementare un programma che risolva questo problema usando almeno tre diversi algoritmi di ricerca
Per risolvere il problema, possono essere utilizzati diversi algoritmi di ricerca, tra cui:
- ricerca in ampiezza (BFS)
- ricerca in profondità (DFS)
- algoritmo A\* con le euristiche sopra menzionate

## Ricerca in ampiezza (BFS)
**BFS (Breadth-First Search)** è un algoritmo di ricerca che esplora tutti i nodi adiacenti di un nodo prima di muoversi in profondità. In altre parole, esplora i nodi livello per livello e garantisce che la soluzione ottimale sia trovata solo quando la soluzione corrente ha il minor numero di mosse possibili. Tuttavia, BFS può richiedere molta memoria per tenere traccia dei nodi visitati in quanto deve mantenere una coda dei nodi visitati.

### Codice
```
def bfs(start, goal, k, N):
    queue = Queue()
    queue.put((start, [])) # inserisce lo stato iniziale e un percorso vuoto nella coda
    visited = set() # insieme degli stati già visitati
    while not queue.empty(): # finché la coda non è vuota
        state, path = queue.get() # preleva lo stato e il percorso dalla testa della coda
        if state == goal: # se lo stato è l'obiettivo, restituisce il percorso
            return path
        if state in visited: # se lo stato è già stato visitato, passa allo stato successivo
            continue
        visited.add(state) # marca lo stato come visitato
        for i in range(k): # per ogni cavallo
            moves = generate_moves(state[i], N) # genera tutti i movimenti validi
            for move in moves: # per ogni movimento valido
                if move not in state and move not in visited: # se la nuova posizione non è occupata e non è già stata visitata
                    new_state = tuple(state[:i] + (move,) + state[i+1:]) # crea il nuovo stato con il cavallo che si è mosso
                    new_path = path + [(i, move)] # aggiunge la mossa al percorso
                    queue.put((new_state, new_path)) # inserisce il nuovo stato e il percorso nella coda
    return None # se la coda è vuota e non è stato trovato un percorso, restituisce None
```

### Note
La funzione BFS implementa la ricerca in ampiezza per risolvere il problema dello spostamento dei k cavalieri sulla scacchiera. La funzione prende in input i seguenti parametri:
- `start`: una tupla contenente le posizioni di partenza dei cavalieri nella forma ((r1, c1), (r2, c2), ..., (rk, ck)).
- `goal`: una tupla contenente le posizioni di arrivo dei cavalieri nella forma ((r1, c1), (r2, c2), ..., (rk, ck)).
- `k`: il numero di cavalieri da spostare.
- `N`: la dimensione della scacchiera.
La funzione restituisce il percorso ottimo per spostare i cavalieri dalla posizione di partenza alla posizione di arrivo, rappresentato come una lista di mosse. Ogni mossa è una tupla nella forma (i, [(r1, c1), (r2, c2), ..., (rz, cz)]) dove i indica l'indice del cavallo che viene spostato e (r, c) indica la nuova posizione del cavallo.

L'algoritmo utilizza una coda per memorizzare i successivi stati da esplorare. Inizialmente, il punto di partenza viene inserito nella coda insieme al percorso vuoto. Ad ogni iterazione, l'algoritmo estrae lo stato dalla testa della coda e lo espande generando tutti i possibili nuovi stati che possono essere raggiunti. Per ogni nuovo stato generato, l'algoritmo controlla se è lo stato obiettivo e, in caso contrario, lo inserisce nella coda insieme al percorso fino a quel punto. In questo modo, l'algoritmo esplora tutti gli stati possibili nello spazio degli stati in modo sistematico, partendo dallo stato iniziale e muovendosi verso gli stati successivi in ordine di distanza dalla radice.

## Ricerca in profondità (DFS)
**DFS (Depth-First Search)** è un algoritmo di ricerca che esplora un ramo del grafo il più possibile prima di tornare indietro e esplorare il prossimo ramo. In altre parole, esplora il grafo in profondità prima di tornare indietro. A differenza di BFS, DFS non garantisce di trovare la soluzione ottimale, ma può essere più efficiente in termini di memoria.

### Codice
```
def dfs(start, goal, k, N):
```

### Note
Ho avuto diversi problemi di implementazione. Sul file dfs.py si trova una versione non completamente funzionante. Nello specifico ritorna solo percorsi parziali, e spesso il valore di ritorno è "None", come se non esistesse una soluzione al problema.

## Algoritmo A\*
**A\*** è un algoritmo di ricerca informata che combina l'approccio di BFS con una funzione euristica per migliorare l'efficienza di BFS. La funzione euristica calcola un'euristica del costo dallo stato corrente al goal e usa questa informazione per guidare l'algoritmo nella direzione giusta. A\* garantisce di trovare la soluzione ottimale se la funzione euristica è ammissibile e consistentemente stimabile. A differenza di BFS e DFS, A\* può essere più efficiente in termini di tempo e spazio.

### Codice
```
def manhattan_distance(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

def chebyshev_distance(start, goal):
    return sum(max(abs(start[i][0]-goal[i][0]), abs(start[i][1]-goal[i][1])) for i in range(len(start)))

def a_star(start, goal, k, N, heuristic=manhattan_distance):
    open_set = [(heuristic(start, goal), start, [])] # inserisce lo stato iniziale e un percorso vuoto nella coda
    closed_set = set() # insieme degli stati già visitati
    while open_set: # finché la coda non è vuota
        f, state, path = heapq.heappop(open_set) # preleva lo stato e il percorso dalla testa della coda
        if state in closed_set: # se lo stato è già stato visitato, passa allo stato successivo
            continue
        if state == goal: # se lo stato è l'obiettivo, restituisce il percorso
            return path
        closed_set.add(state) # marca lo stato come visitato
        for i in range(k): # per ogni cavallo
            moves = generate_moves(state[i], N) # genera tutti i movimenti validi
            for move in moves: # per ogni movimento
                if move in state: # se il movimento è già stato effettuato
                    continue
                new_state = tuple(state[:i] + (move,) + state[i+1:]) # genera lo stato successivo
                new_path = path + [(i, move)] # genera il percorso successivo
                new_f = len(new_path) + heuristic(new_state, goal) # calcola la funzione di valutazione
                heapq.heappush(open_set, (new_f, new_state, new_path)) # inserisce lo stato e il percorso nella coda
    return None # se la coda è vuota e non è stato trovato un percorso, restituisce None
```

### Note (DA CORREGGERE!!)
La funzione `a_star` riceve in input la posizione di partenza start, la posizione di arrivo goal, il numero massimo di mosse che ogni cavallo può effettuare max_moves, il numero di cavalieri k e la dimensione della scacchiera N. La funzione utilizza una coda di priorità per tenere traccia degli stati che devono essere esplorati, e la funzione heuristic per calcolare un'euristica ammissibile.

La funzione heuristic calcola la distanza di ogni cavallo dalla sua posizione obiettivo, e restituisce la somma delle distanze massime di ogni cavallo. Questa è un'euristica ammissibile, in quanto la distanza effettiva per raggiungere l'obiettivo non può essere inferiore alla somma delle distanze di ogni cavallo.

Il ciclo principale dell'algoritmo estrae lo stato con il costo f minore dalla coda di priorità, lo esamina e genera tutti i successori. Per ogni successore, l'algoritmo calcola il costo f e lo inserisce nella coda di priorità. Se uno stato è già presente nella coda di priorità con un costo inferiore, non viene inserito di nuovo.

Infine, se la coda di priorità si svuota senza trovare una soluzione, la funzione restituisce None.

## Funzioni comuni
Tutti gli algoritmi scritti sopra utilizzano la funzione `generate_moves`, la quale prende in input due argomenti:
- `pos`: una tupla rappresentante la posizione attuale del cavallo nella forma (row, col).
- `N`: la dimensione della scacchiera.

La funzione itera su tutti i possibili movimenti del cavallo. Per ogni movimento, viene calcolata la posizione della casella di destinazione e, se questa si trova all'interno della scacchiera, la casella di destinazione viene aggiunta all'insieme `moves`.

La funzione restituisce un insieme di tutte le caselle raggiungibili dal cavallo in una scacchiera N x N partendo dalla posizione `pos`.

### Codice
```
def generate_moves(pos, N):
    row, col = pos # estrae la riga e la colonna della posizione
    moves = set() # insieme dei possibili movimenti
    for dr, dc in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]: # per ogni possibile mossa
        r, c = row + dr, col + dc # calcola la nuova posizione
        if 0 <= r < N and 0 <= c < N: # se la nuova posizione è valida
            moves.add((r, c)) # aggiunge la nuova posizione all'insieme dei movimenti
    return moves # restituisce l'insieme dei movimenti
```

## Spiegazione utilizzo
Il progetto si compone di più parti:
### File di input
Diversi esempi in formato json che permettono di caricare velocemente in memoria tutti i dati utili per eseguire gli algoritmi sopra elencati
### File di output
Per ogni file di input corrisponde un file di output (in formato txt) che contiene le informazioni utili sull'esecuzione di tutti gli algoritmi. In particolare contiene il nome dell'algoritmo (nel caso di A* ci sono tutte le varianti con diverse euristiche), il tempo di esecuzione, e l'output fornito
### File algorithm.py
File che contiene il codice per poter eseguire correttamente tutti gli algoritmi
### File ai.py
File di interfaccia che permette di caricare i dati in memoria (inserendo il file che vogliamo testare), richiama l'esecuzione degli algoritmi sul file algorithm.py e scrive tutto sul file di output corretto
## Note
Possiamo notare che diversi algoritmi forniscono diversi output.\
In particolare, i tempi di esecuzione per BFS incrementano quasi esponenzialmente all'aumentare della dimensione del problema (sia per numero di cavalli presenti sia per dimensione della scacchiera), mentre A* sfruttando le euristiche ha una durata molto più breve (anche se aumentando la dimensione i tempi si allungano).\
Inoltre, possiamo notare che i percorsi generati sono diversi, ma tutti arrivano alla soluzione con lo stesso numero di mosse. Questo è dovuto all'ordine di esplorazione di tutte le possibili mosse di ogni cavallo per ogni step.

