import numpy as np

def get_degrees_directed(matrix):
    n = len(matrix)
    out_degrees = [sum(matrix[i]) for i in range(n)]
    in_degrees = [sum(matrix[j][i] for j in range(n)) for i in range(n)]
    return in_degrees, out_degrees

def get_degrees_undirected(matrix):
    return [sum(row) for row in matrix]

def is_regular(degrees):
    return all(d == degrees[0] for d in degrees), degrees[0] if degrees else 0

def get_isolated_and_leaf_vertices(degrees):
    isolated = [i + 1 for i, d in enumerate(degrees) if d == 0]
    leaf = [i + 1 for i, d in enumerate(degrees) if d == 1]
    return isolated, leaf

def multiply_matrices(A, B):
    return (np.dot(A, B) > 0).astype(int)

def power_matrix(A, k):
    result = np.array(A, dtype=int)
    for _ in range(k - 1):
        result = multiply_matrices(result, A)
    return result

def transitive_closure(A):
    n = len(A)
    R = np.array(A, dtype=int)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if R[i][k] and R[k][j]:
                    R[i][j] = 1
    return R

def strong_connectivity_matrix(R):
    n = len(R)
    S = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            if R[i][j] and R[j][i]:
                S[i][j] = 1
    return S

def get_strong_components(S):
    n = len(S)
    visited = [False] * n
    components = []

    for i in range(n):
        if not visited[i]:
            component = []
            for j in range(n):
                if S[i][j]:
                    component.append(j + 1)
                    visited[j] = True
            components.append(component)
    return components

def build_condensation_graph(Adir, components):
    n = len(components)
    cond_graph = np.zeros((n, n), dtype=int)
    node_to_component = {}

    for comp_index, comp in enumerate(components):
        for node in comp:
            node_to_component[node - 1] = comp_index

    for i in range(len(Adir)):
        for j in range(len(Adir)):
            if Adir[i][j]:
                if i not in node_to_component or j not in node_to_component:
                    continue
                ci = node_to_component[i]
                cj = node_to_component[j]

                if ci != cj:
                    cond_graph[ci][cj] = 1

    return cond_graph

def find_paths_of_length_2(adj_matrix):
    n = len(adj_matrix)
    paths = []
    for i in range(n):
        for j in range(n):
            if i != j:
                for k in range(n):
                    if adj_matrix[i][k] and adj_matrix[k][j]:
                        paths.append([i + 1, k + 1, j + 1])
    return paths

def find_paths_of_length_3(adj_matrix):
    n = len(adj_matrix)
    paths = []
    for i in range(n):
        for j in range(n):
            if i != j:
                for k in range(n):
                    for l in range(n):
                        if adj_matrix[i][k] and adj_matrix[k][l] and adj_matrix[l][j]:
                            paths.append([i + 1, k + 1, l + 1, j + 1])
    return paths


