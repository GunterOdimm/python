import os
import sys
import matplotlib as mpl
from matplotlib import font_manager

font_manager._rebuild()

if sys.platform == 'win32':
    font_list = font_manager.findSystemFonts()

    font_list.sort()

    for file_path in font_list:
        fp = font_manager.FontProperties(fname=file_path)

        font_name = fp.get_name()

        print("%s >> %s" % (file_path,font_name))