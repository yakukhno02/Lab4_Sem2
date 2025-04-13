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
