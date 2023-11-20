from datetime import datetime, timedelta
today = datetime(year=2023, month=5, day=31)
print(f'{today:%B %d, %Y}')
now = datetime.now()
ten_days_ago = now - timedelta(days=10)
print(f'{ten_days_ago:%Y-%m-%d %H:%M:%S}')
print(f'{now:%Y-%m-%d %H:%M:%S}')