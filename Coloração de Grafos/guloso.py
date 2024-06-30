def greedy_coloring(graph):
    
    n = len(graph)
    result = [-1] * n  # inicializa todas as cores como n atribuídas

    # inicializa a cor do primeiro vrtice com 0
    result[0] = 0

    # array temporario para armazenar as cores disponíveis
    available = [False] * n

    # atribui cores aos outros vértices
    for u in range(1, n):
        # marca as cores dos vizinhos de u como indisponíveis
        for i in graph[u]:
            if result[i] != -1:
                available[result[i]] = True

        # encontra a primeira cor disponível
        color = 0
        while color < n:
            if not available[color]:
                break
            color += 1

        result[u] = color  # Atribui a cor ao vértice u

        # Reseta as cores disponíveis para a próxima iteração
        for i in graph[u]:
            if result[i] != -1:
                available[result[i]] = False

    return result

graph = {
    0: [1, 2, 3],
    1: [0, 2, 4],
    2: [0, 1, 3, 4],
    3: [0, 2, 4],
    4: [1, 2, 3]
}

coloring = greedy_coloring(graph)
print("Coloração dos vértices:", coloring)
