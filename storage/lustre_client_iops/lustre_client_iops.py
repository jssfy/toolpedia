#!/usr/bin/python 
#-*-coding:utf-8-*- 

import json
import sys
import time

# TBD: auto discovery
# data_path = "/proc/fs/lustre/llite/nvmefs-ffff883f8a4f2800/stats"
data_path = "/proc/fs/lustre/lmv/shnvme3-clilmv-ffff8859d3e2d000/md_stats"

# use a dic1/dic2 to hold sampling data
def load_data(dic):
    # Open file    
    fileHandler = open(data_path, "r")
    # Get list of all lines in file
    listOfLines = fileHandler.readlines()
    # Close file
    fileHandler.close()

    # Iterate over the lines
    for  line in  listOfLines:
        words = line.split()
        if(len(words) < 2):
            println("got error line, to skip")
            continue
        dic[words[0]] = float(words[1])
        # print(dic)


# put "next - prev" into delta
def calc_delta(prev, next, delta):
    for key in prev:
        delta[key] = next[key] - prev[key]


# print a dictionary in the indented json format
def print_dict(dic):
    print(json.dumps(dic, indent=2, sort_keys=True, ensure_ascii=False))


# calculate iops for each category except snapshot_time, all divided by snapshot_time
def calc_iops_from_delta(delta):
    # in case of snapshot_time error, skip
    if (delta['snapshot_time'] < 0.000001):
        print("error: time gap too small")
        return
    for key in delta:
        if ('snapshot_time' != key):
            delta[key] = int(delta[key]/delta['snapshot_time'])

if __name__ == '__main__':
    # dic1/dic2 are used to load prev/next kernel data interchangably
    # calc delta by doing: next - prev
    # calc iops by doing: delta/time_consumption
    dic1 = {}
    dic2 = {}
    delta = {}

    load_data(dic1)
    prev = 1
    # load_data(dic2)
    # calc_delta(dic1, dic2, delta)
    # calc_iops_from_delta(delta)
    # print_dict(delta)

    # dic1['name'] = 'anhua'
    # print_dict(dic1)

    # enter loop
    while True:
        time.sleep(2) # TBD: configurable
        if prev == 1:
            load_data(dic2)
            prev = 2
            calc_delta(dic1, dic2, delta)
        else:
            load_data(dic1)
            prev = 1
            calc_delta(dic2, dic1, delta)
        calc_iops_from_delta(delta)
        print_dict(delta)
