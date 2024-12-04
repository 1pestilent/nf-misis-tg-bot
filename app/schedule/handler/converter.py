from pylovepdf import OfficeToPdf
from pylovepdf.ilovepdf import ILovePdf

from pdf2image import convert_from_path

from dotenv import load_dotenv
import os
import time

load_dotenv()

from app.schedule.dirs import *

def xlsx_to_pdf(path):
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)
    
    task = OfficeToPdf(os.getenv('PUBLIC_KEY_ILPDF'), True, None)      
    task.add_file(path)
    task.set_output_folder(pdf_dir)
    task.execute()
    name = task.download()
    path = f'{pdf_dir}/{name}'
    task.delete_current_task()

    print(f'{path} - путь к PDF после конвертации')
    return path

def pdf_to_png(path, course, week):
    paths = []
    
    if not os.path.exists(png_dir):
        os.makedirs(png_dir)

    images = convert_from_path(path)

    for i, image in enumerate(images):
        name = f'{course}k{week}p{i}.png'
        path = f'{png_dir}/{name}'
        image.save(path, 'PNG')
        paths.append(path)
        print(f'[Успешно] Файл {name} успешно сохранён')
    print(paths)
    return paths
