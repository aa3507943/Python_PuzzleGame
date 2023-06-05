from re import M
import threading
import time

def timer(start_time):
    end_time = time.time()
    time_count = int(end_time-start_time)
    time_list = time_convert(time_count)
    
    return time_list
    # print("start time: ", start_time)
    # print("end time: ", end_time)
    # print("time count: ", time_count)
    # print(hour, " : ", minute, " : ", second)

def time_convert(time_count):    
    level1_time = 0
    level2_time = 0
    level3_time = 0
    global result_second_0
    global result_second_1
    global result_minute_0
    global result_minute_1
    global result_hour_0
    global result_hour_1
    while time_count >= 3600: 
        time_count -= 3600
        level3_time += 1
    while time_count >= 60:
        time_count -= 60
        level2_time += 1
    level1_time = time_count

    if level1_time >= 10 : 
        result_second_0 = str(int(level1_time/10))
        result_second_1 = str(int(level1_time%10))
    else:
        result_second_0 = '0'
        result_second_1 = str(int(level1_time))
    if level2_time >= 10 : 
        result_minute_0 = str(int(level2_time/10))
        result_minute_1 = str(int(level2_time%10))
    else:
        result_minute_0 = '0'
        result_minute_1 = str(int(level2_time))

    if level3_time >= 10:
        result_hour_0 = str(int(level3_time[0]))
        result_hour_1 = str(int(level3_time[1]))
    else:
        result_hour_0 = '0'
        result_hour_1 = str(int(level3_time))
    return [result_hour_0, result_hour_1, result_minute_0, result_minute_1, result_second_0, result_second_1]


start_time = time.time()
timer(start_time)