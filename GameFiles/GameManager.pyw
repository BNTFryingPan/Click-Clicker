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
from tkinter import messagebox

autosave = True
AutosaveInterval = 60



class numbers:
    #Numbers
    clicks = 0
    cursors = 0
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
    multiplier = 1.125
    requiredPerCursor = 15 * multiplier ** ( numbers.cursors )
    requiredPerMouse = 100 * multiplier ** ( numbers.mice )
    requiredPerAuto = 500 * multiplier ** ( numbers.autoclickers )
    requiredPerSuper = 1200 * multiplier ** ( numbers.superclickers )
    requiredPerMega = 4000 * multiplier ** ( numbers.megaclickers )
    
class clickers:
    class cursors:
        def create(amnt=1):
            if amnt == 1:
                required = math.requiredPerCursor
                if numbers.clicks >= required:
                    numbers.clicks = numbers.clicks - required
                    numbers.cursors = numbers.cursors + amnt
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
                else:
                    return
                    
            else:
                for i in range(amnt):
                    required = math.requiredPerMouse
                    if numbers.clicks >= required:
                        numbers.clicks = numbers.clicks - required
                        numbers.mice = numbers.mice + 1
                    else:
                        break
    
    class autoClicker:
        def create(amnt=1):
            if amnt == 1:
                required = math.requiredPerAuto
                if numbers.clicks >= required:
                    numbers.clicks = numbers.clicks - required
                    numbers.autoclickers = numbers.autoclickers + 1
                else:
                    return
                    
            else:
                for i in range(amnt):
                    required = math.requiredPerAuto
                    if numbers.clicks >= required:
                        numbers.clicks = numbers.clicks - required
                        numbers.autoclickers = numbers.autoclickers + 1
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
        autosave = str(save.Get('usersettings','autosave')).lower
        if autosave == 'true' or autosave == '1':
            autosave = True
        else:
            autosave = False
        AutosaveInterval = int(save.Get('usersettings','autosaveinterval'))
        numbers.clicks = float(save.Get('currency', 'clicks'))
        numbers.cursors = int(save.Get('makers', 'cursors'))
        numbers.mice = int(save.Get('makers', 'mice'))
        numbers.autoclickers = int(save.Get('makers', 'autoclickers'))
    except TypeError:
        messagebox.showerror('Unable to load save file. Make sure that your save file isnt corrupted. \nIf your save file is missing or corrupted, run ResetSave.py to create a new save file.')
        return
        
    
    #for i in range(numbers.cursors):
        #tName = 'CursorCreateT #' + str(i)
        #t = threading.Thread(target=None)
        
        
    
    
    
    
def wipeSave():
    global autosave
    doWipe = messagebox.askyesno('Wipe Save','Are you sure you want to wipe your save file? \n this cannot be undone!')
    if doWipe:
        autosave = False
        numbers.clicks = 0
        numbers.cursors = 0
        numbers.mice = 0
        numbers.autoclickers = 0
        numbers.superclickers = 0
        numbers.megaclickers = 0
        math.clicksPerSecond = 0
        math.clicksPerCursor = .25
        math.clicksPerMouse = 1
        math.clicksPerAuto = 15
        math.clicksPerSuper = 50
        math.clicksPerMega = 115
        math.multiplier = 1.125
        math.requiredPerCursor = 15 * math.multiplier ** ( numbers.cursors )
        math.requiredPerMouse = 100 * math.multiplier ** ( numbers.mice )
        math.requiredPerAuto = 500 * math.multiplier ** ( numbers.autoclickers )
        math.requiredPerSuper = 1200 * math.multiplier ** ( numbers.superclickers )
        math.requiredPerMega = 4000 * math.multiplier ** ( numbers.megaclickers )
        saveGame()
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
            math.clicksPerSecond = ( ( numbers.cursors * math.clicksPerCursor ) + ( numbers.mice * math.clicksPerMouse ) + ( numbers.autoclickers * math.clicksPerAuto ) + ( numbers.superclickers * math.clicksPerAuto) + ( numbers.megaclickers * math.clicksPerMega ) )
            math.requiredPerCursor = 15 * math.multiplier ** ( numbers.cursors )
            math.requiredPerMouse = 100 * math.multiplier ** ( numbers.mice )
            math.requiredPerAuto = 500 * math.multiplier ** ( numbers.autoclickers )
            math.requiredPerSuper = 1200 * math.multiplier ** ( numbers.superclickers )
            math.requiredPerMega = 4000 * math.multiplier ** ( numbers.megaclickers )
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
            
            