import os
import openpyxl 
from openpyxl.drawing.image import Image
from PIL import Image
from openpyxl.styles import Alignment

def inserting():
    folder_path = "barcode128_result/automate" # Ganti dengan path ke folder yang ingin diambil daftar filenya

    file_names = os.listdir(folder_path)
    file_names.remove('excel')
    
    try:
        num_files = len(file_names)
    except TypeError:
        return

    # Membuat objek workbook dan worksheet baru
    wb = openpyxl.Workbook()
    ws = wb.active

    # Menempatkan nama file ke dalam kolom B
    for i in range(num_files):
        ws.cell(row=i+2, column=2, value=file_names[i].replace(".jpg", ""))

    print("")

    # Menempatkan gambar ke dalam kolom C
    for i in range(num_files):
        
        print(f"[+] Saved {folder_path}/{file_names[i]}")
        img_ori = Image.open(f"{folder_path}/{file_names[i]}")
        img_ori.resize((20, 20))
        img_ori.save(f"{folder_path}/{file_names[i]}")

        img_file = Image.open(f"{folder_path}/{file_names[i]}")
        img = openpyxl.drawing.image.Image(img_file)
        img.width = 110
        img.height = 30

        ws.column_dimensions['B'].width = 35
        ws.column_dimensions['C'].width = 35
        ws.row_dimensions[i+2].height = 30
        ws.add_image(img, 'C{}'.format(i+2))    

    # simpan workbook ke dalam file
    wb.save('barcode128_result/automate/excel/result_barcode.xlsx')

    return