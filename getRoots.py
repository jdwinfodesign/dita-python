import os
import sys
from lxml import etree
import shutil

from pathlib import Path

def walkFiles(inDir):

    macRes = ('._', '.DS_Store')
    xmlExt = ('ditamap', 'dita', 'xml')
    
    for subdir, dirs, files in os.walk(inDir):
        for filename in files:

            ext = Path(filename).suffix.lower()
            
            filepath = subdir + os.sep + filename
            if not filename.startswith(macRes):
                if filepath.endswith(xmlExt):
                    docinfo(inDir, filename, filepath, ext)


# PRINT ROOT ELEMENT NAME

def docinfo(inDir, filename, filepath, ext):

    parser = etree.XMLParser(strip_cdata=False)
    tree = etree.parse(filepath, parser)
    docinfo = tree.docinfo
    
    print(docinfo.root_name + ': ')
    print(filepath)
    print(ext)
    print()

#---------------------------------------------------------------------

inDir = r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\walkTest'
walkFiles(inDir)

