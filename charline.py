#!/usr/bin/python

from subprocess import Popen, PIPE
import sys

ip = sys.argv[1]
filename = sys.argv[2]

# -c client, -p port, -P parallel, -i interval, -f format_output,

tcp = ["iperf3", "-c", ip,  # server address
       "-p", "5201",        # server port
       "-P", "1",           # parallel process
       "-i", "1",           # intervals
       "-f", "m",           # format output m = Mbits
       "-t", "10",          # experiment time
       "-l", "56.0K",       # buffer length
       "-w", "64.0K",       # tcp window size
       "-M", "1400B",       # max segment size
       "-N"]                # tcp no delay

udp = ["iperf3", "-c", ip,  # server address
       "-p", "5201",        # server port
       "-u",                # use udp protocol
       "-P", "1",           # parallel process
       "-i", "1",           # intervals
       "-f", "m",           # format output m = Mbits
       "-t", "10",          # experiment time
       "-b", "1.0M",        # bandwith
       "-w", "64.0K",       # udp buffer size
       "-l", "1400B"]       # udp packet size


def execute_scenario(scenario):

    process = Popen(scenario, stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()

    return output


def main():

    scenarios = []
    scenarios.append(tcp)
    scenarios.append(udp)

    for scenario in scenarios:
        title = str(scenario) + "\n"
        output = execute_scenario(scenario)

        print output


main()
