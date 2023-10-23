from datetime import datetime, timedelta


class CalendarIterator:
    def __init__(self, start_date, end_date):
        self.current_date = start_date
        self.end_date = end_date

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_date > self.end_date:
            raise StopIteration
        else:
            date_str = self.current_date.strftime("%d %B")
            self.current_date += timedelta(days=1)
            return date_str


start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

calendar = CalendarIterator(start_date, end_date)
for day in calendar:
    print(day)
