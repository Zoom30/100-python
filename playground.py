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


x = "hello"

# [1, 1, 2]