import mysql.connector
import backend.text_to_barcode128
import backend.insert_to_excel
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
        
        # mengambil semua nama kolom pada tabel terkait
        colNameFetcherCursor = cnx.cursor()
        query_fetcher_col_name = f"DESC {get_table_name}"
        colNameFetcherCursor.execute(query_fetcher_col_name)

    except mysql.connector.errors.ProgrammingError:
        input("\nERROR 404 - Periksa kembali nama database/nama table anda! [teken 'Enter' buat mengisi ulang!]")
        start_auto_convert()

    # mengubah dalam bentuk list colomn yang diambil
    column_names = [column[0] for column in colNameFetcherCursor.fetchall()]

    # input nama kolom yang isinya mau diubah jadi kode barcode
    get_col_name = input("\n[Input] Masukin nama kolom yang mau lu ubah jadi barcode : ")  

    # mencari indeks keberapa colomn terkait
    while(True):
        try:
            indexKeyChoosen = column_names.index(get_col_name)
            break
        except ValueError:
            get_col_name = input("\nHarap nama kolom sudah sesuai dengan yang ada di database!\n\n[Input] Silahkan input lagi Nama Kolomnya : ")
            continue

    get_custom_nama_file = input("\n[Optional] (Tekan 'Enter' jika ingin skip ini) Masukan kustom nama kolom yang ingin dijadikan nama file : ")

    # jika langsung di tekan enter, akan di skip custom nama file
    if get_custom_nama_file != "":
        # mencari indeks keberapa colomn terkait
        while(True):
            try:            
                indexKeyChoosenNamaFile = column_names.index(get_custom_nama_file)
                break

            except ValueError:
                get_custom_nama_file = input("\nHarap nama kolom sudah sesuai dengan yang ada di database!\n\n[Input] Silahkan input lagi Nama Kolomnya : ")
                continue

    print("\n[+] Proses sedang berjalan...")

    # Membuat cursor
    cursor = cnx.cursor()

    # Mengambil semua data pada tabel terkait
    query_get_table_data = f"SELECT * FROM {get_table_name}"
    cursor.execute(query_get_table_data)

    # Mengambil semua hasil query
    results = cursor.fetchall()

    # Menampilkan hasil query
    for row in results:

        # Mengambil value kode_barang pada table mysql
        text_kode_barang = row[indexKeyChoosen]

        if get_custom_nama_file != "":
            text_nama_barang = row[indexKeyChoosenNamaFile]    
            nama_file = f"{text_nama_barang.replace('/', 'per')} [{text_kode_barang}]"
        else:
            nama_file = text_kode_barang

        # Mengecek apakah kode barang berupa string atau tidak
        try:
            int(text_kode_barang)
            continue
        except ValueError:
            
            # Konversi ke code barcode 128
            backend.text_to_barcode128.convert(text_kode_barang, image_file_name=nama_file, additional_path="barcode128_result/automate/")
            

    # Menutup koneksi dan cursor
    cursor.close()
    cnx.close()
    colNameFetcherCursor.close()
    backend.insert_to_excel.inserting()

    input("[Finish] Yeay, teks berhasil diubah menjadi kode barcode128 secara masal!\n\n[Tekan 'Enter' untuk kembali ke-menu utama!]")

    return True
