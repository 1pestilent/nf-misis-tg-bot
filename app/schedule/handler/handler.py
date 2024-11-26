from openpyxl import load_workbook

import zipfile
import os

from app.schedule.dirs import xlsx_dir, pdf_dir, zip_dir

def delete_3_sheet():

    files = os.listdir(xlsx_dir)
    
    for xlsx in files:
        if xlsx.endswith('.xlsx'):
            xlsx_path = (f'{xlsx_dir}/{xlsx}')
            workbook = load_workbook(xlsx_path)

        if len(workbook.sheetnames) < 3:
            print(f"[Ошибка] В документе'{xlsx}' нет 3-его листа!!!")
            continue
            

        sheet_to_delete = workbook.sheetnames[2]
        workbook.remove(workbook[sheet_to_delete])

        workbook.save(xlsx_path)
        print(f"[Успех] Лист '{sheet_to_delete}' удалён из файла {xlsx}.")

    return True


def unzip():
    
    files = os.listdir(zip_dir)

    for zip in files:
        if zip.endswith('.zip'):
            with zipfile.ZipFile(f'{zip_dir}/{zip}', 'r') as zipper:
                zipper.extractall(pdf_dir)
                print(f"[Успешно] Архив {zip} успешно разархивирован")