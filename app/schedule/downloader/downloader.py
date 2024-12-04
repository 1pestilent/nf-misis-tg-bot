import requests
import os

from app.schedule.dirs import xlsx_dir

def download_schedule(course, week):

    base_link = 'https://nf.misis.ru/images/uo/OFO'

    if not os.path.exists(xlsx_dir):
        os.makedirs(xlsx_dir)

    patterns = ['kurs','k.','k']
    name = f'{course}k_{week[:-5]}.xlsx'
    path = f'{xlsx_dir}/{name}'
    
    try:
        for pattern in patterns:
            link = f'{base_link}/{course}{pattern}%20{week}.xlsx'
            print(link)
            response = requests.get(link)
            if response.status_code == 200:
                with open(path, 'wb') as file:
                    file.write(response.content)
                print(f'[Успешно] {name} - скачен!')
                return path
            else:
                continue
    except Exception as e:
        print(f"[Ошибка] {e}")
