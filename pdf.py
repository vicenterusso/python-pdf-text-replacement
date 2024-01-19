import fitz  # PyMuPDF

def replace_text_in_pdf(input_pdf_path, output_pdf_path, replacements):
    # Open the PDF
    document = fitz.open(input_pdf_path)

    # Iterate through each page
    for page in document:
        for placeholder, replacement in replacements.items():
            # Search for the placeholder text
            text_instances = page.search_for(placeholder)

            # Directly overwrite the existing text
            for inst in text_instances:
                # Clear the area of the placeholder text
                page.add_redact_annot(inst)
                page.apply_redactions()

                # Adjust font size and name as needed
                # Insert text at the top-left corner of the cleared area
                page.insert_text((inst.x0, inst.y0), replacement, fontsize=12, fontname='helv', color=(0, 0, 0))

    # Save the modified PDF
    document.save(output_pdf_path)
    document.close()

# Define the path for your PDF file and replacements
input_pdf_path = 'original.pdf'
output_pdf_path = 'output.pdf'
replacements = {
    '{{title}}': 'Your New Title',
    '{{summary}}': 'Your New Summary'
}

replace_text_in_pdf(input_pdf_path, output_pdf_path, replacements)
