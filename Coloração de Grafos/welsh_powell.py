def welsh_powell(graph):
    
    n = len(graph)
    
    # obtem os graus dos vrtices
    degrees = [(vertex, len(neighbors)) for vertex, neighbors in graph.items()]
    # ordena os vértices em ordem decrescente de grau
    degrees.sort(key=lambda x: x[1], reverse=True)
    
    # inicializa as cores dos vértices como não atribuídas
    result = [-1] * n
    
    # atribui cores aos vértices
    current_color = 0
    for vertex, _ in degrees:
        if result[vertex] == -1:
            # atribui a cor atual ao vértice
            result[vertex] = current_color
            
            # marca todos os vizinhos que não podem receber essa cor
            for neighbor in graph[vertex]:
                if result[neighbor] == -1:  # Se o vizinho ainda não foi colorido
                    forbidden_colors = {result[neigh] for neigh in graph[neighbor] if result[neigh] != -1}
                    if current_color not in forbidden_colors:
                        result[neighbor] = current_color

            current_color += 1  # Passa para a próxima cor

    return result

graph = {
    0: [1, 2, 3],
    1: [0, 2, 4],
    2: [0, 1, 3, 4],
    3: [0, 2, 4],
    4: [1, 2, 3]
}

coloring = welsh_powell(graph)
print("Coloração dos vértices:", coloring)
