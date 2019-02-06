from contextlib import contextmanager, ExitStack
from functools import wraps

from PyQt5 import QtCore
from PyQt5.QtCore import QEventLoop, pyqtSlot
from PyQt5.QtWidgets import QProgressDialog, QProgressBar


def long_operation(window_title=" ", label_text="Processing...", is_qt_method=True, disable=True, is_slot=True):
    """
    Shows an infinite progress bar and does the actual work inside a QThread. This keeps the GUI responsive while
    showing that some operation is currently running.

    :param window_title: Window title for the progress bar
    :param label_text: Text for the progress bar
    :param is_qt_method: If set to true, the decorated function must be a QWidget class method. It is then used
                         as the parent of the progress bar window.
    :param disable:  This temporarily disables the parent QWidget while the operation is going on. Only has effect
                     if is_qt_method = True
    :param is_slot: This decorator additionally makes the decorated function a pyqtSlot. If this is not wanted or
                    needed, set to False.
    :return: function decorator
    """
    def wrapper(func):
        if is_slot:
            func = pyqtSlot()(func)

        @wraps(func)
        def decorator(*args, **kwargs):
            qobj = args[0] if is_qt_method else None
            result, exception = None, None
            loop = QEventLoop()
            progress = ProgressWindow(parent=qobj, window_title=window_title, label_text=label_text)

            class Thread(QtCore.QThread):
                def run(self):
                    nonlocal result, exception
                    try:
                        result = func(*args, **kwargs)
                    except Exception as e:
                        exception = e

            task = Thread()
            task.finished.connect(progress.close)
            task.finished.connect(loop.exit)

            with disabled(qobj, enable=disable, except_objs=[progress]):
                progress.show()
                task.start()
                loop.exec()
            
            if exception is not None:
                raise exception
                
            return result
            
        return decorator
    return wrapper


@contextmanager
def disabled(qobj, state=True, enable=True, except_objs=None):
    """
    Temporarily enables/disables the passed QWidget.

    :param qobj: QWidget to disable
    :param state: Target "disable" state (True = temporarily disabled)
    :param enable: Completely disables what this does.
    :param except_objs: These objects are set to the opposite state.
    :return: None
    """
    if not enable:
        yield
        return

    if except_objs is None:
        except_objs = []

    original_state = not qobj.isEnabled()
    qobj.setDisabled(state)
    with ExitStack() as stack:
        for exc in except_objs:
            stack.enter_context(disabled(exc, state=not state))
        yield
    qobj.setDisabled(original_state)


class ProgressWindow(QProgressDialog):
    def __init__(self, parent=None, window_title=None, label_text=None, min_value=0, max_value=0):
        super().__init__(label_text, None, min_value, max_value, parent)
        pbar = QProgressBar(self)
        pbar.setRange(min_value, max_value)
        pbar.setTextVisible(not (min_value == max_value == 0))
        self.setBar(pbar)
        # Also interesting option: QtCore.Qt.FramelessWindowHint
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowTitleHint | QtCore.Qt.CustomizeWindowHint)
        self.setWindowTitle(window_title)
        self.setModal(True)
        self.setFixedSize(self.sizeHint())

    def keyPressEvent(self, *args, **kwargs):
        pass
