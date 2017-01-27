from datetime import datetime
hour = datetime.now().hour
if hour < 12:
    time_of_day = 'morning'
else:
    time_of_day = 'afternoon'
print ('Good %s, people' % time_of_day)
