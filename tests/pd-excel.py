import pandas as pd
import openpyxl

#Stealing code from here: https://pythonbasics.org/write-excel/
df = pd.DataFrame([[11, 21, 31], [12, 22, 32], [31, 32, 33]],
                  index=['one', 'two', 'three'], columns=['a', 'b', 'c'])

path = r'E:\code\python\tests\pandas-to-excel\product-of-pandas.xlsx'

#Specify path and file name, and name of the sheet
#Note that the to_excel method overwrites the data in the excel sheet, so keep in mindz
#To write multiple sheets, use Excelwriter (look on website or pandas docs)
df.to_excel(path, sheet_name='new_sheet')


