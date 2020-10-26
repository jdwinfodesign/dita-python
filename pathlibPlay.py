import os
import sys
from lxml import etree
import shutil

from pathlib import Path


##/._*/ and delete veto files options in our smb.conf to prevent creation of such files. Instead we leave .DS_STORE
macRes = ('._', '.DS_Store')
xmlExt = ('ditamap', 'dita', 'xml')

## using pathlib

def listSubs(inDir):
##    p = Path(inDir)
##    print([x for x in p.iterdir() if x.is_dir()])
##    print()
    for subdir, dirs, files in os.walk(inDir):
        print('subdir: ' + str(subdir))
        print('...')

#---------------------------------------------------------------------

##inDir = r'C:\Users\jdwin\Documents\jdwinfodesign\alcuin\src_alcuin_xml-dita_advanced'
inDir = r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\walkTest'
listSubs(inDir)

