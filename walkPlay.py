import os
import sys
from lxml import etree
import shutil

from pathlib import Path

def walkFiles(inDir):


##/._*/ and delete veto files options in our smb.conf to prevent creation of such files. Instead we leave .DS_STORE
    macRes = ('._', '.DS_Store')
    xmlExt = ('ditamap', 'dita', 'xml')
    
##    for subdir, dirs, files in os.walk(inDir):
##        for filename in files:
##
##            ext = Path(filename).suffix.lower()
##            
##            filepath = subdir + os.sep + filename
##            if not filename.startswith(macRes):
##                if filepath.endswith(xmlExt):
##                    docinfo(inDir, filename, filepath, ext)

##    for subdir, dirs, files in os.walk(inDir):
##        for filename in files:
##            filepath = subdir + os.sep + filename
##            print('Subdirs and filepath')
##            print(filepath)
##            print()
##            print('----')
##    for root, dirs, files in os.walk(inDir):
##       for name in files:
##           print('Join root, name')
##           print(os.path.join(root, name))
##           print()
##           print('----')
    
##    for dirname, dirnames, filenames in os.walk(inDir):
##       for filename in filenames:
##           print('Join dirname, filename')
##           print(os.path.join(dirname, filename))
##           print('----')
##           print()

    for dirpath, dirnames, filenames in os.walk(inDir):
       for dirname in dirnames:
           print('----------------------------------------')
           print('dirname: ' + dirname)
           for filename in filenames:
               print('      dirpath:   ' + dirpath)
               print('     dirnames:   ' + str(dirnames))
               print('    filenames:   ' + str(filenames))
               print('    filename:   ' + str(filename))
               print('')


#---------------------------------------------------------------------

inDir = r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\walkTestShort'
walkFiles(inDir)

