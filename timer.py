import time

def time_settings(list_settings):
    if list_settings == [0]:
        return [25, 5, 15]
    else:
        return list_settings

settings = [int(i) for i in input('write work time short break long break, 0 to standard:').split(" ")]
print(time_settings(settings))

work_time = time_settings(settings)[0]*60
short_break = time_settings(settings)[1]*60
long_break = time_settings(settings)[2]*60

session_count = 0
mode = 'work'
remaining = work_time

while True:
    mins = remaining//60
    secs = remaining%60
    print(f'\r{mode}: {mins:02d}:{secs:02d}', end="")
    time.sleep(1)
    remaining -= 1

    if remaining < 0:
        if mode == 'work':
            session_count += 1

            if session_count % 4 == 0:
                mode = "long_break"
                remaining = long_break
            else:
                mode = 'break'
                remaining = short_break 
        
        else:
            mode = "work"
            remaining = work_time
