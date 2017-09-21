import os, sys, re, ctypes, datetime, RenamingTools

illegalChars = '[#%*:<>?/\\|{}~&^]'

oneDrivePath = raw_input("Please enter path to OneDrive sync folder: ")

if not os.path.isdir(oneDrivePath):
    ctypes.windll.user32.MessageBoxA(0, "No OneDrive sync folder found, program will now terminate", "Error", 0)
    sys.exit()

#Begin logging
logFile = open(oneDrivePath + '\\OneDrive Rename Log.txt', 'a+')
logFile.write('\nScript running at ' + str(datetime.datetime.now()))
logFile.write('\nSync file located at ' + oneDrivePath)

runScript = RenamingTools.Tools()

for root, dirs, files in os.walk(unicode(oneDrivePath, 'utf-8'), topdown=False):
    for name in files:
        if re.search(illegalChars, name):
            runScript.changeObjName(name, root, illegalChars, oneDrivePath, logFile)            
            
    for name in dirs:
        if re.search(illegalChars, name):
            runScript.changeObjName(name, root, illegalChars, oneDrivePath, logFile)

#End logging
logFile.write('\nScript completed at ' + str(datetime.datetime.now()))    
logFile.close()

msg = 'Files and folders have been renamed, log stored at %s\\OneDrive Rename Log.txt' % oneDrivePath
ctypes.windll.user32.MessageBoxA(0, msg, 'Script Completed', 0)
sys.exit()

