import tkinter as tk
import os

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
        os.system('python codigo/XlsxToGtfs.py')

    def ejecutar_doc2(self):
        os.system('python codigo/GtfsToXlsx.py')


if __name__ == '__main__':
    app = InterfazPrincipal()
    app.mainloop()