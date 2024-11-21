import requests

from app.schedule.downloader.timecalc import *


def get_schedule(week):

    base_link = 'https://nf.misis.ru/images/uo/OFO'
    courses = (1,2,3,4)

    for i in courses:
        link = f'{base_link}/{i}k%20{week}.xlsx'
        name = f'{i}k_{week}.xlsx'
        path = f'app/schedule/handler/{name}'
        try:
            response = requests.get(link)
            if response.status_code == 200:
                with open(save_name, 'wb') as file:
                    file.write(response.content)
                print(f'{save_name} - успешно скачен!')
            else:
                link = f'{base_link}/{i}k.%20{week}.xlsx'
                response = requests.get(link)
                if response.status_code == 200:
                    with open(save_name, 'wb') as file:
                        file.write(response.content)
                    print(f'{save_name} - успешно скачен!')
                else:
                    print(f"Ошибка при скачивании файла: {response.status_code}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

get_schedule(get_current_week())