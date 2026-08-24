import sqlite3
import pandas as pd

# 1. Cargar el CSV y conectar a SQLite
df = pd.read_csv("incidentes_sst.csv")
conn = sqlite3.connect("sst_database.db")
df.to_sql("incidentes_sst", conn, if_exists="replace", index=False)

# 2. Definir las consultas de análisis
consultas = {
    "1. Total de incidentes y días de incapacidad por área": """
        SELECT Area, COUNT(ID_Incidente) AS Total_Incidentes, SUM(Dias_Incapacidad) AS Total_Dias_Incapacidad
        FROM incidentes_sst
        GROUP BY Area
        ORDER BY Total_Incidentes DESC;
    """,
    "2. Distribución de accidentes por Causa Raíz": """
        SELECT Causa_Raiz, COUNT(*) AS Cantidad,
               ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM incidentes_sst WHERE Tipo_Incidente = 'Accidente de Trabajo'), 2) AS Porcentaje
        FROM incidentes_sst
        WHERE Tipo_Incidente = 'Accidente de Trabajo'
        GROUP BY Causa_Raiz
        ORDER BY Cantidad DESC;
    """,
    "3. Tendencia mensual de accidentes vs casi accidentes": """
        SELECT strftime('%Y-%m', Fecha) AS Mes,
               COUNT(CASE WHEN Tipo_Incidente = 'Accidente de Trabajo' THEN 1 END) AS Total_Accidentes,
               COUNT(CASE WHEN Tipo_Incidente = 'Casi Accidente (Near Miss)' THEN 1 END) AS Total_Casi_Accidentes
        FROM incidentes_sst
        GROUP BY Mes
        ORDER BY Mes ASC;
    """
}

# 3. Imprimir resultados en consola
for titulo, query in consultas.items():
    print(f"\n--- {titulo} ---")
    resultado = pd.read_sql_query(query, conn)
    print(resultado.to_string(index=False))

conn.close()