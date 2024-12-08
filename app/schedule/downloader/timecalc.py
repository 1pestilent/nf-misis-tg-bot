from datetime import datetime, timedelta

class Monday():
    def __init__(self):
        self.today = datetime.now()
        self.weekday = datetime.weekday(self.today)
    
    def __str__(self):
        str_monday = (self.today-timedelta(self.weekday)).strftime(('%d.%m.%Y'))
        return str_monday
    
    @property
    def date(self):
        monday = (self.today-timedelta(self.weekday))
        return monday

    @property
    def week(self):
        current_week = f'{(self.today - timedelta(self.weekday)).strftime('%d.%m')}-{(self.today-timedelta(self.weekday)+timedelta(5)).strftime('%d.%m.%Y')}'
        return current_week

    @property
    def next(self):
        class Next_Monday:
            def __init__(self, today, weekday):
                self.next_monday = today + timedelta(7) - timedelta(weekday)
            
            def __str__(self):
                return self.next_monday.strftime('%d.%m.%Y')
            
            @property
            def date(self):
                return self.next_monday
            
            @property
            def week(self):
                next_week = f'{(self.next_monday).strftime('%d.%m')}-{(self.next_monday+timedelta(5)).strftime('%d.%m.%Y')}'
                return next_week

        
        return Next_Monday(self.today, self.weekday)

    @property
    def previous(self):
        class Previous_Monday:
            def __init__(self, today, weekday):
                self.previous_monday = today - timedelta(7) - timedelta(weekday)
            
            def __str__(self):
                return self.previous_monday.strftime('%d.%m.%Y')
            
            @property
            def date(self):
                return self.previous_monday
            
            @property
            def week(self):
                previous_week = f'{(self.previous_monday).strftime('%d.%m')}-{(self.previous_monday+timedelta(5)).strftime('%d.%m.%Y')}'
                return previous_week
            
        return Previous_Monday(self.today, self.weekday)




m = Monday()
print(m.previous.date)