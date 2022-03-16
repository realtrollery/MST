INF = float('inf')
Graph =
N = len(Graph)
selected_node = [0, 0, 0, 0, 0]

no_edge = 0

selected_node[0] = True
print("Edge : Weight\n")
while (no_edge < N - 1):
    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if (not selected_node[n]) and Graph[m][n]:
                    if minimum > Graph[m][n]:
                        minimum = Graph[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":" + str(Graph[a][b]))
    selected_node[b] = True
    no_edge += 1
