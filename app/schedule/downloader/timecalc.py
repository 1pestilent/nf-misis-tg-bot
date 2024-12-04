from datetime import datetime, timedelta

def get_current_week():
    today = datetime.now()
    weekday = datetime.weekday(today)
    current_week = f'{(today - timedelta(weekday)).strftime('%d.%m')}-{(today-timedelta(weekday)+timedelta(5)).strftime('%d.%m.%Y')}'
    return current_week

def get_first_day_current_week():
    today = datetime.now()
    weekday = datetime.weekday(today)
    first_day = (today-timedelta(weekday))
    return first_day