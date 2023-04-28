import pandas as pd
import numpy as np
import os

# Crea la carpeta "text_files" si no existe
if not os.path.exists('../text_files'):
    os.makedirs('../text_files')

# Lee el archivo Excel
xl = pd.ExcelFile('../Informacion.xlsx')

# Itera sobre todas las hojas del archivo de Excel
for sheet_name in xl.sheet_names:
    
    # Lee los datos de la hoja del Excel
    df = xl.parse(sheet_name)
    
    # Reemplaza los valores NaN por un espacio vacío
    df.replace(np.nan, '', inplace=True)

    # Extrae la primera fila como encabezados de las columnas
    headers = list(df.columns.values)

    # Escribe los encabezados en el archivo de texto
    with open(f'../text_files/{sheet_name}', 'w') as f:
        f.write(';'.join(headers) + '\n')

    # Escribe los datos en el archivo de texto
    with open(f'../text_files/{sheet_name}', 'a') as f:
        for index, row in df.iterrows():
            f.write(';'.join([str(x) if str(x) != 'nan' else '' for x in row.tolist()]) + '\n')
