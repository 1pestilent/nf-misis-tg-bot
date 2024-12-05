import requests
import os

from app.schedule.dirs import xlsx_dir

def download_schedule(course, week):

    base_link = 'https://nf.misis.ru/images/uo/OFO'

    if not os.path.exists(xlsx_dir):
        os.makedirs(xlsx_dir)

    patterns = ['kurs','k.','k']
    
    try:
        files = os.listdir(xlsx_dir)

        for pattern in patterns:
            name = f'{course}{pattern}%20{week}.xlsx'
            path = f'{xlsx_dir}/{name}'

            if name not in files:
                link = f'{base_link}/{name}'
                response = requests.get(link)
                if response.status_code == 200:
                    with open(path, 'wb') as file:
                        
                        file.write(response.content)
                    print(f'[Успешно] {name} - скачен!')
                    return path
                else:
                    print(f'[Ошибка] {link} - не существует!')
                    continue
            else:
                return False
    except Exception as e:
        print(f"[Ошибка] {e}")
