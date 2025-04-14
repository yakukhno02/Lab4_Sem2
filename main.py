import tkinter as tk
from graph_generator import generate_adjacency_matrices
from draw_graph import draw_graph
from graph_analysis import (
    get_degrees_directed,
    get_degrees_undirected,
    is_regular,
    get_isolated_and_leaf_vertices,
    transitive_closure,
    strong_connectivity_matrix,
    get_strong_components,
    build_condensation_graph,
    find_paths_of_length_2,
    find_paths_of_length_3
)

def print_matrix(matrix, name):
    print(f"\n{name} (розмір {len(matrix)}x{len(matrix[0])}):")
    for row in matrix:
        print(" ".join(str(elem) for elem in row))


n1, n2, n3, n4 = 4, 1, 3, 3
Adir, Aundir, n = generate_adjacency_matrices(n1, n2, n3, n4)

print_matrix(Adir, "Матриця суміжності напрямленого графа Adir")
print_matrix(Aundir, "Матриця суміжності ненапрямленого графа Adir")

root = tk.Tk()
root.title("Графи")
canvas = tk.Canvas(root, width=1300, height=900, bg="white")
canvas.pack()

draw_graph(canvas, Adir, directed=True, n=n, offset_x=0, offset_y=100)
draw_graph(canvas, Aundir, directed=False, n=n, offset_x=650, offset_y=100)
canvas.create_text(325, 20, text="Напрямлений граф", font=("Arial", 14, "bold"))
canvas.create_text(975, 20, text="Ненапрямлений граф", font=("Arial", 14, "bold"))

in_deg, out_deg = get_degrees_directed(Adir)
deg_undir = get_degrees_undirected(Aundir)
total_deg_dir = [in_deg[i] + out_deg[i] for i in range(n)]

print("🔷 Напівстепені та повні степені:")
print(" Вершина | Напівстеп. заходу | Напівстеп. виходу | Повний степінь")
for i in range(n):
    print(f"{i+1:>8} | {in_deg[i]:>17} | {out_deg[i]:>17} | {total_deg_dir[i]:>16}")

is_reg_dir, reg_val_dir = is_regular(total_deg_dir)
print(f"\nРегулярний: {'Yes' if is_reg_dir else 'No'}, Degree: {reg_val_dir if is_reg_dir else '—'}")

isolated_dir, leaf_dir = get_isolated_and_leaf_vertices(total_deg_dir)
print(f"Ізольовані вершини: {isolated_dir}")
print(f"Висячі вершини: {leaf_dir}")

print("\n🔶 Ненапрямлений граф:")
print(" Вершина | Степінь")
for i in range(n):
    print(f"{i+1:>8} | {deg_undir[i]:>7}")

is_reg_undir, reg_val_undir = is_regular(deg_undir)
print(f"\nРегулярний: {'Так' if is_reg_undir else 'Ні'}, Степінь: {reg_val_undir if is_reg_undir else '—'}")

isolated_undir, leaf_undir = get_isolated_and_leaf_vertices(deg_undir)
print(f"Ізольовані вершини: {isolated_undir}")
print(f"Висячі вершини: {leaf_undir}")

def print_matrix(matrix, name):
    print(f"\n{name} (розмір {len(matrix)}x{len(matrix[0])}):")
    for row in matrix:
        print(" ".join(str(elem) for elem in row))

print_matrix(Adir, "Матриця суміжності напрямленого графа Adir")
print_matrix(Aundir, "Матриця суміжності ненапрямленого графа Aundir")

def print_paths_limited(paths, title, max_width=100):
    print(f"\n{title}")
    current_line = ""
    for path in paths:
        path_str = "→".join(map(str, path))
        if len(current_line) + len(path_str) + 2 > max_width:
            print(current_line.strip())
            current_line = ""
        current_line += path_str + "  "
    if current_line:
        print(current_line.strip())

paths_2 = find_paths_of_length_2(Adir)
paths_3 = find_paths_of_length_3(Adir)

print_paths_limited(paths_2, "🔁 Шляхи довжини 2:")
print_paths_limited(paths_3, "🔁 Шляхи довжини 3:")

reach = transitive_closure(Adir)
print_matrix(reach, "🧭 Матриця досяжності")

strong = strong_connectivity_matrix(reach)
print_matrix(strong, "🔗 Матриця сильної зв’язності")

components = get_strong_components(strong)
print("\n📦 Компоненти сильної зв’язності:")
for i, comp in enumerate(components, 1):
    print(f"Компонента {i}: {comp}")

cond_matrix = build_condensation_graph(Adir, components)
print_matrix(cond_matrix.tolist(), "🧩 Матриця графа конденсації")

draw_graph(canvas, cond_matrix.tolist(), directed=True, n=len(components), offset_x=325, offset_y=650)
canvas.create_text(650, 580, text="Граф конденсації", font=("Arial", 14, "bold"))

root.mainloop()