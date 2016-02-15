#!/usr/bin/python

from subprocess import Popen, PIPE
import sys

ip = sys.argv[1]
filename = sys.argv[2]

# iperf3 -c 192.168.1.1 -P 1 -i 1 -p 5201 -f m -t 10
tcp = ["iperf3", "-c", ip,  # server address
       "-p", "5201",        # server port
       "-P", "1",           # parallel process
       "-i", "1",           # intervals
       "-f", "m",           # format output m = Mbits
       "-t", "10",          # experiment time (-n experiments bytes)
       "-l", "56.0K",       # buffer length
       "-w", "64.0K",       # tcp window size
       "-M", "1400B",       # max segment size
       "-N"]                # tcp no delay

# iperf3 -c 192.168.1.1 -u -P 1 -i 1 -p 5201 -f m -b 1.0M -t 10
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


def save_experiment(title, result, file):
    stars = "*"*15 + "\n"

    final_text = stars + title + stars + result + "\n"*3

    f = open(file, 'a')
    f.write(final_text)
    f.close()


def main():
    scenarios = []
    scenarios.append(tcp)
    scenarios.append(udp)

    counter = 0
    for scenario in scenarios:
        counter += 1
        title = str(scenario) + "\n"
        output = execute_scenario(scenario)

        print "Scenario " + str(counter) + " DONE"
        save_experiment(title, output, filename)


if __name__ == "__main__":
    main()
