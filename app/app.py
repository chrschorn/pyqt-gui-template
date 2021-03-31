import time

from .utils import resource_path


class Application(object):
    def __init__(self):
        self.file_path = resource_path('example.txt')

    def calculation(self, sleep):
        print("Start")
        with open(self.file_path) as file:
            text = file.read()
        time.sleep(sleep)
        print(text)
        print("End")
        return text
