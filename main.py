from flask import Flask, send_file, request, abort
from functools import wraps
from datetime import datetime
import random, os

from address_repository import Address
from barcode_generator import generate_and_save_barcode, generate_and_save_data_matrix, generate_and_save_minicode

import streamlit as st
from label_converter import convert_label_to_pdf

from process_label import process_label

app = Flask(__name__)

# API_KEY = "dd10a7d2-6c0e-4976-a16e-832f0a725705"

# def require_api_key(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if request.headers.get('X-API-KEY') != API_KEY:
#             abort(401)  # Unauthorized
#         return f(*args, **kwargs)
#     return decorated_function

def create_data_matrix_input(tracking: str, ref_number: str, sender_address: Address, recipient_address: Address) -> str:
    #1UW0GFZ296662||12345|SPRING GDS||VIA BOVISASCA 18|NOVATE MILANESE|(MI)||1|Ivan Catalano||Via Monte 7|35012|Camposampiero|||PBE|||||10
    return f"{tracking}||{ref_number}|{recipient_address.name}||{recipient_address.street}|{recipient_address.cap}|{recipient_address.city}|({recipient_address.region})||1|{sender_address.name}||{sender_address.street}|{sender_address.cap}|{sender_address.city}|({sender_address.region})||||PBE|10"

def generate_random_ref_number() -> str:
    return str(random.randint(100000, 999999))

def get_current_date() -> str:
    # Get the current date
    current_date = datetime.now()
    # Format the date in Italian style (dd/mm/yyyy)
    italian_date_format = current_date.strftime("%d/%m/%Y")
    return italian_date_format


@app.route('/labels/<tracking>', methods=['GET'])
#@require_api_key
def generate_label(tracking):

    #body = request.json
    
    # try:
    #     mittente = body['mittente']
    #     destinatario = body['destinatario']
    # except:
    #     mittente = 1
    #     destinatario = 1
    try:
        mittente = int(request.args.get('mittente', default=0))
        destinatario = int(request.args.get('destinatario', default=1))
    except ValueError:
        # Handle the case where the parameter value cannot be converted to an integer
        mittente = 1
        destinatario = 1
    
    ref_number = generate_random_ref_number()
    
    current_date = get_current_date()
    
    generate_and_save_barcode(tracking)
    
    generate_and_save_minicode(tracking)
    
    data_matrix_input = create_data_matrix_input(
        tracking, 
        ref_number, 
        Address.get_sender_address(mittente), 
        Address.get_recipient_address(destinatario))
    
    generate_and_save_data_matrix(data_matrix_input)
    
    label_path = process_label(
        tracking, 
        ref_number, 
        current_date, 
        Address.get_sender_address(mittente),
        Address.get_recipient_address(destinatario))
    
    pdf_path = convert_label_to_pdf(tracking)
    
    try:
        return send_file(pdf_path, download_name=f"{tracking}.pdf", as_attachment=True)
    except FileNotFoundError:
        return {"error": "Error generating the label"}, 500

if __name__ == '__main__':
    app.run(debug=True)
