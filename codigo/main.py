import sys
import os

# Este bloque de código es para manejar el problema del _MEIPASS
if hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)

import tkinter as tk
import pandas as pd
import numpy as np

class InterfazPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Conversor")
        
        self.label_decision = tk.Label(self, text="Que tipo de conversion quieres utilizar: ")
        # Crear botón1 para ejecutar XlsxToGtfs.py
        self.boton1 = tk.Button(self, text="Xlsx -> Gtfs", command=self.ejecutar_doc1)
        # Crear botón2 para ejecutar GtfsToXlsx.py
        self.boton2 = tk.Button(self, text="Gtfs ->Xlsx", command=self.ejecutar_doc2)
        

        self.label_decision.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.boton1.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.boton2.grid(row=2,column=0, padx=10, pady=10, sticky="nsew")
        

    def ejecutar_doc1(self):
        script_path = os.path.join(os.getcwd(), 'XlsxToGtfs.py')
        os.system(f'python "{script_path}"')

    def ejecutar_doc2(self):
        script_path = os.path.join(os.getcwd(), 'GtfsToXlsx.py')
        os.system(f'python "{script_path}"')

if __name__ == '__main__':
    app = InterfazPrincipal()
    app.mainloop()