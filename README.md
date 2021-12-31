# PyQt GUI Template

This template comes with multiple desirable features for setting up a Python Qt-based GUI:

* GUI / app separation for GUI-less usage
* One-file executable build script to deliver your GUI 
* File access abstraction to access arbitrary data file in both development use and "One-file executable" delivery
* Qt error message redirection to console (avoiding a common pitfall when using Qt with Python)
* A progress bar that keeps the GUI responsive while doing e.g. a long calculation (another common Qt issue)

## Usage

Start the app with `python run.py` or as a module: `python -m app`.

## Setup

* The base GUI only depends on PyQt5: `pip install pyqt5`
* To produce a standalone .exe file, also install pyinstaller (`pip install pyinstaller`) and run `tools\make_exe.bat`. 
* To interactively edit the GUI, have Qt installed and edit the GUI with `designer.exe app\ui\app.ui`. All changes made to ui files have to be converted with the provided `tools\ui2py.bat` script.
  * To easily obtain Qt, Conda is often the easiest way: `conda install qt`
  * Reproducible dependencies can be installed wit `conda create --file environment.yml`)
