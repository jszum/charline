#!/usr/bin/python

from subprocess import Popen, PIPE
import sys

ip = sys.argv[1]
filename = sys.argv[2]

#mtu to be measured
# mtu1 = "1500B"
# mtu2 = "750B"
# mtu3 = "375B"
# mtu4 = "187B"

#then mtu=1500 and...
# window1 = "64.0K"
# window2 = "32.0K"
# window3 = "16.0K"
# window4 = "8.0K"

# bytes = 1M - 100K
# time = ~10min

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

String size = "10M"

tcp = []
tcp.append(["iperf3", "-c", ip, "-p", "5201", "-P", "1", "-i", "1",
          "-f", "m", "-n", size, "-M", "1500B", "-N"])
tcp.append(["iperf3", "-c", ip, "-p", "5201", "-P", "1", "-i", "1",
          "-f", "m", "-n", size, "-M", "750B", "-N"])
tcp.append(["iperf3", "-c", ip, "-p", "5201", "-P", "1", "-i", "1",
          "-f", "m", "-n", size, "-M", "375B", "-N"])
tcp.append(["iperf3", "-c", ip, "-p", "5201", "-P", "1", "-i", "1",
          "-f", "m", "-n", size, "-M", "187B", "-N"])

tcp.append(["iperf3", "-c", ip, "-p", "5201", "-P", "1", "-i", "1",
          "-f", "m", "-n", size, "-w", "64.0K", "-M", "1500B", "-N"])
tcp.append(["iperf3", "-c", ip, "-p", "5201", "-P", "1", "-i", "1",
          "-f", "m", "-n", size, "-w", "32.0K", "-M", "1500B", "-N"])
tcp.append(["iperf3", "-c", ip, "-p", "5201", "-P", "1", "-i", "1",
          "-f", "m", "-n", size, "-w", "16.0K", "-M", "1500B", "-N"])
tcp.append(["iperf3", "-c", ip, "-p", "5201", "-P", "1", "-i", "1",
          "-f", "m", "-n", size, "-w", "8.0K", "-M", "1500B", "-N"])


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
    for element in tcp:
        scenarios_array.append(element)

    for element in udp:
        scenarios_array.append(element)


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
