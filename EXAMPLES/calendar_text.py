#!/usr/bin/env python
from calendar import TextCalendar

text_calendar = TextCalendar()  # <1>
print(text_calendar.formatmonth(2022, 3))  # <2>

print()

print(text_calendar.formatyear(2022))
