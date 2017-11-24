"""Creates a blank save file
Will reset if there already is one"""

import configparser as cp
print("imported ConfigParser")

#print("Are you SURE you want to RESET your save file? This CANNOT BE UNDONE!!!!!!!!!")
#print("0 = No, 1 = Yes")



print("Creating 'Config'")
save = cp.ConfigParser()

save['notes'] = {}
save['notes']['a'] = "Sure. You could cheat, and modify this save file. But thats what cheateers do. Cheaters gonna cheat cheat cheat!"

print("Creating Sections...")
save['currency'] = {}
save['makers'] = {}
save['stats'] = {}
save['usersettings'] = {}
print("Created Sections")

print("Creating [currency]")
save['currency']['clicks'] = '0'
save['currency']['keyboards'] = '0'
print("Created [currency]")

print("Creating [makers]")
save['makers']['cursors'] = '0'
save['makers']['mice'] = '0'
save['makers']['autoclickers'] = '0'
save['makers']['superclickers'] = '0'
save['makers']['megaclickers'] = '0'
print("Created [makers]")

print("Creating [stats]")
save['stats']['username'] = '{NONE}'
save['stats']['cps'] = '0'
save['stats']['kps'] = '0'
print("Created [stats]")

print("Creating settings")
#save['usersettings']['cheats'] = 'False'
settings = save['usersettings']
settings['autosave'] = '1'
settings['autosaveinterval'] = '60'

with open('SaveFile.txt','w') as sf:
    save.write(sf)
