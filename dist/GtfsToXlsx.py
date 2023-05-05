import tkinter as tk
from tkinter import ttk  
from tkinter import filedialog
import pandas as pd
import numpy as np
import os
from openpyxl import Workbook

class GtfsToExcel:
    def __init__(self, master):
        self.master = master
        master.title("Convertidor Gtfs -> Xlsx")

        # Crear los widgets
        self.label_seleccion_archivo = tk.Label(master, text="Seleccionar la carpeta con los Gtfs:")
        self.boton_buscar_archivo = tk.Button(master, text="Buscar Carpeta", command=self.seleccionar_archivo)
        self.label_seleccion_directorio = tk.Label(master, text="Seleccionar directorio de salida:")
        self.boton_buscar_directorio = tk.Button(master, text="Buscar directorio", command=self.seleccionar_directorio_salida)
        self.label_link_directorio_salida = tk.Label(master, text="", fg="blue")
        self.label_link_archivo = tk.Label(master, text="", fg="blue")
        self.boton_conversion = tk.Button(master, text="Convertirir a archivos Excel", state=tk.DISABLED, command=self.convertir)
        self.label_status = tk.Label(master, text="", fg="green")

        # Colocar los widgets en la ventana 
        self.label_seleccion_archivo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew") 
        self.boton_buscar_archivo.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.label_link_archivo.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.label_seleccion_directorio.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        self.boton_buscar_directorio.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
        self.label_link_directorio_salida.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")
        self.boton_conversion.grid(row=6, column=0, padx=10, pady=10, sticky="nsew")
        self.label_status.grid(row=7, column=0, padx=10, pady=10, sticky="nsew")


    def seleccionar_archivo(self):
        # Mostrar un diálogo para seleccionar el archivo de Excel
        self.directorio = filedialog.askdirectory()

        # Obtener todos los archivos dentro de la carpeta
        archivos = os.listdir(self.directorio)

        # Filtrar solo los archivos de texto
        archivos_txt = [archivo for archivo in archivos if archivo.endswith('.txt')]

        # Almacenar los nombres de los archivos de texto en el atributo nombres_archivos
        self.nombres_archivos = [os.path.join(self.directorio, archivo) for archivo in archivos_txt]

        self.label_link_archivo.config(text=self.directorio)
        self.boton_conversion.config(state=tk.NORMAL)
        self.label_status.config(text="")
    
    def seleccionar_directorio_salida(self): 
        # Mostrar un diálogo para seleccionar el directorio de salida
        self.directorio_salida = filedialog.askdirectory()
        self.label_link_directorio_salida.config(text=self.directorio_salida)

    def convertir(self):
        # Crea el archivo Excel de salida
        excel_output = pd.ExcelWriter(os.path.join(self.directorio_salida, 'Gtfs.xlsx'), engine='xlsxwriter')

        # Itera sobre todos los archivos de texto seleccionados
        for nombre_archivo in self.nombres_archivos:
            # Lee el archivo de texto
            with open(nombre_archivo, 'r') as f:
                contenido_archivo = f.read()

            # Divide el contenido del archivo de texto en líneas
            lineas = contenido_archivo.split('\n')

            # Obtiene el nombre de la hoja del archivo de Excel (nombre del archivo sin la extensión)
            sheet_name = os.path.basename(nombre_archivo)


            # Crea un DataFrame de Pandas con los datos del archivo de texto
            df = pd.DataFrame([linea.split(',') for linea in lineas])

            # Transpone el DataFrame para que las filas se conviertan en columnas
            #df = df.transpose()

            # Usa la primera fila como encabezados de las columnas
            df.columns = df.iloc[0]
            df = df[1:]

            # Escribe los datos en la hoja correspondiente del archivo de Excel
            df.to_excel(excel_output, sheet_name=sheet_name, index=False)

        # Guarda el archivo de Excel y cierra el writer

        excel_output.close()

        self.label_status.config(text="La conversión se completó exitosamente.")

root = tk.Tk()
app = GtfsToExcel(root)
root.mainloop()