import fitz
import pandas as pd

doc = fitz.open(r'C://////')

# Iterate through each page in the document
for page_num, page in enumerate(doc):
    tabs = page.find_tables()   # Find tables in the page
    page=page.get_text("text") #get "text" can be replaced with "xml" , "words", "json"

print(tabs)
