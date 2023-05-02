import sys
import os
from cx_Freeze import setup, Executable

# Obtener la ruta del directorio raíz del proyecto
root_dir = os.path.dirname(os.path.abspath(__file__))

# Incluye los archivos necesarios en el ejecutable
includefiles = ['text_files/']

# Opciones para el ejecutable
build_exe_options = {
    'packages': ['os', 'pandas', 'numpy'],
    'include_files': ['Informacion.xlsx','icono/icono.ico'],
    'include_msvcr': True,
    'build_exe': './dist', # Ruta donde se creará el ejecutable
}

# Configuración del ejecutable
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('main.py', base=base, target_name='ExcelToTextConverter')
]

# Configuración del setup
setup(name="mi_app",
      version="1.0",
      description='Convierte un archivo Excel a archivos de texto',
      options={"build_exe": build_exe_options},
      executables=[Executable("main.py", base=base, target_name="XlsxToGtfs.exe",icon='icono/icono.ico')])