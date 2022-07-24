import os
import sys

import pandas
import tabula
import PyPDF2 

file_path = r"C:\Users\Lucas\Desktop\PDF-Extract\Pathways Course Guide by Alpha.pdf"

pages = tabula.read_pdf(file_path, stream=True, pages="all")
page_num = len(pages)

tables = tabula.read_pdf(file_path, pages="all",multiple_tables=True)
#for page in range(page_num):
#    tables[page].to_excel('test.xlsx', index=False)
table = table.concat(tables) 
table.to_excel('test.xlsx', index=False)