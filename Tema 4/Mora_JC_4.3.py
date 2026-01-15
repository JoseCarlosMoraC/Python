import pandas as pd
import matplotlib.pyplot as plt
import datapane as dp

df = pd.read_csv(
    "C:/Users/alumno/Desktop/DAM/Proyectos Python/Tema 4/DI_U05_A02_PP_E_01.csv"
)

#Caso 1
ventas_producto = df.groupby("Tipo de producto")["Ventas"].sum()

fig1, ax1 = plt.subplots()
ax1.pie(
    ventas_producto,
    labels=ventas_producto.index,
    startangle=90
)
ax1.set_title("Distribución de ventas por tipo de producto")

#Caso 2
ventas_anuales = df.groupby("Año")["Ventas"].sum()

fig2, ax2 = plt.subplots()
ax2.plot(
    ventas_anuales.index,
    ventas_anuales.values,
    marker="o"
)
ax2.set_xlabel("Año")
ax2.set_ylabel("Ventas totales")
ax2.set_title("Evolución de las ventas totales por año")

#Caso 3
ventas_region = df.groupby("Región")["Ventas"].sum()

fig3, ax3 = plt.subplots()
ax3.bar(
    ventas_region.index,
    ventas_region.values
)
ax3.set_xlabel("Región")
ax3.set_ylabel("Ventas totales")
ax3.set_title("Ventas totales por región")

informe = dp.Report(
    dp.Text("# Informe de Ventas"),
    dp.Text("## Distribución de ventas por tipo de producto"),
    dp.Plot(fig1),
    dp.Text("## Evolión de las ventas en los últimos años"),
    dp.Plot(fig2),
    dp.Text("## Ventas totales por región"),
    dp.Plot(fig3)
)

informe.save("Mora_JC_4.3.html", open=True)
