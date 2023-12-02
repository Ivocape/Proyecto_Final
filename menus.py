from collections import Counter
import matplotlib.pyplot as plt


# Datos para el gráfico de barras
categorias = ['Categoria 1', 'Categoria 2', 'Categoria 3', 'Categoria 1', 'Categoria 2', 'Categoria 3', 'Categoria 1', 'Categoria 4']
# Suponiendo que estas son tus categorías

# Contar la frecuencia de cada categoría
frecuencia = Counter(categorias)

# Obtener las categorías y las frecuencias por separado
categorias = list(frecuencia.keys())
valores = list(frecuencia.values())

# Crear el gráfico de barras
plt.bar(categorias, valores, color='blue')

# Añadir etiquetas y título
plt.xlabel('Categorías')
plt.ylabel('Frecuencia')
plt.title('Gráfico de Barras de Frecuencia')

# Mostrar el gráfico
plt.show()
