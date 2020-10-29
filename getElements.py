import os
import sys
from lxml import etree
import shutil
import glob

from pathlib import Path

def walkFiles(inDir):
    macRes = ('._', '.DS_Store')
    xmlExt = ('ditamap', 'dita', 'xml')
# TRY PATHLIB AND GLOB SOME TIME to replace os.walk() here
    for subdir, dirs, files in os.walk(inDir):
        for filename in files:
            filepath = subdir + os.sep + filename
            if not filename.startswith(macRes):
                if filepath.endswith(xmlExt):
                    print(filepath)
                    listElements(inDir, filename, filepath)


def listElements(inDir, filename, filepath):
    parser = etree.XMLParser(strip_cdata=False)
    tree = etree.parse(filepath, parser)
    docinfo = tree.docinfo
    root = tree.getroot()
##    print('filename: ' + filename)
##    print(tree.docinfo.root_name)
##    print(root.tag)
    for element in root.iter():
        print(element.tag)
    
##    print(etree.tostring(tree, pretty_print=True, encoding='unicode'))
    


#---------------------------------------------------------------------

inDir = r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\walkTestShort\A\AA\AAA'
walkFiles(inDir)

