import sys
import os
from cx_Freeze import setup, Executable

# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.abspath(__file__))

# Opciones para el ejecutable: paquetes incluidos, archivos incluidos & la ruta donde se creará el freeze
build_exe_options = {
    'packages': ['os', 'pandas', 'numpy'],
    'include_files': ['codigo/icono/icono.ico','codigo/GtfsToXlsx.py','codigo/XlsxToGtfs.py'],
    'include_msvcr': True,
    'build_exe': './dist', 
}
# Añadir los archivos al include_files si se está ejecutando el código con cx_Freeze

# Configuración del ejecutable
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('main.py', base=base, target_name='Convertidor tXlsx & Gtds')
]

# Configuración del setup
setup(name="mi_app",
      version="1.0",
      description='Convierte un archivo Excel a archivos de texto Gtfs y viceversa',
      options={"build_exe": build_exe_options},
      executables=[Executable("codigo/main.py", base=base, target_name="XlsxToGtfs.exe",icon='codigo/icono/icono.ico')])