import code128

print("""

    ██   ██  █████  ███    ██ ███████     ██████   █████  ██████   ██████  ██████  ██████  ███████ 
    ██   ██ ██   ██ ████   ██    ███      ██   ██ ██   ██ ██   ██ ██      ██    ██ ██   ██ ██      
    ███████ ███████ ██ ██  ██   ███       ██████  ███████ ██████  ██      ██    ██ ██   ██ █████   
    ██   ██ ██   ██ ██  ██ ██  ███        ██   ██ ██   ██ ██   ██ ██      ██    ██ ██   ██ ██        Developed by @mfarhanz1 (v1.27)
    ██   ██ ██   ██ ██   ████ ███████     ██████  ██   ██ ██   ██  ██████  ██████  ██████  ███████   Barcode Generator System
                                                                                               
""")    

while(True):

    text_to_code = input("[Input] Text To Barcode : ")
    try:        
        code128.image(text_to_code).save(f"{text_to_code}.jpg")
        print("\n[+] Yeay, barcode has been succesfully generated!")
    except:
        print("\n[+] Oops, barcode has been failed generated!")

    use_this_tool_again = input("\n[+] Use This Tools Again? (Type : 'ga' if you want to close this or press enter if you want to continue!)")
    if use_this_tool_again.lower() in ["no", "n", "gak", "ga", "g", "tidak", "tdk", "gk"]:
        print("\n[+] Thanks for using hanz barcode!")
        break
