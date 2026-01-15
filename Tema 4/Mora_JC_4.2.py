import pandas as pd
import datapane as dp


csv_path = r"C:\Users\alumno\Desktop\DAM\Proyectos Python\Tema 4\DI_U05_A02_PP_E_01.csv"
df = pd.read_csv(csv_path)
df.columns = df.columns.str.strip()


total_ventas = df["Ventas"].sum()
ventas_por_anio = df.groupby("Año")["Ventas"].sum()
anio_max = ventas_por_anio.idxmax()
ventas_2021 = ventas_por_anio.loc[2021]
ventas_2020 = ventas_por_anio.loc[2020]
diferencia = ventas_2021 - ventas_2020

region_max_2021 = df[df["Año"] == 2021].groupby("Región")["Ventas"].sum().idxmax()
tipo_max_total = df.groupby("Tipo de producto")["Ventas"].sum().idxmax()


bn_total = dp.BigNumber(
    heading="Ventas acumuladas",
    value="{:,.0f} €".format(total_ventas)
)
bn_anio = dp.BigNumber(
    heading="Año con mayores ventas",
    value=str(anio_max)
)
bn_2021 = dp.BigNumber(
    heading="Ventas 2021",
    value="{:,.0f} €".format(ventas_2021),
    prev_value="{:,.0f} €".format(ventas_2020),
    change="{:,.0f} €".format(diferencia),
    is_upward_change=diferencia >= 0
)


tabla = dp.DataTable(df)


resumen_texto = (
    "Resumen \n"
    "Total de ventas acumuladas: " + "{:,.0f} €".format(total_ventas) + "\n"
    "Año con mayores ventas: " + str(anio_max) + "\n"
    "Región con mayores ventas 2021: " + str(region_max_2021) + "\n"
    "Tipo de producto con más ventas totales: " + str(tipo_max_total)
)

report = dp.Report(
    dp.Text("Informe de Ventas"),
    dp.Text(resumen_texto),
    dp.Group(bn_total, bn_anio, columns=2),
    bn_2021,
    dp.Text("Tabla completa de ventas"),
    tabla
)


dp.save_report(report, path="informe_ventas.html", open=True)
