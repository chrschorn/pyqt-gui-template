import argparse
import sys
import traceback

from PyQt5.QtWidgets import QApplication

from .gui import MainWindow


def new_excepthook(type, value, tb):
    # by default, Qt does not seem to output any errors, this prevents that
    traceback.print_exception(type, value, tb)


sys.excepthook = new_excepthook


def main():
    parser = argparse.ArgumentParser()
    # parser.add_argument(...)
    known_args = parser.parse_known_args()[0]

    qapp = QApplication(sys.argv)
    gui = MainWindow(**vars(known_args))
    gui.show()
    sys.exit(qapp.exec_())


if __name__ == '__main__':
    main()
