# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 17:46:20 2018

@author: nimesh
"""

import glob
from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()

files = glob.glob('C:\\Nimesh\\Suggestive Reads\\Udemy\\*')
for folder in files:
    for f in glob.glob(folder+'\\*.pdf'):
        merger.append(f)
merger.write('C:\\Nimesh\\Suggestive Reads\\Udemy Probability Statistics\\merged.pdf')
    
    