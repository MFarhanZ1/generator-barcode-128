import code128

def convert(text_to_code, image_file_name, additional_path=None):
    code128.image(text_to_code).save(f"{additional_path}{image_file_name}.jpg")
    