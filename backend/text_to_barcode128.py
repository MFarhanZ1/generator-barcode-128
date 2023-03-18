import code128

def convert(text_to_code, additional_path=None):
    code128.image(text_to_code).save(f"{additional_path}{text_to_code}.jpg")