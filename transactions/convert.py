import img2pdf
import time
from PIL import Image
import os


def jpg_converter(jpg_file_path, is_png=False):

    file_name = jpg_file_path[jpg_file_path.rfind("/")].replace(".jpg", "")

    pdf_path = "pdfs/{}.pdf".format(file_name)

    t1 = time.time()

    pdf_bytes = img2pdf.convert(jpg_file_name)

    file = open(pdf_path, "wb")

    file.write(pdf_bytes)

    file.close()

    if is_png:
        os.remove(jpg_file_name)

    t2 = time.time()

    print("{} -->  {} seconds".format(new_jpg, round(t2-t1, 4)))


def png_converter(png_file_name):

    new_png = png_file_name.replace("pngs/", "").replace(".png", "")

    temp_jpg_file = "temp_jpgs/temp_jpg{}.jpg".format(new_png)

    im = Image.open(png_file_name)

    rgb_im = im.convert('RGB')

    im.close()
    rgb_im.save(temp_jpg_file)
    return jpg_converter(temp_jpg_file, is_png=True)
