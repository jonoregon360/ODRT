import os, sys, re, ctypes, RenamingTools

illegalChars = '[#%*:<>?/\\|{}~&^]'

oneDrivePath = raw_input("Please enter path to OneDrive sync folder: ")

if not os.path.isdir(oneDrivePath):
    ctypes.windll.user32.MessageBoxA(0, "No OneDrive sync folder found, program will now terminate", "Error", 0)
    sys.exit()

runScript = RenamingTools.Tools()

for root, dirs, files in os.walk(oneDrivePath, topdown=False):
    for name in files:
        if re.search(illegalChars, name):
            runScript.changeObjName(name, root, illegalChars, oneDrivePath)            
            
    for name in dirs:
        if re.search(illegalChars, name):
            runScript.changeObjName(name, root, illegalChars, oneDrivePath)

msg = 'Files and folders have been renamed, log stored at %s\\OneDrive Rename Log.txt' % oneDrivePath
ctypes.windll.user32.MessageBoxA(0, msg, 'Script Completed', 0)
sys.exit()

