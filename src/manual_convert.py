import backend.text_to_barcode128
import os

def start_manual_convert():
    while(True):

        text_to_code = input("[Input] Text To Barcode : ")
        try:        
            backend.text_to_barcode128.convert(text_to_code, additional_path="barcode128_result/manual/")
            print("\n[+] Yeay, barcode has been succesfully generated!")
        except:
            print("\n[+] Oops, barcode has been failed generated!")

        use_this_tool_again = input("\n[+] Use This Tools Again? (Type : 'ga' if you want to close this or press enter if you want to continue!) ")
        print("")
        if use_this_tool_again.lower() in ["no", "n", "gak", "ga", "g", "tidak", "tdk", "gk"]:
            print("[Finish] Thanks for using hanz barcode!")            
            return True
        
        os.system("cls")