import matplotlib.pyplot as plt
import pandas as pd
import datapane as dp

df = pd.read_csv("uso_servicios_municipales.csv")

table = dp.Table(df)
data_table = dp.DataTable(df)
titulo = dp.HTML('<h1 style="color:black;">Resumen ejecutivo – Uso de servicios municipales </h1')
texto = dp.Text("Es importante ya que con esto puede saber con mayor facilidad el mayor número de lo que quiera, además de compararlo con otros posibles datos")
usosAcumulados = df["numero_usos"].sum()

usosBigNumber = dp.BigNumber(
    heading= "## Total uso acumulados",
    value= usosAcumulados
)


mes_datos = df[df["anio"]=="2023"]["numero_usos"].sum()
mes_datos2 = df[df["anio"]=="2022"]["numero_usos"].sum()

comparaBigNumber = dp.BigNumber(
    heading= "## Comparativa anios",
    value= mes_datos,
    change= mes_datos - mes_datos2,
    is_upward_change= mes_datos > mes_datos2
)


report = dp.Report(titulo, texto, usosBigNumber, comparaBigNumber)
report.save(path= "Mora_JC_E2_resumen.html", open = True)