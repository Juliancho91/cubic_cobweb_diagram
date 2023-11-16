import matplotlib.pyplot as plt  # Importa la librería matplotlib para visualización de gráficos
import numpy as np  # Importa la librería NumPy para operaciones numéricas

# Función para crear un diagrama de telaraña (cobweb) con argumentos (funcion. semilla, cantidad de iteraciones, titulo, valor de lambda, valor inicial, valor final)
def cobweb(func, x0, num_iterations, title="Cobweb Diagram", lam=1, a=-1, b=1):
    x = np.linspace(a, b, 1000)  # Crea un conjunto de valores de x equidistantes en el intervalo [a, b]
    y = func(x, lam)  # Calcula los valores de la función 'func' para cada valor de x

    plt.figure(figsize=(8, 6))  # Crea una figura para el gráfico con tamaño específico (8,6)
    plt.plot(x, y, label='f(x)', color='black')  # Grafica la función 'f(x)' en color negro
    plt.plot(x, x, label='y=x', linestyle='--', color='lime')  # Grafica la línea y=x en color lima y estilo discontinuo

    xn = x0  # Establece el valor inicial de x
    for _ in range(num_iterations):  # Realiza un bucle para el número dado de iteraciones
        yn = func(xn, lam)  # Calcula el valor de la función para xn
        if yn > xn:  # Si el valor de la función es mayor que xn
            # Grafica líneas en color turquesa para representar la iteración
            plt.plot([xn, yn], [yn, yn], color='turquoise', linestyle='-', linewidth=1)
            plt.plot([xn, xn], [xn, yn], color='turquoise', linestyle='-', linewidth=1)
        else:  # Si el valor de la función es menor o igual a xn
            # Grafica líneas en color rosa para representar la iteración
            plt.plot([xn, yn], [yn, yn], color='deeppink', linestyle='-', linewidth=1)
            plt.plot([xn, xn], [xn, yn], color='deeppink', linestyle='-', linewidth=1)
        xn = yn  # Actualiza xn con el nuevo valor yn para la próxima iteración

    plt.title(title)  # Establece el título del gráfico
    plt.xlabel('x')  # Etiqueta del eje x
    plt.ylabel('$f_{%s}(x)$' % lam, fontsize=14)  # Etiqueta del eje y con formato LaTeX
    plt.legend()  # Muestra la leyenda en el gráfico
    plt.grid()  # Muestra una cuadrícula en el gráfico

    plt.show()  # Muestra el gráfico generado

# Ejemplos de uso:

# Define la función cúbica:
def cubic_func(x, lam):
    return lam * x - x**3

cobweb(cubic_func, -0.1, 14, title="Diagrama de telaraña", lam=-1.1, a=-0.6, b=0.6)

cobweb(cubic_func, -0.5, 50, title="Diagrama de telaraña", lam=0, a=-0.6, b=0.6)

cobweb(cubic_func, -0.99, 15, title="Diagrama de telaraña", lam=0, a=-1.1, b=1.1)

#definimos otra función, en este caso 2-ciclo de la anterior:
def cubic_func_2(x, lam):
    return lam * ( lam * x - x**3) - ( lam * x - x**3) ** 3

cobweb(cubic_func_2, 0.1, 14, title="Diagrama de telaraña 2-ciclo", lam=3, a=-2, b=2)
