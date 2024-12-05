from datetime import datetime, timedelta

def get_current_week():
    today = datetime.now()
    weekday = datetime.weekday(today)
    current_week = f'{(today - timedelta(weekday)).strftime('%d.%m')}-{(today-timedelta(weekday)+timedelta(5)).strftime('%d.%m.%Y')}'
    return current_week

class Monday():
    def __init__(self):
        self.today = datetime.now()
        self.weekday = datetime.weekday(self.today)
    
    def date(self):
        monday = (self.today-timedelta(self.weekday))
        return monday
    
    def __str__(self):
        str_monday = (self.today-timedelta(self.weekday)).strftime(('%d.%m.%Y'))
        return str_monday
    