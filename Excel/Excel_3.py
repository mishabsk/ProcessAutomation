import pandas as pd
import numpy as np

df1=pd.read_csv("Excel1.csv", index_col="id")
df2=pd.read_csv("Excel2.csv", index_col="id")
df3=pd.read_csv("Excel3.csv", index_col="id")

df_master=pd.concat([df1, df2, df3])

pivot=pd.pivot_table(df_master, index=['Country', 'Size'], values=['qty', 'price'])

-------------------------------------------------------------------------------------------------------------------

import os
import pandas as pd

excel_data=r'C:\Users\abhasker1\Downloads\EmilyTeohProject\ExcelData_Important'

def fn(excel_data, nan=" "):
    all_sheets_data=[]
    for file in os.listdir(excel_data):
        if file.endswith(".xlsx"):
            all_sheets=pd.read_excel(os.path.join(excel_data,file), sheet_name=None)
            for sheet_name, df in all_sheets.items():
                df.fillna(nan, inplace=True)
                all_sheets_data.append(df)
                print(f"{file} with {sheet_name} has been uploaded")
                print(df.head())
    
    combined_df=pd.concat(all_sheets_data, ignore_index=True)
    
    return combined_df


fn(excel_data)
