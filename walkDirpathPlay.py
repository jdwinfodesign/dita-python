import os
import sys
from lxml import etree
import shutil

from pathlib import Path

def walkFiles(inDir):


##/._*/ and delete veto files options in our smb.conf to prevent creation of such files. Instead we leave .DS_STORE
    macRes = ('._', '.DS_Store')
    xmlExt = ('ditamap', 'dita', 'xml')
    print('running walkFiles(inDir)')
    print()
    print('calling scanDir')
    scanDir(inDir)

def scanDir(inDir):
    with os.scandir(inDir) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_dir():
                print(entry.name)
    
##    for dirpath, dirnames, filenames in os.walk(inDir):
##       for dirname in dirnames:
##           print('----------------------------------------')
##           print('dirname: ' + dirname)
##           print('      dirpath:   ' + dirpath)
##           print('     dirnames:   ' + str(dirnames))
##           print('    filenames:   ' + str(filenames))
##           for filename in filenames:
##               print('    filename:   ' + str(filename))
##           print('')
##           for filename in filenames:
##               print('      dirpath:   ' + dirpath)
##               print('     dirnames:   ' + str(dirnames))
##               print('    filenames:   ' + str(filenames))
##               print('    filename:   ' + str(filename))
##               print('')
    
##    for dirpath, dirnames, filenames in os.walk(inDir):
##        for dirname in dirnames:
##            print('dirname: ' + dirname)
##        print('')

##    for path, directories, files in os.walk(inDir):
##        print('path: ' + str(path))
##        print('directories: ' + str(directories))
##        print('files: ' + str(files))
##        print()
##        print('-----------------------------')



#---------------------------------------------------------------------

inDir = r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\walkTestShort'
print()
walkFiles(inDir)
