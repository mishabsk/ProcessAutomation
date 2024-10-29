import fitz  # PyMuPDF
import pandas as pd
from docx import Document

# Function to extract headings and text
def extract_headings_and_text(pdf_path):
    # Open the PDF
    doc = fitz.open(pdf_path)
    
    data = []  # List to store heading and corresponding text
    
    for i in range(len(doc)):
        page = doc[i]
        blocks = page.get_text("dict")['blocks']  # Extract page content as blocks
        tabs=page.find_tables()
        text=page.get_text()
        if tabs:
            for table in tabs:
                extracted_table=table.extract()
                #print(extracted_table)
       
        
        
        current_heading = None
        current_text = []
        
        for block in blocks:
            if 'lines' not in block:
                continue
            
            for line in block['lines']:
                for span in line['spans']:
                    font_size = span['size']
                    text = span['text'].strip()
                    print(text)
                    
                    # Simple rule: consider text as heading if font size > 12 (you can adjust this)
                    if font_size > 12:
                        # If there is an existing heading, save it with its content
                        if current_heading and current_text:
                            data.append({'Heading': current_heading, 'Text': " ".join(current_text)})
                            current_text = []
                        
                        # Treat the text as a new heading
                        current_heading = text
                    else:
                        # Append the text to the current section under the heading
                        if current_heading:
                            current_text.append(text)
        
        # After looping, add the last heading and text
        if current_heading and current_text:
            data.append({'Heading': current_heading, 'Text': " ".join(current_text)})
    
    # Convert the collected data into a DataFrame
    df = pd.DataFrame(data)
    
    return df

# Function to save the extracted data to a Word document
def save_to_word(df, output_file):
    # Create a new Document
    doc = Document()
    
    # Add a table with two columns
    table = doc.add_table(rows=1, cols=2)
    
    # Set the headings for the table
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Heading'
    hdr_cells[1].text = 'Text'
    
    # Iterate through the DataFrame and add rows to the table
    for index, row in df.iterrows():
        row_cells = table.add_row().cells
        row_cells[0].text = row['Heading']  # Left column for the heading
        row_cells[1].text = row['Text']   
        
    
    doc.save(output_file)

# Example usage
pdf_path = r"-"
output_word_file = "extracted_headings_and_text.docx"

# Extract the data from the PDF
df = extract_headings_and_text(pdf_path)

# Save the data to a Word document
save_to_word(df, output_word_file)

print(f"Data saved to {output_word_file}")
