# #Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

# The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

# It is much easier to understand with an example:

# format_duration(62)    # returns "1 minute and 2 seconds"
# format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"

# For the purpose of this Kata, a year is 365 days and a day is 24 hours.

# Note that spaces are important.
# Detailed rules

# The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

# The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

# A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

# Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

# A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

# A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.

def format_duration(seconds):

    time = ""
    time_descrp = ["year", "day", "hour", "minute", "second"]
    new_lis = []

    a_second = 1
    a_min = 60
    an_hour = 3600
    a_day = 86_400
    a_year = 31_536_000

    full_time = 0
    no_years = 0
    no_days = 0
    no_hours = 0
    no_mins = 0
    no_secs = 0
    remaining_time = seconds
    time_list = []

    while remaining_time >= 1:
        if remaining_time >= a_year:
            full_time = remaining_time / a_year
            no_years = int(full_time)
            if no_years > 1:
                time_list.append(f"{no_years} years")
            else:
                time_list.append(f"{no_years} year")
            remaining_sec_floating = full_time - no_years
            remaining_sec = remaining_sec_floating * a_year
            remaining_time = remaining_sec

        elif remaining_time >= a_day:
            full_time = remaining_time / a_day
            no_days = int(full_time)
            if no_days > 1:
                time_list.append(f"{no_days} days")
            else:
                time_list.append(f"{no_days} day")
            remaining_sec_floating = full_time - no_days
            remaining_sec = remaining_sec_floating * a_day
            remaining_time = remaining_sec

        elif remaining_time >= an_hour:
            full_time = remaining_time / an_hour
            no_hours = int(full_time)
            if no_hours > 1:
                time_list.append(f"{no_hours} hours")
            else:
                time_list.append(f"{no_hours} hour")
            remaining_sec_floating = full_time - no_hours
            remaining_sec = remaining_sec_floating * an_hour
            remaining_time = remaining_sec

        elif remaining_time >= a_min:
            full_time = remaining_time / a_min
            no_mins = int(full_time)
            if no_mins > 1:
                time_list.append(f"{no_mins} minutes")
            else:
                time_list.append(f"{no_mins} minute")
            remaining_sec_floating = full_time - no_mins
            remaining_sec = remaining_sec_floating * a_min
            remaining_time = remaining_sec

        elif remaining_time >= a_second:
            full_time = remaining_time / a_second
            no_secs = int(full_time)
            if no_secs > 1:
                time_list.append(f"{no_secs} seconds")
            else:
                time_list.append(f"{no_secs} second")
            remaining_sec_floating = full_time - no_secs
            remaining_sec = remaining_sec_floating * a_second
            remaining_time = remaining_sec
            

    final_list = []

    for x in range(0, len(time_list)):
        if x == len(time_list) - 2:
            final_list.append(time_list[x])
            final_list.append("and")
        elif x == len(time_list) - 1:
            final_list.append(time_list[x])
        else:
            final_list.append(f"{time_list[x]},")

    if seconds == 0:
        return "now"
    else:
        return " ".join(final_list)

print(format_duration(4906920))