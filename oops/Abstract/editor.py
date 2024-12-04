from abc import ABC,abstractmethod

class Editor:

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def debug(self):
        pass

    @abstractmethod
    def execute(self):
        pass

class vscode(Editor):

    def open(self):
        print("vscode can open")

    def write(self):
        print("vscode can write")

    def debug(self):
        print("vscode can debug")

    def execute(self):
        print("vscode can excute")

vscode_instance=vscode()

vscode_instance.open()