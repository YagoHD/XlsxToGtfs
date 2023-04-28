import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    'packages': ['os', 'pandas', 'numpy'],
    'include_files': ['Informacion.xlsx','icono/icono.ico'],
    'include_msvcr': True,
    'build_exe': './dist', # Ruta donde se creará el ejecutable
    'excludes': ['tkinter']
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="mi_app",
      version="1.0",
      description="Descripción de mi app",
      options={"build_exe": build_exe_options},
      executables=[Executable("main.py", base=base, target_name="XlsxToGtfs.exe",icon='icono/icono.ico')])