from PIL import Image, ImageDraw, ImageFont

from address_repository import Address

def process_label(tracking: str, ref_number: str, current_date: str, sender_address: Address, recipient_address: Address) -> str:
    # Paths for the base label, barcode, data matrix, and the output label
    base_label_path = "base_label.png"
    barcode_path = f"barcodes/{tracking}.png"  
    data_matrix_path = f"datamatrix/{tracking}.png"
    minicode_path = f"minicode/{tracking}.png"
    modified_label_path = f"labels/{tracking}.png"
    data_matrix_scale = 0.45
    minicode_scale = 1
    barcode_scale = 1.13
    
    # Load the base label image
    base_label_image = Image.open(base_label_path)

    # Load the data matrix image (assumed to be in PNG format)
    data_matrix_image = Image.open(data_matrix_path)

    # Load the barcode image (assumed to be converted to a compatible format like PNG)
    barcode_image = Image.open(barcode_path)
    
    minicode_image = Image.open(minicode_path)

    # Rotate the barcode image by -90 degrees

    # Define the positions where to paste the barcode and data matrix images
    barcode_position = (70, 480)  # Update these coordinates as necessary
    data_matrix_position = (700, 170)  # Update these coordinates as necessary
    minicode_position = (580, 165)
    
    data_matrix_image = data_matrix_image.resize((int(data_matrix_image.width * data_matrix_scale), int(data_matrix_image.height * data_matrix_scale)))
    barcode_image = barcode_image.resize((int(barcode_image.width * (barcode_scale + 0.05)), int(barcode_image.height * barcode_scale)))
    minicode_image = minicode_image.resize((int(minicode_image.width * minicode_scale), int(minicode_image.height * minicode_scale)))
    
    barcode_image_rotated = barcode_image.rotate(90, expand=True)
    # Paste the rotated barcode image onto the base label image
    # If the rotated barcode image has an alpha channel, use it as a mask for transparency
    if barcode_image_rotated.mode == 'RGBA':
        base_label_image.paste(barcode_image_rotated, barcode_position, barcode_image_rotated.split()[3])
    else:
        base_label_image.paste(barcode_image_rotated, barcode_position)

    # Paste the data matrix image onto the base label image
    # If the data matrix image has an alpha channel, use it as a mask for transparency
    if data_matrix_image.mode == 'RGBA':
        base_label_image.paste(data_matrix_image, data_matrix_position, data_matrix_image.split()[3])
    else:
        base_label_image.paste(data_matrix_image, data_matrix_position)
        
    if minicode_image.mode == 'RGBA':
        base_label_image.paste(minicode_image, minicode_position, minicode_image.split()[3])
    else:
        base_label_image.paste(minicode_image, minicode_position)

    # Add bold text to the image
    draw = ImageDraw.Draw(base_label_image)
    # Use a predefined or a system font. For a predefined font, specify the path to the font file.
    # For example purposes, we'll use a default PIL font for demonstration.
    font = ImageFont.load_default().font_variant(size=18)#ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 18)  # 'arialbd.ttf' is Arial Bold; specify the full path if necessary
    text_position = (338, 770)  # Adjust the position as needed
    draw.text(text_position, tracking, fill="black", font=font)
    
    font = ImageFont.load_default().font_variant(size=18)#ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Unicode.ttf", 18)
    text_position = (485, 330)
    draw.text(text_position, current_date, fill="black", font=font)
    
    text_position = (370, 353)
    draw.text(text_position, ref_number, fill="black", font=font)
    
    text_position = (338, 557)
    draw.text(text_position, str(recipient_address), fill="black", font=font)
    
    text_position = (338, 450)
    draw.text(text_position, str(sender_address), fill="black", font=font)

    # Create a new image with white background
    txt = Image.new('RGB', (200, 25), color=(255, 255, 255))
    d = ImageDraw.Draw(txt)
    font = ImageFont.load_default().font_variant(size=22)#ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Unicode.ttf", 22)
    # Draw text with white fill color
    d.text((0, 0), tracking, fill="black", font=font)

    # Rotate the image
    w = txt.rotate(90, expand=True)
    
    text_position = (295, 730)
    base_label_image.paste(w, text_position)
    
    # Save the modified label image
    base_label_image.save(modified_label_path)

    return modified_label_path

