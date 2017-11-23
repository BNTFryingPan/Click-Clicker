## ----------- Imports -------------
try:
    import GUI
    import Save
    import Errors
    import GameManager
except ImportError: # if you run this file directly, the above works. If you run the actual launcher, the modules are at GameFiles.<moduleName>
    import GameFiles.GUI as GUI
    import GameFiles.Save as Save
    import GameFiles.Errors as Errors
    import GameFiles.GameManager as GameManager

import threading
import time
import sys
import os

def cls():
    os.system('cls')

# lib
# Empty


class consoleInput:
    def mainLoop():
        loop = True
        print("WARNING: The console may be very buggy. These arent very easy in Python :/")
        print("NOTE: This console will sometimes show info about game events.")
        #print("Console too buggy.")
        ##while loop == True:
            ##input()
            ##print("None")
        while loop == True:
            consoleIn = input("Console >>> ")
            consoleInput.consoleInputFunc(consoleIn)
            time.sleep(0.5)
            continue
        print("Loop ended")
        return

    def consoleInputFunc(consoleIn):
        '''Used to execute console code. Outside programs, use '''
        try:
            rcIn = str(consoleIn)
            cLn = rcIn.split(";")
            for action in cLn:

                cIn = action
                if cIn.startswith("raise"):
                    print("You cannont raise errors from the console.")
                elif cIn.startswith("consoleInput."):
                    print("You arent allowed to do that.")
                elif cIn.startswith('exit()') or cIn.startswith('quit()'):
                    print('You arent allowed to do that')
                else:
                    try:
                        exec(consoleIn)
                        return
                    except Exception as err:
                        exc_type, exc_value, exc_traceback = sys.exc_info()
                        import traceback
                        print("\nAn error occured in console input:\n\nTraceback (most recent call last) (first call is exec()):")
                        #print(traceback.extract_tb(exc_traceback))
                        for level in traceback.extract_tb(exc_traceback):
                            print(''.join('  File "{}", line {}, in {}\n    {}'.format(*level)))
                        print('{}: {}'.format(exc_type.__name__, exc_value))
                        print("\n")
                        ## \/ fixed somehow. idrk \/
                        #print("Press enter to continue... TODO // fix this thingy")
                        return
        except Exception as err:
            print("Error:" + err)
            return
        return

    def simConsIn(consoleIn):
        """Made for external programs to simulate a console input. outside programs should use this, and not consoleInputFunc()"""
        consoleInput.consoleInputFunc(consoleIn)
        return



def runGame():
    print('Starting Game...')
    os.system('title Click Clicker Console') #(imported)')
    gameThread = threading.Thread(target = game, name = 'Game Thread')
    gameThread.start()
    

def game():
    # Creates threads
    guiT = threading.Thread(target = GUI.startGui, name = "GUI Loader (RunGame.guiT)", kwargs = {"closeOnExit": True})
    consoleT = threading.Thread(target = consoleInput.mainLoop, name = "Console (RunGame.consoleT)")
    mainLoopT = threading.Thread(target = GameManager.MainLoopsManager.mainLoop, name = "Main Game Manager Loop (RunGame.mainLoopT)")
    # Starts threads
    guiT.start()
    mainLoopT.start()
    #consoleT.start()


if __name__ == "__main__":
    #print("Running game...")
    #os.system('title Click Clicker Console (main)')
    runGame()
else:
    print("Imported RunGame\nDo <RunGame>.runGame() to start the game.")
    #runGame()