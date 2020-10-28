import os
import sys
from lxml import etree
import shutil
import glob
from pathlib import Path


##/._*/ and delete veto files options in our smb.conf to prevent creation of such files. Instead we leave .DS_STORE
macRes = ('._', '.DS_Store')
xmlExt = ('ditamap', 'dita', 'xml')

## using pathlib

def listSubs(inDir):
    p = Path(inDir)
    # adjust the path here for how deep to go
    # '*' lists child folders only
    for a in p.glob('*'):
        if a.is_dir():
            print(a)

#---------------------------------------------------------------------

##inDir = r'C:\Users\jdwin\Documents\jdwinfodesign\alcuin\src_alcuin_xml-dita_advanced'
inDir = r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\walkTest'
listSubs(inDir)