def process_label_v2(tracking: str, ref_number: str, current_date: str, sender_address: Address, recipient_address: Address) -> str:
    # Paths for the base label, barcode, data matrix, and the output label
    base_label_path = "base_label_v2.png"
    barcode_path = f"barcodes/{tracking}.png"  
    data_matrix_path = f"datamatrix/{tracking}.png"
    minicode_path = f"minicode/{tracking}.png"
    modified_label_path = f"labels/{tracking}.png"
    data_matrix_scale = 0.41
    minicode_scale = 1
    barcode_scale = 0.6
    
    # Load the base label image
    base_label_image = Image.open(base_label_path)

    # Load the data matrix image (assumed to be in PNG format)
    data_matrix_image = Image.open(data_matrix_path)

    # Load the barcode image (assumed to be converted to a compatible format like PNG)
    barcode_image = Image.open(barcode_path)
    
    minicode_image = Image.open(minicode_path)

    # Rotate the barcode image by -90 degrees

    # Define the positions where to paste the barcode and data matrix images
    barcode_position = (115, 820)  # Update these coordinates as necessary
    data_matrix_position = (410, 130)  # Update these coordinates as necessary
    minicode_position = (270, 115)
    
    data_matrix_image = data_matrix_image.resize((int(data_matrix_image.width * data_matrix_scale), int(data_matrix_image.height * data_matrix_scale)))
    barcode_image = barcode_image.resize((int(barcode_image.width * (barcode_scale + 0.05)), int(barcode_image.height * barcode_scale)))
    minicode_image = minicode_image.resize((int(minicode_image.width * minicode_scale), int(minicode_image.height * minicode_scale)))
    
   # barcode_image_rotated = barcode_image.rotate(90, expand=True)
    # Paste the rotated barcode image onto the base label image
    # If the rotated barcode image has an alpha channel, use it as a mask for transparency
    if barcode_image.mode == 'RGBA':
        base_label_image.paste(barcode_image, barcode_position, barcode_image.split()[3])
    else:
        base_label_image.paste(barcode_image, barcode_position)

    # Paste the data matrix image onto the base label image
    # If the data matrix image has an alpha channel, use it as a mask for transparency
    if data_matrix_image.mode == 'RGBA':
        base_label_image.paste(data_matrix_image, data_matrix_position, data_matrix_image.split()[3])
    else:
        base_label_image.paste(data_matrix_image, data_matrix_position)
        
    if minicode_image.mode == 'RGBA':
        base_label_image.paste(minicode_image, minicode_position, minicode_image.split()[3])
    else:
        base_label_image.paste(minicode_image, minicode_position)

    # Add bold text to the image
    draw = ImageDraw.Draw(base_label_image)
    # Use a predefined or a system font. For a predefined font, specify the path to the font file.
    # For example purposes, we'll use a default PIL font for demonstration.
    font = ImageFont.load_default().font_variant(size=13)#ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 18)  # 'arialbd.ttf' is Arial Bold; specify the full path if necessary
    text_position = (137, 690)  # Adjust the position as needed
    draw.text(text_position, tracking, fill="black", font=font)

    font = ImageFont.load_default().font_variant(size=10)
    text_position = (215, 935)  # Adjust the position as needed
    draw.text(text_position,tracking, fill="black", font=font)
    
    font = ImageFont.load_default().font_variant(size=15)#ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Unicode.ttf", 18)
    text_position = (133, 310)
    draw.text(text_position, current_date, fill="black", font=font)
    
    text_position = (165, 327)
    draw.text(text_position, ref_number, fill="black", font=font)
    
    # recipient address
    text_position = (137, 485)
    draw.text(text_position, recipient_address.name, fill="black", font=font)

    text_position = (137, 505)
    draw.text(text_position, str(recipient_address.street), fill="black", font=font)

    text_position = (468, 505)
    draw.text(text_position, str(recipient_address.cap), fill="black", font=font)

    text_position = (137, 525)
    draw.text(text_position, str(recipient_address.city), fill="black", font=font)

    text_position = (493, 525)
    draw.text(text_position, str(recipient_address.region), fill="black", font=font)
    

    # sender address
    TEXT_POSITION = (137, 366)
    draw.text(TEXT_POSITION, str(sender_address.name).upper(), fill="black", font=font)

    TEXT_POSITION = (137, 386)
    draw.text(TEXT_POSITION, str(sender_address.street).upper(), fill="black", font=font)

    TEXT_POSITION = (468, 386)
    draw.text(TEXT_POSITION, str(sender_address.cap).upper(), fill="black", font=font)

    TEXT_POSITION = (137, 406)
    draw.text(TEXT_POSITION, str(sender_address.city).upper(), fill="black", font=font)

    TEXT_POSITION = (493, 406)
    draw.text(TEXT_POSITION, str(sender_address.region).upper(), fill="black", font=font)

    base_label_image.save(modified_label_path)

    return modified_label_path

