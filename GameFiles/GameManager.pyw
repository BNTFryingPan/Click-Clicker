if __name__ == '__main__':
    import RunGame
    RunGame.runGame()

from collections import OrderedDict
try:
    import Save as save
    #import GUI as gui
except ImportError:
    import GameFiles.Save as save
    #import GameFiles.GUI as gui
    
import time
import threading

autosave = True
AutosaveInterval = 60



class numbers:
    #Numbers
    cursors = 0
    clicks = 0
    mice = 0
    autoclickers = 0
    superclickers = 0
    megaclickers = 0
    
class math:
    #Math
    clicksPerSecond = 0
    clicksPerCursor = .25
    clicksPerMouse = 1
    clicksPerAuto = 15
    clicksPerSuper = 50
    clicksPerMega = 115
    requiredPerCursor = 15 + (numbers.cursors * 2)
    requiredPerMouse = 100 + (numbers.mice * 3)
    requiredPerAuto = 500 + (numbers.autoclickers * 4)
    requiredPerSuper = 1200 + (numbers.superclickers * 5)
    requiredPerMega = 4000 + (numbers.megaclickers * 6)
    
class clickers:
    class cursors:
        def create(amnt=1):
            if amnt == 1:
                required = math.requiredPerCursor
                if numbers.clicks >= required:
                    numbers.clicks = numbers.clicks - required
                    numbers.cursors = numbers.cursors + amnt
                    math.clicksPerSecond = math.clicksPerSecond + math.clicksPerCursor
                else:
                    return
                    
            else:
                for i in range(amnt):
                    required = math.requiredPerCursor
                    if numbers.clicks >= required:
                        numbers.clicks = numbers.clicks - required
                        numbers.cursors = numbers.cursors + 1
                    else:
                        break
                        
    class mice:
        def create(amnt=1):
            if amnt == 1:
                required = math.requiredPerMouse
                if numbers.clicks >= required:
                    numbers.clicks = numbers.clicks - required
                    numbers.mice = numbers.mice + 1
                    math.clicksPerSecond = math.clicksPerSecond + math.clicksPerMouse
                else:
                    return
                    
            else:
                for i in range(amnt):
                    required = math.requiredPerMouse
                    if numbers.clicks >= required:
                        numbers.clicks = numbers.clicks - required
                        numbers.mice = numbers.mice + 1
                        math.clicksPerSecond = math.clicksPerSecond + math.clicksPerMouse
                    else:
                        break
    
    class autoClicker:
        def create(amnt=1):
            if amnt == 1:
                required = math.requiredPerAuto
                if numbers.clicks >= required:
                    numbers.clicks = numbers.clicks - required
                    numbers.autoclickers = numbers.autoclickers + 1
                    math.clicksPerSecond = math.clicksPerSecond + math.clicksPerAuto
                else:
                    return
                    
            else:
                for i in range(amnt):
                    required = math.requiredPerAuto
                    if numbers.clicks >= required:
                        numbers.clicks = numbers.clicks - required
                        numbers.autoclickers = numbers.autoclickers + 1
                        math.clicksPerSecond = math.clicksPerSecond + math.clicksPerAuto
                    else:
                        break
                        
                        
                        
def saveGame():
    #print("Saving Game...")
    save.Set('makers', 'cursors', numbers.cursors)
    save.Set('currency', 'clicks', numbers.clicks)
    save.Set('makers', 'mice', numbers.mice)
    save.Set('makers', 'autoclickers', numbers.autoclickers)
    #print('Game Saved! Commiting Save...')
    save.commit()
    #print('Commited Save File! Save Complete!')
    
def loadSave():
    global AutosaveInterval
    global autosave
    #print('Loading Save Game...')
    try:
        autosave = bool(int(save.Get('usersettings','autosave')))
        AutosaveInterval = int(save.Get('usersettings','autosaveinterval'))
        numbers.clicks = float(save.Get('currency', 'clicks'))
    except TypeError:
        messagebox.showerror('Unable to load save file. Make sure that your save file isnt corrupted. \nIf your save file is missing or corrupted, run ResetSave.py to create a new save file.')
    
def wipeSave():
    from tkinter import messagebox
    doWipe = messagebox.askyesno('Wipe Save','Are you sure you want to wipe your save file? \n this cannot be undone!')
    if doWipe:
        try:
            import ResetSave
        except ImportError:
            import GameFiles.ResetSave
        loadSave()
        messagebox.showinfo('Wipe Save','Your save file has been wiped.')
    else:
        messagebox.showinfo('Wipe Save','Your save file will not be wiped.')
            
            
            
            
class MainLoopsManager:
    def mainLoop():
        loadSave()
        clicksGenLoopT = threading.Thread(target = MainLoopsManager.clicksGeneratorLoop, name = 'Clicks Gen Thread (GameManager.MainLoopsManager.mainLoop().clicksGenLoopT)')
        clicksGenLoopT.start()
        autosaveT = threading.Thread(target=MainLoopsManager.autoSaveLoop, name='Autosave Thread (GameManager.MainLoopsManager.mainLoop().autosaveT)')
        autosaveT.start()
        loop = True
        while loop == True:
            math.requiredPerCursor = 15 + (numbers.cursors * 2)
            math.requiredPerMouse = 100 + (numbers.mice * 3)
            math.requiredPerAuto = 500 + (numbers.autoclickers * 4)
            math.requiredPerSuper = 1200 + (numbers.superclickers * 5)
            math.requiredPerMega = 4000 + (numbers.megaclickers * 6)
            time.sleep(0.025)
            
    def clicksGeneratorLoop():
        loop = True
        while loop == True:
            while math.clicksPerSecond > 0:
                numbers.clicks = numbers.clicks + math.clicksPerSecond
                time.sleep(1)
            #print('No CPS; will check again in 5 seconds...')
            #time.sleep(5)
            
    def autoSaveLoop():
        global AutosaveInterval
        global autosave
        loop = True
        while loop == True:
            while autosave == True:
                #print('Autosaving...')
                saveGame()
                time.sleep(AutosaveInterval)
            
            