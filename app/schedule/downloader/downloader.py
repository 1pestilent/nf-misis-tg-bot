import requests
import os

from app.schedule.downloader.timecalc import *
from app.schedule.dirs import xlsx_dir

def get_schedule(week):

    base_link = 'https://nf.misis.ru/images/uo/OFO'
    courses = (1,2,3,4)
    paths = []
    names = []

    if not os.path.exists(xlsx_dir):
        os.makedirs(xlsx_dir)

    for i in courses:
        link = f'{base_link}/{i}k%20{week}.xlsx'
        name = f'{i}k_{week[:-5]}.xlsx'
        path = f'{xlsx_dir}/{name}'
        try:
            response = requests.get(link)
            if response.status_code == 200:
                with open(path, 'wb') as file:
                    file.write(response.content)
                print(f'{name} - успешно скачен!')
                paths.append(path)
                names.append(name)
                
            else:
                link = f'{base_link}/{i}k.%20{week}.xlsx'
                response = requests.get(link)
                if response.status_code == 200:
                    with open(path, 'wb') as file:
                        file.write(response.content)
                    print(f'{name} - успешно скачен!')
                    paths.append(patn)  
                    names.append(name)
                else:
                    print(f"Ошибка при скачивании файла: {response.status_code}")
                    return False
        except Exception as e:
            print(f"Произошла ошибка: {e}")
    return paths
print(get_schedule(get_current_week()))