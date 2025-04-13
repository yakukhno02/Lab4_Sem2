import tkinter as tk
from graph_generator import generate_adjacency_matrices
from draw_graph import draw_graph
from graph_analysis import (
    get_degrees_directed,
    get_degrees_undirected,
    is_regular,
    get_isolated_and_leaf_vertices
)


n1, n2, n3, n4 = 4, 1, 3, 3
Adir, Aundir, n = generate_adjacency_matrices(n1, n2, n3, n4)

root = tk.Tk()
root.title("Графи")
canvas = tk.Canvas(root, width=1300, height=600, bg="white")
canvas.pack()

draw_graph(canvas, Adir, directed=True, n=n, offset_x=0)
draw_graph(canvas, Aundir, directed=False, n=n, offset_x=650)

canvas.create_text(325, 20, text="Напрямлений граф", font=("Arial", 14, "bold"))
canvas.create_text(975, 20, text="Ненапрямлений граф", font=("Arial", 14, "bold"))

# 🔍 Аналіз графів

# 1. Ступені та напівступені
in_deg, out_deg = get_degrees_directed(Adir)
deg_undir = get_degrees_undirected(Aundir)

print("🔷 Напрямлений граф:")
print(" Вершина | Напівстеп. заходу | Напівстеп. виходу | Повний степінь")
total_deg_dir = []
for i in range(n):
    total = in_deg[i] + out_deg[i]
    total_deg_dir.append(total)
    print(f"{i+1:>8} | {in_deg[i]:>17} | {out_deg[i]:>17} | {total:>16}")

# 3. Регулярність напрямленого графа
is_reg_dir, reg_val_dir = is_regular(total_deg_dir)
print(f"\nРегулярний: {'Yes' if is_reg_dir else 'No'}, Degree: {reg_val_dir if is_reg_dir else '—'}")

# 4. Ізольовані та висячі вершини (напрямлений)
isolated_dir, leaf_dir = get_isolated_and_leaf_vertices(total_deg_dir)
print(f"Ізольовані вершини: {isolated_dir}")
print(f"Висячі вершини: {leaf_dir}")

print("\n🔶 Ненапрямлений граф:")
print(" Вершина | Степінь")
for i in range(n):
    print(f"{i+1:>8} | {deg_undir[i]:>7}")

# 3. Регулярність ненапрямленого графа
is_reg_undir, reg_val_undir = is_regular(deg_undir)
print(f"\nРегулярний: {'Так' if is_reg_undir else 'Ні'}, Степінь: {reg_val_undir if is_reg_undir else '—'}")

# 4. Ізольовані та висячі вершини (ненапрямлений)
isolated_undir, leaf_undir = get_isolated_and_leaf_vertices(deg_undir)
print(f"Ізольовані вершини: {isolated_undir}")
print(f"Висячі вершини: {leaf_undir}")

# 5. Вивід матриць
def print_matrix(matrix, name):
    print(f"\n{name} (розмір {len(matrix)}x{len(matrix[0])}):")
    for row in matrix:
        print(" ".join(str(elem) for elem in row))

print_matrix(Adir, "Матриця суміжності напрямленого графа Adir")
print_matrix(Aundir, "Матриця суміжності ненапрямленого графа Aundir")

root.mainloop()
