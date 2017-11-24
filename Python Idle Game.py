import sys
try:
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("Python Idle Game Console and Information")
    
    import os
    def cls():
        os.system("cls")
        
    import GameFiles.RunGame
    import GameFiles.Errors
    
    import GameFiles.Save
    # if Save.get("stats", "username") == "{NONE}":
        # cls()
        # print("""You must choose a name for your journey!
        
# Please Choose a name:""")
        # newUn = input("Name >>> ")
        # Save.set('stats', 'username', newUn)
        # print("Hello! " + newUn + "!")

    import threading
    gameT = threading.Thread(target=GameFiles.RunGame.runGame)
    gameT.start()


except ImportError as err:
    info = sys.exc_info()
    import traceback
    cls()
    print("""
============================== Error Handler ==============================
=                   The game has encountered an error!                    =
=           To try to prevent further errors, the game will close         =
=                     This error was an ImportError                       =
= Please send this printout to the developer at LeotomasMC@outlook.com    =
=============================== Traceback: ================================""")
    try:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        import traceback
        print("Traceback (most recent call last) (first call is exec()):")
        #print(traceback.extract_tb(exc_traceback))
        for level in traceback.extract_tb(exc_traceback):
            print(''.join('  File "{}", line {}, in {}\n    {}'.format(*level)))
        print('{}: {}'.format(exc_type.__name__, exc_value))
    except Exception as err2:
        print("Unable to print exception: " + err2)
    print("\n===========================================================================\n= Please send this to me!                                                 =\n===========================================================================\n")
    #smessagebox.showerror("Title", "An error occured. Please check the log for more info")
except GameFiles.Errors.Error as err:
    info = sys.exc_info()
    import traceback
    cls()
    print("""
============================== Error Handler ==============================
=                   The game has encountered an error!                    =
=           To try to prevent further errors, the game will close         =
=                       This error was a Game Error                       =
= Please send this printout to the developer at LeotomasMC@outlook.com    =
=============================== Traceback: ================================""")
    try:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        import traceback
        print("Traceback (most recent call last) (first call is exec()):")
        #print(traceback.extract_tb(exc_traceback))
        for level in traceback.extract_tb(exc_traceback):
            print(''.join('  File "{}", line {}, in {}\n    {}'.format(*level)))
        print('{}: {}'.format(exc_type.__name__, exc_value))
    except Exception as err2:
        print("Unable to print exception: " + err2)
    print("""
===========================================================================
= System Exc Info: """ + str(info) + """
= Please send this to me!                                                 =
===========================================================================
""")
    #messagebox.showerror("Title", "An error occured. Please check the log for more info")
except Exception as err:
    info = sys.exc_info()
    import traceback
    cls()
    print("""
============================== Error Handler ==============================
=                   The game has encountered an error!                    =
=           To try to prevent further errors, the game will close         =
=                    This error was NOT a Game Error                      =
= Please send this printout to the developer at LeotomasMC@outlook.com    =
=============================== Traceback: ================================""")
    try:
        traceback.print_tb(err)
    except Exception as err2:
        print("Unable to print traceback: " + str(err2))
        print("Original Error: " + str(err))
    print("""
===========================================================================
= System Exc Info: """ + str(info) + """
= Please send this to me!                                                 =
===========================================================================
""")
    #messagebox.showerror("Title", "An error occured. Please check the log for more info")