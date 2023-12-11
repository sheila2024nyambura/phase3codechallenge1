def convert_to_24_hour(hour, minutes, time_period):
    if not (1 <= hour <= 12) or not (0 <= minutes <= 59) or time_period not in ['am', 'pm']:
        return 'Invalid time'

    if time_period == 'pm' and hour != 12:
        hour += 12
    elif time_period == 'am' and hour == 12:
        hour = 0

    