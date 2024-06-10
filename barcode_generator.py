# Step 1: Generate a new barcode for the given tracking number
# Use the barcode generation library of your choice here
# You might create a function like generate_barcode(tracking_number) that saves the barcode image and returns its path
from io import BytesIO

from barcode import Code128
from barcode.writer import ImageWriter
from pylibdmtx.pylibdmtx import encode, decode
from PIL import Image

def generate_and_save_barcode(tracking_number: str) -> None:
    with open(f"barcodes/{tracking_number}.png", "wb") as f:
        barcode = Code128(str(tracking_number), writer=ImageWriter())
        barcode.default_writer_options['write_text'] = False
        barcode.write(f)
        
def generate_and_save_minicode(tracking_number: str, version: str = "1") -> None:
     # Encode the data matrix input
    #tracking_number = f'PBE{tracking_number}'
    if(version == "1"):
        encoded = encode(f'PBE{tracking_number}'.encode('utf-8'))
    else:
        encoded = encode(f'{tracking_number}'.encode('utf-8'))
    
    # Convert the encoded data to an image using PIL
    img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
    
    # Save the image
    img.save(f'minicode/{tracking_number}.png')
    

# Step 2: Generate a new data matrix with the specified input
# Use a library capable of generating data matrices
# Similarly, you might create a function like generate_data_matrix(data_matrix_input) that saves the data matrix image and returns its path
def generate_and_save_data_matrix(data_matrix_input: str, size: str = "96x96") -> None:
   # data_matrix_input = f"{tracking_number}||087000002562819008|Yusen Logistics (Italy) S.p.A.||1, Yusen-Via Privata Piemonte,|20204|Arluno (Milano)|||1|CHIARA VERZELLA||TRESANDA DEL SALE 6,22|25121|BRESCIA|||PBS|||||+3902902517257||RVE|10"
    
    # Encode the data matrix input
    encoded = encode(data_matrix_input.encode('utf-8'), size=size)
    
    # Convert the encoded data to an image using PIL
    img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
    
    # Save the image
    img.save(f'datamatrix/{data_matrix_input.split("|")[0]}.png')
    
    
#generate_and_save_data_matrix("1UW0GFZ291334")
#generate_and_save_barcode("1UW0GFZ291334")