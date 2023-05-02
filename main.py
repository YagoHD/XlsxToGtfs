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
        self.dir_label = tk.Label(master, text="Seleccionar directorio de salida:")
        self.dir_button = tk.Button(master, text="Buscar directorio", command=self.select_directory)
        self.dir_selected_label = tk.Label(master, text="", fg="blue",font="BOLD")
        self.filename_label = tk.Label(master, text="", fg="blue",font="BOLD")
        self.convert_button = tk.Button(master, text="Convertir a archivos de texto", state=tk.DISABLED, command=self.convert)
        self.status_label = tk.Label(master, text="", fg="green", font="BOLD")

        # Colocar los widgets en la ventana
        self.file_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.file_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.filename_label.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.dir_label.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        self.dir_button.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
        self.dir_selected_label.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")
        self.convert_button.grid(row=6, column=0, padx=10, pady=10, sticky="nsew")
        self.status_label.grid(row=7, column=0, padx=10, pady=10, sticky="nsew")

    def select_file(self):
        # Mostrar un diálogo para seleccionar el archivo de Excel
        self.filename = filedialog.askopenfilename()
        self.filename_label.config(text=self.filename)
        self.convert_button.config(state=tk.NORMAL)
        self.status_label.config(text="")

    def select_directory(self):
        # Mostrar un diálogo para seleccionar el directorio de salida
        self.directory = filedialog.askdirectory()
        self.dir_selected_label.config(text=self.directory)

    def convert(self):
        # Lee el archivo Excel
        xl = pd.ExcelFile(self.filename)

        # Crea la carpeta "text_files" en el directorio seleccionado si no existe
        text_files_directory = os.path.join(self.directory, 'text_files')
        if not os.path.exists(text_files_directory):
            os.makedirs(text_files_directory)

        # Itera sobre todas las hojas del archivo de Excel
        for sheet_name in xl.sheet_names:

            # Lee los datos de la hoja del Excel
            df = xl.parse(sheet_name)

            # Reemplaza los valores NaN por un espacio vacío
            df.replace(np.nan, '', inplace=True)

            # Extrae la primera fila como encabezados de las columnas
            headers = list(df.columns.values)

            # Escribe los encabezados en el archivo de texto
            with open(os.path.join(text_files_directory, sheet_name), 'w') as f:
                f.write(','.join(headers) + '\n')

            # Escribe los datos en el archivo de texto
            with open(os.path.join(text_files_directory, sheet_name), 'a') as f:
                for index, row in df.iterrows():
                    f.write(','.join([str(x) if str(x) != 'nan' else '' for x in row.tolist()]) + '\n')

        self.status_label.config(text="La conversión se completó exitosamente.")

root = tk.Tk()
app = ExcelToTextConverter(root)
root.mainloop()