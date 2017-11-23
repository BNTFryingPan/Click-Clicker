if __name__ == '__main__':
    import RunGame
    RunGame.runGame()

try:
    import GameManager as GM
except ImportError:
    import GameFiles.GameManager as GM
    
from tkinter import messagebox


class button:
    class ClickB:
        def Click():
            clicks = GM.numbers.clicks
            clicks = clicks + 1
            GM.numbers.clicks = clicks
            #GUI.Click_Clicker.mainWindowLabels.ClicksAmntLabelText = str(clicks)
            #GUI.Click_Clicker.refresh(['ClicksAmntLabel'])
        
        def RightClick():
            print("null")
    
        ## ---------------------- Buying Clickers ---
    class BuyCursorB:
        def Click():
            GM.clickers.cursors.create(1)
            
    class BuyMouseB:
        def Click():
            GM.clickers.mice.create(1)
            
    class BuyAutoB:
        def Click():
            GM.clickers.autoClicker.create(1)
    
    class BuySuperB:
        pass
    
    class BuyMegaB:
        pass
            
            
    class SaveSaveB:
        def Click():
            GM.saveGame()
            # TODO // Implement Saving. Do this after game has working click counter, and buildings menu.
            
        def RightClick():
            print("null")
            
    class SaveExportB:
        def Click():
            saveFileLocation = filedialog.asksaveasfilename(initialdir = "/",title = "Click Clicker <Export Save>",filetypes = (("ClickClickSave files","*.ClickClickerSave, *.CCS, *.ClCiSave, *.ClCiSa"),("All File Types","*.*")))
            # GM.exportSaveFile(exportTo=saveFileLocation)
            print("Exporting Coming Soon")
            #This will be how the game manages exports and imports
        def RightClick():
            print("Null")
            
    class SaveImportB:
        def Click():
            print("Import Coming Soon")
            #This will be how the game manages exports and imports
            
        def RightClick():
            print("null")
            
    class SaveWipeB:
        def Click():
            GM.wipeSave()
            #this is where the game will wipe the save.
            
        def RightClick():
            print("null")
            
    class TMOAWb:
        def Click():
            print('null')
        
        def RightClick():
            print("null")