from datetime import date
import holidays
uk_holidays = holidays.Nigeria()
  

for ptr in holidays.Nigeria(years = 2020).items():
    print(ptr)
