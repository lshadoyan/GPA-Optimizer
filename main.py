import os
import sys

import pandas as pd
import tabula

file_path = r"C:\Users\Lucas\Desktop\PDF-Extract\Pathways Course Guide by Alpha.pdf"

#pages = tabula.read_pdf(file_path, stream=True, pages="all")
#page_num = len(pages)

#df = tabula.read_pdf(file_path, pages="all", lattice=True, multiple_tables=True)
#for page in range(page_num):
#    tables[page].to_excel('test.xlsx', index=False)
#table = table.concat(tables) 
#df[0].to_excel('test.xlsx', index=False)
df = tabula.convert_into(file_path, "test.csv", output_format='csv', lattice=True, pages="all")

