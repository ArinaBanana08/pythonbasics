from datetime import datetime, timedelta

today = datetime.now()
christmas = datetime(2024, 5, 29)

days_until_christmas = (christmas - today).days
print("There are",days_until_christmas,"days until my B-day!!")