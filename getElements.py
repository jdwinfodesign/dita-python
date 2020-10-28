import os
import sys
from lxml import etree
import shutil
import glob

from pathlib import Path

def walkFiles(inDir):


##/._*/ and delete veto files options in our smb.conf to prevent creation of such files. Instead we leave .DS_STORE
    macRes = ('._', '.DS_Store')
    xmlExt = ('ditamap', 'dita', 'xml')
    
    for subdir, dirs, files in os.walk(inDir):
        for filename in files:
            filepath = subdir + os.sep + filename
            if not filename.startswith(macRes):
                if filepath.endswith(xmlExt):
                    listElements(inDir, filename, filepath)
               

def listElements(inDir, filename, filepath):
    parser = etree.XMLParser(strip_cdata=False)
    tree = etree.parse(filepath, parser)
    docinfo = tree.docinfo
    root = tree.getroot()
##    print('filename: ' + filename)
##    print(tree.docinfo.root_name)
    print(root.tag)
    for el in root.iter():
        print('el: ' + el.tag)
    
##    print(etree.tostring(tree, pretty_print=True, encoding='unicode'))
    


#---------------------------------------------------------------------

inDir = r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\walkTestShort\A\AA\AAA'
walkFiles(inDir)

