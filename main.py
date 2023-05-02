import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
import os

class ExcelToTextConverter:
    def __init__(self, master):
        self.master = master
        master.title("Convertidor Xlsx -> Gtfs")

        # Crear los widgets
        self.file_label = tk.Label(master, text="Seleccionar archivo de Excel:")
        self.file_button = tk.Button(master, text="Buscar archivo", command=self.select_file)
        self.filename_label = tk.Label(master, text="")
        self.convert_button = tk.Button(master, text="Convertir a archivos de texto", state=tk.DISABLED, command=self.convert)
        self.status_label = tk.Label(master, text="", fg="green")

        # Colocar los widgets en la ventana
        self.file_label.grid(row=0, column=0, padx=10, pady=10)
        self.file_button.grid(row=0, column=1, padx=10, pady=10)
        self.filename_label.grid(row=1, column=0, padx=10, pady=10)
        self.convert_button.grid(row=1, column=1, padx=10, pady=10)
        self.status_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def select_file(self):
        # Mostrar un diálogo para seleccionar el archivo de Excel
        self.filename = filedialog.askopenfilename()
        self.filename_label.config(text=self.filename)
        self.convert_button.config(state=tk.NORMAL)
        self.status_label.config(text="")

    def convert(self):
        # Lee el archivo Excel
        xl = pd.ExcelFile(self.filename)

        # Crea la carpeta "text_files" si no existe
        if not os.path.exists('../text_files'):
            os.makedirs('../text_files')

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
                f.write(','.join(headers) + '\n')

            # Escribe los datos en el archivo de texto
            with open(f'../text_files/{sheet_name}', 'a') as f:
                for index, row in df.iterrows():
                    f.write(','.join([str(x) if str(x) != 'nan' else '' for x in row.tolist()]) + '\n')

        self.status_label.config(text="La conversión se completó exitosamente.")

root = tk.Tk()
app = ExcelToTextConverter(root)
root.mainloop()