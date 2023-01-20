#it will search all drives for folders starting with "a", and then search thru those folders
#for files that start with "a", it will copy these files to another folder on the desktop called
#"texta.txt"

import os
import shutil

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
dest_folder = os.path.join(desktop, "text1a.txt")

#assuming all drives are used
for drive in ['C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', 'L:', 'M:', 'N:', 'O:', 'P:', 'Q:', 'R:', 'S:', 'T:', 'U:', 'V:', 'W:', 'X:', 'Y:', 'Z:']:
    for folderName, subfolders, filenames in os.walk(drive):
        if folderName.startswith("a"):
            for filename in filenames:
                if filename.startswith("a"):
                    src_file = os.path.join(folderName, filename)
                    shutil.copy(src_file, dest_folder)

