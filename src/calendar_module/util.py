import calendar

def day_of_week(date_string):
    month, day, year = map(int, date_string.split())
    days = {0: 'MONDAY', 1: 'TUESDAY', 2: 'WEDNESDAY', 3: 'THURSDAY', 4: 'FRIDAY', 5: 'SATURDAY', 6: 'SUNDAY'}
    return days[calendar.weekday(year, month, day)]