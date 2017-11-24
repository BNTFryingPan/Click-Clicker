"""Save file reader and writer"""

import configparser as cp

save = cp.ConfigParser()

save.read("SaveFile.txt")

def Get(section="{ALL}", item="{ALL}"):
    """Gets a value from the save file.
    
    Arguments:
        
        section: the section the item you want to get is in
        item: the item you want to get the value of
    
    Special Inputs:
        
        section = {ALL}: Return the whole save file; item can be ommited.
        item = {ALL}: Returns a whole section
        
    Behaviour:
        
        returns the value from the save file, probably as a string
    """
    try:
        if section == "{ALL}":
            return save
        elif item == '{ALL}':
            section = section.lower()
            return save[section]
        else:
            section = section.lower()
            return save[section][item]
    except KeyError:
        pass
    
def Set(section='{FULLSAVE}', item=None, value=''):
    """Sets a value in the save file. Wouldve been set() but that was already a thing D:
    
    Arguments:
    
        section: The section in the save file you want to set
        item: The item in the save file you want to set
        value: the value of the item you want to set
        
    Behavour:
        
    """
    try:
        value = str(value)
        section = str(section).lower()
        item = str(item).lower()
        #if
        if not item == None:
            save[section][item] = value
        else:
            save[section] = {}
            save[section][item] = value
    except Exception as err:
        print(str(err))
        
def commit():
    with open('SaveFile.txt','w') as saveFile:
        save.write(saveFile)
        
    