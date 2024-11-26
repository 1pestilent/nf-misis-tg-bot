from pylovepdf import OfficeToPdf
from pylovepdf.ilovepdf import ILovePdf

from dotenv import load_dotenv
import os
import time

load_dotenv()

from app.schedule.dirs import *

def xlsx_to_pdf():
    if not os.path.exists(zip_dir):
        os.makedirs(zip_dir)
    
    files = os.listdir(xlsx_dir)
    task = OfficeToPdf(os.getenv('PUBLIC_KEY_ILPDF'), True, None)

    for xlsx in files:
        if xlsx.endswith('.xlsx'):
            xlsx_path = f'{xlsx_dir}/{xlsx}'
            print(xlsx_path,'\n','\n')
            
            task.add_file(xlsx_path)
    task.set_output_folder(zip_dir)
    task.execute()
    task.download()