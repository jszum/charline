#!/usr/bin/python

from subprocess import Popen, PIPE
import sys
from iperf import *


# iperf3 -c 192.168.1.1 -P 1 -i 1 -p 5201 -f m -t 10
tcpex = ["iperf3", "-c", ip,  # server address
       "-p", "5201",        # server port
       "-P", "1",           # parallel process
       "-i", "1",           # report intervals
       "-f", "m",           # format output m = Mbits
       "-t", "10",          # experiment time (-n experiments bytes)
       "-l", "56.0K",       # buffer length
       "-w", "64.0K",       # tcp window size
       "-M", "1400B",       # max segment size
       "-N"]                # tcp no delay

# iperf3 -c 192.168.1.1 -u -P 1 -i 1 -p 5201 -f m -b 1.0M -t 10
udpex = ["iperf3", "-c", ip,  # server address
       "-p", "5201",        # server port
       "-u",                # use udp protocol
       "-P", "1",           # parallel process
       "-i", "1",           # report intervals
       "-f", "m",           # format output m = Mbits
       "-t", "10",          # experiment time (-n experiments bytes)
       "-b", "1.0M",        # bandwith
       "-w", "64.0K",       # udp buffer size
       "-l", "1400B"]       # udp packet size


def execute_scenario(scenario):

    process = Popen(scenario, stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()

    return output


def save_experiment(title, result, file):
    stars = "*"*15 + "\n"

    final_text = stars + title + stars + result + "\n"*3

    f = open(file, 'a')
    f.write(final_text)
    f.close()


def add_scenarios(scenarios_array):
    for element in test_cases:
        scenarios_array.append(element.get_command())


def main():
    scenarios = []
    add_scenarios(scenarios)

    counter = 0
    for scenario in scenarios:
        counter += 1
        title = str(scenario) + "\n"
        output = execute_scenario(scenario)

        print "Scenario " + str(counter) + " DONE"
        save_experiment(title, output, filename)


if __name__ == "__main__":
    main()
