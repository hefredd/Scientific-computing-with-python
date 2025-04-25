def add_time(start, duration, starting_day=None):
    days_of_week =['monday','tuesday','wednesday','thursday', 'friday','saturday', 'sunday']

    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))

    duration_hour, duration_minute = map(int, duration.split(":"))

    if period == "PM" and start_hour != 12:
        start_hour += 12
    if period == "AM" and start_hour == 12:
        start_hour = 0

    end_minute = start_minute + duration_minute
    extra_hour = end_minute // 60
    end_minute %= 60

    end_hour = start_hour + duration_hour + extra_hour
    extra_day = end_hour // 24
    end_hour %= 24

    if end_hour == 0:
        display_hour = 12
        final_period = "AM"
    elif end_hour < 12:
        display_hour = end_hour
        final_period = "AM"
    elif end_hour == 12:
        display_hour = end_hour
        final_period = "PM"
    else:
        display_hour = end_hour - 12
        final_period = "PM"


    result_day = ""
    if starting_day:
        start_day_index = days_of_week.index(starting_day.lower())
        final_day = days_of_week[(start_day_index + extra_day) %7].capitalize()
        result_day = (f', {final_day}')

    if extra_day == 1:
        day_str = ' (next day)'
    elif extra_day > 1:
        day_str = f' ({extra_day} days later)'
    else:
        day_str = ""

    new_time = f'{display_hour}:{end_minute:02d} {final_period}{result_day}{day_str}'

    return new_time

start_input = input("Enter the start time (e.g. '3:30 PM'): ")
duration_input = input("Enter the duration (e.g. '2:12'): ")
day_input = input("Enter the starting day (optional): ")

# Call the function with user's input
if day_input.strip():
    result = add_time(start_input, duration_input, day_input)
else:
    result = add_time(start_input, duration_input)

print(f"New time: {result}")

