# Python program to illustrate the concept 
# of threading 
import threading
import json
import datetime

def drink_reminder_task():
    while(1>0):
        timings_list = []
        with open('timings.json') as json_file:
            data = json.load(json_file)
            for p in data:
                time_val = p['time']
                timings_list.append(time_val)
        current_time = datetime.datetime.now()
        hour_val = current_time.hour
        min_val = current_time.minute
        if int(min_val) < 10 :
            min_val = "09"
        curr_time = str(hour_val) + "." + str(min_val)
        #print(str(hour_val) + ":" + str(min_val))
        #print(timings_list)
        #print(str(curr_time in timings_list))
        if curr_time in timings_list :
            print("Drink water")


if __name__ == "__main__":
	t1 = threading.Thread(target=drink_reminder_task, name='t1', daemon='true')
	t1.start()
	t1.join()
