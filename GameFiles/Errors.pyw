"""Module full of general errors for the game"""


def __initError__(self, msg="{def}"):
        expression = "Error: "
        self.expression = expression
        if msg == "{def}":
            self.message = "Unspecified Error"
        else:
            self.message = msg
        print(expression + self.message)
            
class Error(Exception):
    def __init__(self, msg="{def}"):
        __initError__(Error, msg)
        

class SaveError(Error):
    def __init__(self, msg="{def}"):
        __initError__(Error, msg)
        
    
class GameError(Error):
    def __init__(self, msg="{def}"):
        __initError__(Error, msg)
    
class GUIError(Error):
    def __init__(self, msg="{def}"):
        if msg is '{def}':
            msg = 'Unspecified Save Error'
        __initError__(Error, msg)
    
class SaveValueError(SaveError):
    def __init__(self, msg='{def}'):
        __initError__(Error, msg)