#1
from datetime import datetime, timedelta

x = datetime.now()
y=x-timedelta(days=5)
print(y.strftime("%x"))

#2
from datetime import datetime, timedelta

x = datetime.now()
yesderday=x-timedelta(days=1)
tomorrow=x-timedelta(days=(-1))
print(yesderday.strftime("%x"))
print(x.strftime("%x"))
print(tomorrow.strftime("%x"))

#3
from datetime import datetime, timedelta

x = datetime.now()
drop_mseconds=x.replace(microsecond=0)
print(drop_mseconds)

#4
from datetime import datetime

date1 = datetime(2025, 2, 11, 12, 0, 0)
date2 = datetime(2025, 2, 10, 10, 30, 0)

difference = abs((date1 - date2).total_seconds())
print(difference)