# PyQt GUI Template

This template comes with multiple desirable features for setting up a Python Qt-based GUI:

* GUI / app separation for GUI-less usage
* One-file executable build script to deliver your GUI 
* File access abstraction to access arbitrary data file in both development use and "One-file executable" delivery
* Qt error message redirection to console (avoiding a common pitfall when using Qt with Python)
* A progress bar that keeps the GUI responsive while doing e.g. a long calculation (another common Qt Python issue)

## Usage

Start the app with `python run.py` or as a module: `python -m app`.

## Setup

* The base GUI only depends on PyQt6: `pip install pyqt6`
* To produce a standalone .exe file, also install pyinstaller (`pip install pyinstaller`) and run `tools\make_exe.bat`. 
* To interactively edit the GUI, you can use Qt designer: `designer.exe app\ui\app.ui`. All changes made to ui files have to be converted with the provided `tools\ui2py.bat` script. To obtain the designer, there are multiple options:
  * Install [Qt](https://doc.qt.io/)
  * If you are using [conda](https://docs.conda.io/en/latest/) (recommended anyways), a much easier way is to `conda install qt`
  * Use pyqt6-tools via `pip install pyqt6-tools` and run `pyqt6-tools designer`, although I found it to be less reliable than fully installing Qt, e.g. via conda (see above)
