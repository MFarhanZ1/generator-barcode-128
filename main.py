from src import *
import os
import time

def banner_and_process():
    os.system("cls")
    
    print("""

    ██   ██  █████  ███    ██ ███████     ██████   █████  ██████   ██████  ██████  ██████  ███████ 
    ██   ██ ██   ██ ████   ██    ███      ██   ██ ██   ██ ██   ██ ██      ██    ██ ██   ██ ██      
    ███████ ███████ ██ ██  ██   ███       ██████  ███████ ██████  ██      ██    ██ ██   ██ █████   
    ██   ██ ██   ██ ██  ██ ██  ███        ██   ██ ██   ██ ██   ██ ██      ██    ██ ██   ██ ██        Developed by @mfarhanz1 (v1.27)
    ██   ██ ██   ██ ██   ████ ███████     ██████  ██   ██ ██   ██  ██████  ██████  ██████  ███████   Barcode Generator System

    Choose what you want to do!
    1. Manual Convert
    2. Automatic Convert From MYSQL-DBS                                                                                        
    3. Exit
    """)    

    choosen_menu = int(input("    >> "))

    os.system("cls")

    if choosen_menu == 1:
        if start_manual_convert():
            banner_and_process()

    elif choosen_menu == 2:
        if start_auto_convert():
            banner_and_process()
    else:
        quit()

if __name__ == "__main__":
    banner_and_process()