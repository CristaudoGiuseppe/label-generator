from PIL import Image

def convert_label_to_pdf(tracking):
    png_path = f"labels/{tracking}.png"  # Update this to the path of your PNG label
    pdf_path = f"pdf_labels/{tracking}.pdf" # Update this to where you want the PDF saved
    # Open the PNG image
    image = Image.open(png_path)
    
    # Convert the image to RGB mode if it's not already, as save as PDF might not support all modes
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Save the image as a PDF
    image.save(pdf_path, "PDF", resolution=100.0)

    return pdf_path

# Example usage

#converted_pdf_path = convert_label_to_pdf("1UW0GFZ291334")
#print(f"PNG converted to PDF and saved to: {converted_pdf_path}")
