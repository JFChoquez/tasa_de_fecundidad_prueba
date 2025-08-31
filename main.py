import matplotlib
import csv
from matplotlib import pyplot as plt

# Visualización de datos para linux, si eres de windows busca la documentación correspondiente
matplotlib.use("TkAgg")

# Abrimos y almacenamos los datos
X_axis = [] # Año
Y_axis = [] # Hijos por mujer

# Datos extraidos de: https://datos.bancomundial.org/indicador/SP.DYN.TFRT.IN?end=2023&locations=PE&start=1960&view=chart
with open("./peru.csv") as data:
    csv_reader = csv.reader(data)

    for year in next(csv_reader):
        X_axis.append(int(year))

    for n in next(csv_reader):
        Y_axis.append(float(n))

print(X_axis)
print(Y_axis)

# Creamos un grafico de barras
plt.bar(X_axis, Y_axis)

plt.xlabel("Año")
plt.ylabel("Hijos por mujer")

plt.show()
