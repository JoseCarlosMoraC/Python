import pandas as pd
import matplotlib.pyplot as plt
import datapane as dp

#Cargo el CSV con los datos de ventas
df = pd.read_csv(
    "C:/Users/alumno/Desktop/DAM/Proyectos Python/Tema 4/DI_U05_A02_PP_E_01.csv"
)

#Creo gráfico 1: Ventas por producto
ventas_producto = df.groupby("Tipo de producto")["Ventas"].sum()
fig1, ax1 = plt.subplots()
ax1.pie(ventas_producto, labels=ventas_producto.index, startangle=90)
ax1.set_title("Distribución de ventas por tipo de producto")

#Creo gráfico 2: Barras de ventas por región
ventas_region = df.groupby("Región")["Ventas"].sum()
fig2, ax2 = plt.subplots()
ax2.bar(ventas_region.index, ventas_region.values)
ax2.set_title("Ventas por región")

#Creo gráfico 3: Línea de evolución anual
ventas_anuales = df.groupby("Año")["Ventas"].sum()
fig3, ax3 = plt.subplots()
ax3.plot(ventas_anuales.index, ventas_anuales.values, marker="o")
ax3.set_title("Evolución de ventas por año")

# Creo la tabla resumen de ventas por región
tabla_resumen = df.groupby("Región")["Ventas"].sum()



informe = dp.Report(
    # Creo la página 1 con vista general
    dp.Page(
        title="Resumen",
        blocks=[
            dp.Text("# Informe de Ventas"),
            
            # Uso un grupo para poner dos gráficos lado a lado
            dp.Group(
                dp.Plot(fig1),
                dp.Plot(fig2),
                columns=2
            )
        ]
    ),
    
    # Creo la página 2 con análisis detallado
    dp.Page(
        title="Detalles",
        blocks=[
            dp.Text("## Análisis detallado"),
            dp.Plot(fig3),
            
            # Uso SELECTOR para alternar entre gráfico y tabla
            dp.Select(
                blocks=[
                    dp.Plot(fig2, label="Ver gráfico"),
                    dp.DataTable(tabla_resumen, label="Ver tabla")
                ]
            )
        ]
    )
)

# Guardo el informe como HTML
informe.save("Mora_JC_T4.4.html", open=True)