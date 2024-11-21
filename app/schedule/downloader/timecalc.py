from datetime import datetime, timedelta

def get_current_week():
    today = datetime.now()
    weekday = datetime.weekday(today)
    current_week = f'{(today - timedelta(weekday)).strftime('%d.%m')}-{(today-timedelta(weekday)+timedelta(5)).strftime('%d.%m.%Y')}'
    return current_week

def get_next_week():
    today = datetime.now()
    days_until_next_week = 7 - datetime.weekday(today) 
    next_week = f'{(today + timedelta(days_until_next_week)).strftime('%d.%m')}-{((today + timedelta(5 + days_until_next_week)).strftime('%d.%m.%Y'))}'
    return next_week
