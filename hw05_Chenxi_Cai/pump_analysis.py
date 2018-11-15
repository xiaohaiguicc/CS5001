"""
Reading data from a file
Report the duration of the data file in both hours and days
Report total number of gallons produced and daily average.
Report the total power used by the pump.
"""

# Invert minutes to hours and days
import math

# Global variable
POWER_LINE = 500
GALLONS_1 = 7
GALLONS_2 = 4000
WA_TO_KWH = 60000
MIN_TO_H = 60
MIN_TO_D = 24 * 60
LONG_TIME_LINE = 120

def duration(minutes):
    """Time conversion"""
    hour = minutes / MIN_TO_H
    day = minutes / MIN_TO_D
    return hour, day

def consume_certain(gallons_total, datas, gal_certain):
    """mins to consume a certain quantity of water

    Keyword arguments:
    gallons_total -- total gallons
    datas -- list of minute watt
    gal_certain -- a certain quantity of gallons
    """
    if gal_certain > gallons_total:
        min_take = -1
    else:
        min_certain = math.ceil(gal_certain / 2)
        min_take = 0
        min_run_certain = 0
        for data in datas:
            min_take += 1
            if data > POWER_LINE:
                min_run_certain += 1
            if min_run_certain >= min_certain:
                break
    return min_take

def long_run(datas):
    """How long it runs in a row ( >= 120min)"""
    long_list = []
    min_long = 0 # continuous running mins
    for i in range(len(datas) - 1):
        if(datas[i] > POWER_LINE and datas[i + 1] > POWER_LINE):
            min_long += 1
        elif(datas[i] > POWER_LINE and datas[i + 1] <= POWER_LINE):
            min_long += 1
            long_list.append([i, min_long]) # stop running
        else:
            min_long = 0

    if(datas[-2] > POWER_LINE and datas[-1] > POWER_LINE):
        long_list[-1][0] += 1 # the condition that pump is also
        long_list[-1][1] += 1 # running in the last two mins.
    print("Information on water softener recharges:")
    for long_per in long_list:
        if long_per[1] >= LONG_TIME_LINE:
            start_time = long_per[0] - long_per[1] + 2
            print("{} minute run started at {}"
                  .format(long_per[1], start_time))


def main():
    """report"""
    file_name = input("Please enter the file name:\n")
    try:
        with open("pump_data/" + file_name) as f:
            lines = f.readlines() # total lines
    except FileNotFoundError:
        print("Unable to open", file_name)
    else:
        minutes_total = len(lines)
        hour_total, day_total = duration(minutes_total)
        print("Data covers a total of {} hours\n"
              "(That's {} days)\n".format(hour_total, day_total))

        datas = []
        minute_run = 0
        watt_total = 0
        for line in lines:
            data = int(line.rstrip())
            datas.append(data) # a list with minute power
            watt_total += data
            if data > POWER_LINE:
                minute_run += 1 # total running mins

        gallons_total = 2 * minute_run
        gallons_daily = gallons_total / day_total
        print("Pump was running for {} minutes,"
              "producing {} gallons\n"
              "(That's {} gallons per day)\n"
              .format(minute_run, gallons_total, gallons_daily))

        print("Pump required a total of {} watt minutes of power\n"
              "That's {:.5f} kWh\n".format(watt_total, watt_total / WA_TO_KWH))

        consume_1 = consume_certain(gallons_total, datas, GALLONS_1)
        print("It took {} minutes of data to reach {} gallons"
              .format(consume_1, GALLONS_1))
        consume_2 = consume_certain(gallons_total, datas, GALLONS_2)
        print("It took {} minutes of data to reach {} gallons"
              .format(consume_2, GALLONS_2))

        long_run(datas)

main()
