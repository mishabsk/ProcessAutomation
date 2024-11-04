import PyPDF2

def combine_pdfs(pdf_list, output_path):
    # Create a PDF merger object
    pdf_merger = PyPDF2.PdfMerger()

    # Loop through the list of PDFs and append each to the merger object
    for pdf in pdf_list:
        with open(pdf, 'rb') as f:
            pdf_merger.append(f)

    # Write the combined PDF to the specified output path
    with open(output_path, 'wb') as output_pdf:
        pdf_merger.write(output_pdf)

    print(f"PDFs combined successfully into {output_path}")

# Example usage
pdfs_to_combine = ['S1.pdf', 'S2.pdf', 'S3.pdf', 'S4.pdf', 'S5.pdf', 'S6.pdf']  # List your PDF files here
output_file = 'combined_output.pdf'
combine_pdfs(pdfs_to_combine, output_file)
