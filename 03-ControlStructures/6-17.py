time=(input('Enter time (24-hour format): '))
hours = int(time[:2])
minutes = time[3:5]
if hours<12:
    period="am"
elif hours>=12:
    period="pm"
hours = hours % 12

if hours == 0:
    hours = 12

print(f"Time in 12-hour format: {hours}:{minutes}{period}")
