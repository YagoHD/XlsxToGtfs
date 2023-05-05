import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import numpy as np
import os

class ExcelToGtfs:
    def __init__(self, master):
        self.master = master
        master.title("convertiridor Xlsx -> Gtfs")

        # Crear los widgets
        self.label_seleccion_archivo = tk.Label(master, text="Seleccionar archivo de Excel:")
        self.boton_buscar_archivo = tk.Button(master, text="Buscar archivo", command=self.seleccionar_archivo)
        self.label_seleccion_directorio = tk.Label(master, text="Seleccionar directorio de salida:")
        self.boton_buscar_directorio = tk.Button(master, text="Buscar directorio", command=self.seleccionar_directorio)
        self.label_link_directorio = tk.Label(master, text="", fg="blue")
        self.label_link_archivo = tk.Label(master, text="", fg="blue")
        self.boton_conversion = tk.Button(master, text="Convertirir a archivos de texto", state=tk.DISABLED, command=self.convertir)
        self.label_status = tk.Label(master, text="", fg="green")


        # Colocar los widgets en la ventana
        self.label_seleccion_archivo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.boton_buscar_archivo.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.label_link_archivo.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.label_seleccion_directorio.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        self.boton_buscar_directorio.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
        self.label_link_directorio.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")
        self.boton_conversion.grid(row=6, column=0, padx=10, pady=10, sticky="nsew")
        self.label_status.grid(row=7, column=0, padx=10, pady=10, sticky="nsew")


    def seleccionar_archivo(self):
        # Mostrar un diálogo para seleccionar el archivo de Excel
        self.nombre_archivo = filedialog.askopenfilename()
        self.label_link_archivo.config(text=self.nombre_archivo)
        self.boton_conversion.config(state=tk.NORMAL)
        self.label_status.config(text="")

    def seleccionar_directorio(self):
        # Mostrar un diálogo para seleccionar el directorio de salida
        self.directorio = filedialog.askdirectory()
        self.label_link_directorio.config(text=self.directorio)

    class Convertidor:
        def __init__(self, nombre_archivo, directorio):
            self.nombre_archivo = nombre_archivo
            self.directorio = directorio

    def convertir(self):
        # Lee el archivo Excel
        excel = pd.ExcelFile(self.nombre_archivo)

        # Crea la carpeta "Gtfs" en el directorio seleccionado si no existe
        text_files_directorio = os.path.join(self.directorio, 'Gtfs')
        if not os.path.exists(text_files_directorio):
            os.makedirs(text_files_directorio)

        # Itera sobre todas las hojas del archivo de Excel
        for sheet_name in excel.sheet_names:
            # Lee los datos de la hoja del Excel
            df = pd.read_excel(excel, sheet_name, dtype=str)

            # Escribe los datos en el archivo de texto
            with open(os.path.join(text_files_directorio, sheet_name ), 'w') as f:
                f.write(df.to_csv(index=False, lineterminator='\n'))
    
        self.label_status.config(text="La conversión se completó exitosamente.")

root = tk.Tk()
app = ExcelToGtfs(root)
root.mainloop()