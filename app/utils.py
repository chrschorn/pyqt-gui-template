import os
import sys


def resource_path(relative=''):
    root = getattr(sys, '_MEIPASS', os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    return os.path.join(root, 'app', 'data', relative)