def process_label_v3(tracking: str, ref_number: str, current_date: str, sender_address: Address, recipient_address: Address) -> str:
    # Paths for the base label, barcode, data matrix, and the output label
    base_label_path = "base_label_cronos.png"
    barcode_path = f"barcodes/{tracking}.png"  
    data_matrix_path = f"datamatrix/{tracking}.png"
    minicode_path = f"minicode/{tracking}.png"
    modified_label_path = f"labels/{tracking}.png"
    data_matrix_scale = 0.75
    minicode_scale = 0.8
    barcode_scale = 0.75
    
    # Load the base label image
    base_label_image = Image.open(base_label_path)

    # Load the data matrix image (assumed to be in PNG format)
    data_matrix_image = Image.open(data_matrix_path)

    # Load the barcode image (assumed to be converted to a compatible format like PNG)
    barcode_image = Image.open(barcode_path)
    
    minicode_image = Image.open(minicode_path)

    # Rotate the barcode image by -90 degrees

    # Define the positions where to paste the barcode and data matrix images
    barcode_position = (30, 230)  # Update these coordinates as necessary
    data_matrix_position = (620, 25)  # Update these coordinates as necessary
    minicode_position = (530, 25)
    
    data_matrix_image = data_matrix_image.resize((int(data_matrix_image.width * data_matrix_scale), int(data_matrix_image.height * data_matrix_scale)))
    barcode_image = barcode_image.resize((int(barcode_image.width * (barcode_scale + 0.05)), int(barcode_image.height * barcode_scale)))
    minicode_image = minicode_image.resize((int(minicode_image.width * minicode_scale), int(minicode_image.height * minicode_scale)))
    
    barcode_image_rotated = barcode_image.rotate(90, expand=True)
    # Paste the rotated barcode image onto the base label image
    # If the rotated barcode image has an alpha channel, use it as a mask for transparency
    if barcode_image_rotated.mode == 'RGBA':
        base_label_image.paste(barcode_image_rotated, barcode_position, barcode_image_rotated.split()[3])
    else:
        base_label_image.paste(barcode_image_rotated, barcode_position)

    # Paste the data matrix image onto the base label image
    # If the data matrix image has an alpha channel, use it as a mask for transparency
    if data_matrix_image.mode == 'RGBA':
        base_label_image.paste(data_matrix_image, data_matrix_position, data_matrix_image.split()[3])
    else:
        base_label_image.paste(data_matrix_image, data_matrix_position)
        
    if minicode_image.mode == 'RGBA':
        base_label_image.paste(minicode_image, minicode_position, minicode_image.split()[3])
    else:
        base_label_image.paste(minicode_image, minicode_position)

    # Add bold text to the image
    draw = ImageDraw.Draw(base_label_image)
    # Use a predefined or a system font. For a predefined font, specify the path to the font file.
    # For example purposes, we'll use a default PIL font for demonstration.
    font = ImageFont.load_default().font_variant(size=10)#ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 18)  # 'arialbd.ttf' is Arial Bold; specify the full path if necessary
    text_position = (260, 452)  # Adjust the position as needed
    draw.text(text_position, tracking, fill="black", font=font)
    
    font = ImageFont.load_default().font_variant(size=10)#ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Unicode.ttf", 18)
    text_position = (240, 170)
    draw.text(text_position, current_date, fill="black", font=font)
    
    text_position = (350, 170)
    draw.text(text_position, ref_number, fill="black", font=font)
    
    font = ImageFont.load_default().font_variant(size=12)
    # recipient address
    text_position = (216, 315)
    draw.text(text_position, recipient_address.name, fill="black", font=font)

    text_position = (216, 332)
    draw.text(text_position, str(recipient_address.street), fill="black", font=font)

    text_position = (216, 350)
    draw.text(text_position, str(recipient_address.cap), fill="black", font=font)

    text_position = (256, 350)
    draw.text(text_position, str(recipient_address.city), fill="black", font=font)

    text_position = (365, 350)
    draw.text(text_position, str(recipient_address.region), fill="black", font=font)
    
    # sender address
    TEXT_POSITION = (216, 240)
    draw.text(TEXT_POSITION, str(sender_address.name).upper(), fill="black", font=font)

    TEXT_POSITION = (216, 256)
    draw.text(TEXT_POSITION, str(sender_address.street).upper(), fill="black", font=font)

    TEXT_POSITION = (216, 273)
    draw.text(TEXT_POSITION, str(sender_address.cap).upper(), fill="black", font=font)

    TEXT_POSITION = (256, 273)
    draw.text(TEXT_POSITION, str(sender_address.city).upper(), fill="black", font=font)

    TEXT_POSITION = (320, 273)
    draw.text(TEXT_POSITION, str(sender_address.region).upper(), fill="black", font=font)

        # Create a new image with white background
    txt = Image.new('RGB', (200, 25), color=(255, 255, 255))
    d = ImageDraw.Draw(txt)
    font = ImageFont.load_default().font_variant(size=16)#ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Unicode.ttf", 22)
    # Draw text with white fill color
    d.text((0, 0), tracking, fill="black", font=font)

    # Rotate the image
    w = txt.rotate(90, expand=True)
    
    text_position = (183, 265)
    base_label_image.paste(w, text_position)
    
    # Save the modified label image
    base_label_image.save(modified_label_path)

    return modified_label_path


