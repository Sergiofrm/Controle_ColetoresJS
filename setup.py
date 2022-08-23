import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["PyQt5"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Ferramenta- Solutions-CD Bahia",
    version="1.0",
    description="Controle de Coletores - JS",
    options={"build_exe": build_exe_options},
    executables=[Executable("run.py", base=base)]
)
