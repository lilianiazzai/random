from collections import deque

def is_bipartite(graph):
    
    n = len(graph)
    color = [-1] * n  # -1 significa que o vértice ainda não foi colorido.

    for start in range(n):
        if color[start] == -1:  # se o vértice não foi colorido, começa uma nova BFS.
            queue = deque([start])
            color[start] = 0  # começa colorindo o vertice com a cor 0.

            while queue:
                node = queue.popleft()

                for neighbor in graph[node]:
                    if color[neighbor] == -1:  # se o vizinho n foi colorido, colorimos ele com a cor oposta.
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:  # se o vizinho tem a mesma cor, o grafo n eh bipartido.
                        return False
    return True

graph = {
    0: [1, 2, 3],
    1: [0, 2, 4],
    2: [0, 1, 3, 4],
    3: [0, 2, 4],
    4: [1, 2, 3]
}

bipartite_check = is_bipartite(graph)
print("O grafo é bipartido?", bipartite_check)
