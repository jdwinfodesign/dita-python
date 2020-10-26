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
##        print(subdir)

##    for subdir, dirs, files in os.walk(inDir):
##        print('subdir: ' + str(subdir))
##        print('  dirs: ' + str(dirs))
##        print(' files: ' + str(files))
##        print()

    for subdir, dirs, files in os.walk(inDir):
        print('subdir: ' + str(subdir))
        print()

# Step 4: PRINT ROOT ELEMENT NAME

    def docinfo(inDir, filename, filepath, ext):

        parser = etree.XMLParser(strip_cdata=False)
        tree = etree.parse(filepath, parser)
        docinfo = tree.docinfo
        
        print(docinfo.root_name + ': ')
        print(filepath)
        print(ext)
        print()

#---------------------------------------------------------------------

# Step 0: Prompt user to choose directory containing
#         files to be modified (inDir) and
#         location for output (outDir)

##print(r'Enter the absolute path to the directory containing files to parse. For example:')
##print(r'C:\Users\jdwin\Documents\XMLfiles\src')

##inDir = input()

##inDir = r'C:\Users\jdwin\Documents\jdwinfodesign\alcuin\src_alcuin_xml-dita_advanced'
inDir = r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\walkTest'
walkFiles(inDir)

