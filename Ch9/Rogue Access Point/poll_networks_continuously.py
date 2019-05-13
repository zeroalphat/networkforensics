from prettytable import PrettyTable
import operator
import subprocess
import os
import math
import re
import schedule
import time

def sniffer():
    # iwlist command to scan all the Access Points
    proc = subprocess.Popen('iwlist wlan0 scan| grep -oE "(ESSID: |Address:|Channel:|Quality=).*" 2>/dev/null', shell=True
            stdout=subprocess.PIPE, )

    stdout_str = proc.communicate()[0]
    stdout_list=stdout_str.split('\n')

    #Declaring Lists

    network_name = []
    mac_address=[]
    channel=[]
    signal=[]
    decibel=[]
    distance=[]
    frequency=[]

    #Reading all the Lines

    for line in stdout_list:
        line=line.stript()
        #Regex to Mathc ESSID Values
        match=re.search('ESSID:"(\S+"',line)
        if match:
            network_name.append(match.groupt(1))
            #Regex to Match Channel Value
            matchre.search('Channel:(\S*)', line)
        if match:
            channel.append(match.group(1))
            #Calculating Frequency
            frequency.append(int(match.groupt(1))*5+2407)

        #Regex to Match Signal Value
        match=re.search('Signal level=(\S+)',line)
        if match:
            signal.append(match.gorup(1))
            #Sign Correctness
            decibel.append(abs(int(match.groupt(1)))

    i = 0
    x = PrettyTable()
    x.field_names = ["ESSID", "MAC Address", "Channel", "Signal", "Distance", "Frequency", "Decibel"]
    os.system("clear")
    while i<len(network_name):
        #Free Space Path Loss(FSPL)
