import numpy as np
import matplotlib.pyplot as plt

#datos del problema
lado1 = 3 #pulgadas
lado2 = 4 #pulgadas
angulo =np.radians(60) # Convertir a riadianes

#Coordenadas de los puntos
A = (0, 0) #origen
B = (lado2, 0) #punto en el eje x
C = (lado1 * np.cos(angulo), lado1 + np.sin(angulo)) #tercer vertice usando trigonometria

#funcion para calcular el punto medio de un segmento
def punto_medio(P1, P2):
    return ((P1[0] + P2[0]) / 2, (P1[1] + P2[1]) / 2)

#calculo de los puntos medios
M_BC = punto_medio(B, C)
M_CA = punto_medio(C, A)
M_AB = punto_medio(A, B)

#calculo de baricentro (promedio de los vertices)
baricentro = ((A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3)

# Graficar el triángulo
plt.figure(figsize=(6,6))
plt.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]], 'b-', label="Triángulo")

# Graficar las medianas
plt.plot([A[0], M_BC[0]], [A[1], M_BC[1]], 'r--', label="Medianas")
plt.plot([B[0], M_CA[0]], [B[1], M_CA[1]], 'r--')
plt.plot([C[0], M_AB[0]], [C[1], M_AB[1]], 'r--')

# Graficar el baricentro
plt.scatter(*baricentro, color='purple', label='Baricentro', zorder=3)
plt.text(baricentro[0], baricentro[1], '  G', fontsize=12, verticalalignment='bottom')

# Etiquetas de los vértices
plt.text(A[0], A[1], '  A', fontsize=12, verticalalignment='bottom')
plt.text(B[0], B[1], '  B', fontsize=12, verticalalignment='bottom')
plt.text(C[0], C[1], '  C', fontsize=12, verticalalignment='bottom')

# Configuración del gráfico
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend()
plt.title("Triángulo con Medianas y Baricentro")
plt.show()
