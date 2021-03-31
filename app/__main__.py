import argparse
import sys
import traceback

from .app import Application


def new_excepthook(type, value, tb):
    # by default, Qt does not seem to output any errors, this prevents that
    traceback.print_exception(type, value, tb)


sys.excepthook = new_excepthook


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--no-gui', action='store_true')
    args = parser.parse_args()

    app = Application()

    if args.no_gui:
        app.calculation(3)
    else:
        from PyQt5.QtWidgets import QApplication
        from .gui import MainWindow
        qapp = QApplication(sys.argv)
        gui = MainWindow(app)
        gui.show()
        sys.exit(qapp.exec_())


if __name__ == '__main__':
    main()
