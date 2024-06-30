def brelaz(graph):
    num_vertices = len(graph)
    colors = [-1] * num_vertices
    degree_saturation = [0] * num_vertices
    degrees = [len(graph[v]) for v in range(num_vertices)]

    max_degree_vertex = degrees.index(max(degrees))
    colors[max_degree_vertex] = 0
    num_colors = 1

    while -1 in colors:
        for vertex in range(num_vertices):
            if colors[vertex] == -1:
                neighbors_colors = {colors[neighbor] for neighbor in graph[vertex] if colors[neighbor] != -1}
                degree_saturation[vertex] = len(neighbors_colors)

        max_saturation = max(degree_saturation)
        candidates = [v for v in range(num_vertices) if degree_saturation[v] == max_saturation and colors[v] == -1]
        if candidates:
            if len(candidates) > 1:
                selected_vertex = max(candidates, key=lambda v: degrees[v])
            else:
                selected_vertex = candidates[0]
        else:
            break

        used_colors = {colors[neighbor] for neighbor in graph[selected_vertex] if colors[neighbor] != -1}
        for color in range(num_colors):
            if color not in used_colors:
                colors[selected_vertex] = color
                break
        else:
            colors[selected_vertex] = num_colors
            num_colors += 1
        
        degree_saturation[selected_vertex] = -1

    return colors

graph = {
    0: [1, 2, 3],
    1: [0, 2, 4],
    2: [0, 1, 3, 4],
    3: [0, 2, 4],
    4: [1, 2, 3]
}
print(brelaz(graph))
