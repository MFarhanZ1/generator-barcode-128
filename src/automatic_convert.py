import mysql.connector
import backend.text_to_barcode128
import os

def start_auto_convert():

    os.system("cls")

    get_dbs_name = input("[Input] Masukin Nama Databasenya : ")
    get_table_name = input("\n[Input] Masukin Nama Tabelnya : ")    

    # Mengecek apakah nama database dan nama tabelnya benar
    try:

        # Membuat koneksi ke database MySQL
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database=get_dbs_name
        )

    except mysql.connector.errors.ProgrammingError:
        input("\nERROR 404 - Periksa kembali nama database/nama table anda! [teken 'Enter' buat mengisi ulang!]")
        start_auto_convert()

    print("\n[+] Proses sedang berjalan...")

    # Membuat cursor
    cursor = cnx.cursor()

    # Melakukan query pada tabel 'nama_tabel'
    query = f"SELECT * FROM {get_table_name}"
    cursor.execute(query)

    # Mengambil semua hasil query
    results = cursor.fetchall()

    # Menampilkan hasil query
    for row in results:

        # Mengambil value kode_barang pada table mysql
        text_kode_barang = row[0]
        text_nama_barang = row[1]
        
        # Mengecek apakah kode barang berupa string atau tidak
        try:
            int(text_kode_barang)
            continue
        except ValueError:
            # Konversi ke code barcode 128
            backend.text_to_barcode128.convert(text_kode_barang, image_file_name=f"{text_nama_barang} [{text_kode_barang}]", additional_path="barcode128_result/automate/")

    # Menutup koneksi dan cursor
    cursor.close()
    cnx.close()

    input("[Finish] Yeay, teks berhasil diubah menjadi kode barcode128 secara masal!\n\n[Tekan 'Enter' untuk kembali ke-menu utama!]")

    return True
