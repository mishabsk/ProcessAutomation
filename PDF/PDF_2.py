import tabula
# Read a PDF File
df = tabula.read_pdf(r"--", pages='all')[0]
# convert PDF into CSV
tabula.convert_into(r"-----", "{destination_csv}COA.csv", output_format="csv", pages='all')
print(df)
