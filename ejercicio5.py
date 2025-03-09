import matplotlib.pyplot as plt
import numpy as np

def intersection(p1, p2, p3, p4):
    """Encuentra la intersección de dos líneas definidas por los puntos p1-p2 y p3-p4."""
    A1 = p2[1] - p1[1]
    B1 = p1[0] - p2[0]
    C1 = A1 * p1[0] + B1 * p1[1]
    
    A2 = p4[1] - p3[1]
    B2 = p3[0] - p4[0]
    C2 = A2 * p3[0] + B2 * p3[1]
    
    det = A1 * B2 - A2 * B1
    if det == 0:
        return None  # Líneas paralelas
    
    x = (B2 * C1 - B1 * C2) / det
    y = (A1 * C2 - A2 * C1) / det
    return np.array([x, y])

# Definir los puntos del triángulo
A = np.array([0, 0])
B = np.array([7, 0])

# Ángulos dados
theta_A = np.radians(30)
theta_B = np.radians(70)

# Calcular la posición del punto C usando trigonometría
C_x = B[0] - np.cos(theta_B) * 7 / np.sin(theta_A + theta_B) * np.sin(theta_A)
C_y = np.sin(theta_B) * 7 / np.sin(theta_A + theta_B) * np.sin(theta_A)
C = np.array([C_x, C_y])

# Calcular alturas
H_C = np.array([C[0], 0])  # Altura desde C a AB

# Altura desde A a BC
slope_BC = (C[1] - B[1]) / (C[0] - B[0])
perp_slope_A = -1 / slope_BC
A_height_x = (C[0] + B[0]) / 2
A_height_y = perp_slope_A * (A_height_x - A[0]) + A[1]
H_A = intersection(A, np.array([A_height_x, A_height_y]), B, C)

# Altura desde B a AC
slope_AC = (C[1] - A[1]) / (C[0] - A[0])
perp_slope_B = -1 / slope_AC
B_height_x = (C[0] + A[0]) / 2
B_height_y = perp_slope_B * (B_height_x - B[0]) + B[1]
H_B = intersection(B, np.array([B_height_x, B_height_y]), A, C)

# Encontrar el ortocentro
ortocentro = intersection(A, H_A, B, H_B)

# Graficar el triángulo
plt.figure(figsize=(6,6))
plt.plot([A[0], B[0]], [A[1], B[1]], 'bo-', label="Lado AB")
plt.plot([B[0], C[0]], [B[1], C[1]], 'go-', label="Lado BC")
plt.plot([C[0], A[0]], [C[1], A[1]], 'ro-', label="Lado CA")

# Dibujar las alturas
plt.plot([C[0], H_C[0]], [C[1], H_C[1]], 'k--', label="Altura desde C")
plt.plot([A[0], H_A[0]], [A[1], H_A[1]], 'k--', label="Altura desde A")
plt.plot([B[0], H_B[0]], [B[1], H_B[1]], 'k--', label="Altura desde B")

# Marcar los puntos
plt.scatter(*A, color='b', label='A (0,0)')
plt.scatter(*B, color='b', label='B (7,0)')
plt.scatter(*C, color='b', label='C')
plt.scatter(*ortocentro, color='r', marker='x', s=100, label='Ortocentro')

plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Triángulo con alturas y ortocentro")
plt.grid(True)
plt.show()
