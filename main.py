import pandas as pd
import glob
import openpyxl

filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

for filepath in filepaths:
    # For reading an xlsx file which is an excel file we need read_excel
    df= pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)