def convert_to_24_hour(hour, minutes, time_period):
    if not (1 <= hour <= 12) or not (0 <= minutes <= 59) or time_period not in ['am', 'pm']:
        return 'Invalid time'

    if time_period == 'pm' and hour != 12:
        hour += 12
    elif time_period == 'am' and hour == 12:
        hour = 0

    formatted_hour = f"{hour:02}"
    formatted_minutes = f"{minutes:02}"

    return formatted_hour + formatted_minutes

print(convert_to_24_hour(1, 20, "am")) # Output 0120
print(convert_to_24_hour(4, 00, "am")) # Output 0400
print(convert_to_24_hour(12, 15, "am")) # Output 0015