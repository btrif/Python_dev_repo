"""
XFL-CRC v0.03 2008-02-06 Philippe Lagadec

To store a file list in XML, with CRC32 hashes.
(this is an example to show how to extend xfl features using callbacks)

usage: xfl-crc.py <root path> <XML file>

Project website: http://www.decalage.info/python/xfl

License: CeCILL v2, open-source (GPL compatible)
         see http://www.cecill.info/licences/Licence_CeCILL_V2-en.html
"""

#------------------------------------------------------------------------------
# CHANGELOG
# 2007-08-15 v0.01 PL: - 1st version
# 2007-08-19 v0.02 PL: - fixed negative CRC32 results
#                      - buffered reading is optional
#                      - added compare feature
# 2008-02-06 v0.03 PL: - first public release

#------------------------------------------------------------------------------

#--- IMPORTS ------------------------------------------------------------------

import xfl, sys, binascii

#--- CONSTANTS ----------------------------------------------------------------

# if USE_BUFFER is True, file will be read using a buffer
# (slower, uses less RAM, can handle abitrary long files)
USE_BUFFER = True
# buffer size for CRC32 computing (1MB = 2**20 bytes)
BUFFER_SIZE = 2 ** 20

# XML attribute for CRC32 hashes
ATTR_CRC = "CRC32"

#--- FUNCTIONS ----------------------------------------------------------------

def compare_files_crc32 (et1, et2):
    """
    to compare two files or dirs, with CRC32.
    returns True if files/dirs information are identical,
    False otherwise.
    (date/time are not compared)
    """
    if et1.tag != et2.tag:
        return False
    if et1.tag == xfl.TAG_DIR:
        if et1.get(xfl.ATTR_NAME) != et2.get(xfl.ATTR_NAME):
            return False
        else:
            return True
    elif et1.tag == xfl.TAG_FILE:
        if et1.get(xfl.ATTR_NAME) != et2.get(xfl.ATTR_NAME):
            return False
        if et1.get(xfl.ATTR_SIZE) != et2.get(xfl.ATTR_SIZE):
            return False
        if et1.get(ATTR_CRC) != et2.get(ATTR_CRC):
            return False
        else:
            return True
    else:
        raise TypeError

def compare_DT_crc32 (dirTree1, dirTree2):
    """
    to compare two DirTrees, and report which files have changed.
    returns a tuple of 4 lists of paths: same files, different files,
    files only in dt1, files only in dt2.
    """
    same = []
    different = []
    only1 = []
    only2 = []
    dirTree1.pathdict()
    dirTree2.pathdict()
    paths1 = dirTree1.dict.keys()
    paths2 = dirTree2.dict.keys()
    for p in paths1:
        if p in paths2:
            # path is in the 2 DT, we have to compare file info
            f1 = dirTree1.dict[p]
            f2 = dirTree2.dict[p]
            if compare_files_crc32(f1, f2):
                # files/dirs are the same
                same.append(p)
            else:
                different.append(p)
            paths2.remove(p)
        else:
            only1.append(p)
    # now paths2 should contain only files and dirs that weren't in paths1
    only2 = paths2
    return same, different, only1, only2

def crc32_file(filepath):
    """
    computes CRC32 hash of a file.
    """
    f = file(filepath, 'rb')
    if USE_BUFFER:
        # file is read in a buffer to save RAM
        data = f.read(BUFFER_SIZE)
        crc = binascii.crc32(data)
        data = f.read(BUFFER_SIZE)
        while data:
            crc = binascii.crc32(data, crc)
            data = f.read(BUFFER_SIZE)
    else:
        # file is read at once in memory
        data = f.read()
        crc = binascii.crc32(data)
    f.close()
    # crc32 can return negative integers when crc>2**31,
    # then we have to shift 2**32 to get positive integers
    if crc < 0:
        crc += 2 ** 32
    return crc

def callback_file_crc32 (filepath, element):
    """
    XFL callback function to add CRC32 attribute to the file element.
    (see XFL module)
    """
    crc = crc32_file(filepath)
    element.set(ATTR_CRC, "%X" % crc)
    print " - %s: %X" % (filepath, crc)

try:
    rootpath = sys.argv[1]
    xmlfile = sys.argv[2]
except:
    sys.exit(__doc__)

# TODO: use isdir instead of file ext
if rootpath.endswith('.xml'):
    d1 = xfl.DirTree()
    d1.read_file(rootpath)
    d2 = xfl.DirTree()
    d2.read_file(xmlfile)
    same, different, only1, only2 = compare_DT_crc32(d1, d2)
# #    print "\nSAME:"
# #    for f in sorted(same):
# #        print "  "+f
    print "\nDIFFERENT:"
    # TODO: fix encoding problems between Mac and PC
    for f in sorted(different):
        print "  " + f.encode('latin_1')
    print "\nNEW:"
    for f in sorted(only1):
        print "  " + f.encode('latin_1')
    print "\nDELETED:"
    for f in sorted(only2):
        print "  " + f.encode('latin_1')
else:
    d = xfl.DirTree()
    d.read_disk(rootpath, xfl.callback_dir_print, callback_file_crc32)
    d.write_file(xmlfile)




