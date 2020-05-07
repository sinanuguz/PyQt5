# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:58:46 2019

@author: ali
"""
#from PyQt4 import uic

from PyQt5 import uic

with open('HakkindaUI.py', 'w', encoding="utf-8") as fout:
   uic.compileUi('Hakkinda.ui', fout)