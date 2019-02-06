# PyQt GUI Template

Start the program with `python run.py` or as a module: `python -m app`.

## Development

The base GUI only depends on PyQt5: `pip install pyqt5`. To produce a standalone .exe file, also install pyinstaller (`pip install pyinstaller`) and run `tools\make_exe.bat`. Reproducible dependencies can be installed with `conda create --file environment.yml`. 

After activating your environment, you can edit the GUI with `designer.exe app\ui\app.ui` if you have Qt installed (`conda install qt`). All changes made to ui files have to be converted with the provided `tools\ui2py.bat` script.
