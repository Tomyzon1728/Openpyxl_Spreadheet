# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 16:35:41 2019

@author: Ajayi Raymond T
"""

from openpyxl import Workbook
workbook = Workbook()
sheet = workbook.active
sheet['A1'] = 'hello'
sheet['B1'] = 'world'
workbook.save(filename ='my first openpyxl.xlsx')