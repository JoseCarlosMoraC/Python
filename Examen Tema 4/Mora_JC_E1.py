import matplotlib.pyplot as plt
import pandas as pd
import datapane as dp

df = pd.read_csv("uso_servicios_municipales.csv")

table = dp.Table(df)
data_table = dp.DataTable(df)


report = dp.Report(table, data_table)
report.save(path= "Mora_JC_E1_tabla.html", open = True)