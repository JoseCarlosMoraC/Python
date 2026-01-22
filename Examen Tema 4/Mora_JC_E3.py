import matplotlib.pyplot as plt
import pandas as pd
import datapane as dp

df = pd.read_csv("uso_servicios_municipales.csv")

table = dp.Table(df)
data_table = dp.DataTable(df)
sectores = df.groupby("servicio")["numero_usos"].sum().plot.pie(title = "Grafico de sectores")
graficoDeSector = dp.Plot(plt.gcf())
plt.close()
lineas = df.groupby("anio")["numero_usos"].sum().plot.line(title = "Grafico de lineas")
graficoLineas = dp.Plot(plt.gcf())
plt.close()

lineas = df.groupby("distrito")["numero_usos"].sum().plot.bar(title = "Grafico de barras")
graficoBarras = dp.Plot(plt.gcf())
plt.close()

report = dp.Report(graficoDeSector, graficoLineas, graficoBarras)
report.save(path= "Mora_JC_E3_graficos.html", open = True)