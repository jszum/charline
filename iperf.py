import sys
import os
import datetime
import copy

class IperfScenario:
    def __init__(self):
        self.command = []
        self.desc = ""

    def set_scenario(self, com, desc):
        self.command = com
        self.desc = desc

    def get_command(self):
        return self.command

    def get_desc(self):
        return self.desc

ip = sys.argv[1]

option = sys.argv[2][-1:]

if option == "m":
	minutes = sys.argv[2][:-1]
	timer = str(int(minutes)*60)
else:
	timer = str(int(sys.argv[2]))

directory = str(datetime.datetime.now())[0:-7]
os.mkdir(directory, 0755)

bandwith = "1000.0M"
reporting_interval = "1"

test_cases = []

scen = IperfScenario()
scen.set_scenario(["iperf3", "-c", ip, "-p", "5201", "-P", "1", "-i", reporting_interval,
          "-f", "m", "-t", timer, "-M", "1500B", "-N"], "TCP, MTU = 1500B")
test_cases.append(copy.deepcopy(scen))

scen.set_scenario(["iperf3", "-c", ip, "-p", "5201", "-P", "1", "-i", reporting_interval,
          "-f", "m", "-t", timer, "-M", "750B", "-N"], "TCP, MTU = 750B")
test_cases.append(copy.deepcopy(scen))

scen.set_scenario(["iperf3", "-c", ip, "-p", "5201", "-P", "1", "-i", reporting_interval,
          "-f", "m", "-t", timer, "-M", "375B", "-N"], "TCP, MTU = 375B")
test_cases.append(copy.deepcopy(scen))

scen.set_scenario(["iperf3", "-c", ip, "-p", "5201", "-P", "1", "-i", reporting_interval,
          "-f", "m", "-t", timer, "-M", "187B", "-N"], "TCP, MTU = 187B")
test_cases.append(copy.deepcopy(scen))

scen.set_scenario(["iperf3", "-c", ip, "-p", "5201", "-P", "1", "-i", reporting_interval,
          "-f", "m", "-t", timer, "-w", "64.0K", "-M", "1500B", "-N"], "TCP, MTU = 1500B, window = 64.0K")
test_cases.append(copy.deepcopy(scen))

scen.set_scenario(["iperf3", "-c", ip, "-p", "5201", "-P", "1", "-i", reporting_interval,
          "-f", "m", "-t", timer, "-w", "32.0K", "-M", "1500B", "-N"], "TCP, MTU = 1500B, window = 32.0K")
test_cases.append(copy.deepcopy(scen))

scen.set_scenario(["iperf3", "-c", ip, "-p", "5201", "-P", "1", "-i", reporting_interval,
          "-f", "m", "-t", timer, "-w", "16.0K", "-M", "1500B", "-N"], "TCP, MTU = 1500B, window = 16.0K")
test_cases.append(copy.deepcopy(scen))

scen.set_scenario(["iperf3", "-c", ip, "-p", "5201", "-P", "1", "-i", reporting_interval,
          "-f", "m", "-t", timer, "-w", "8.0K", "-M", "1500B", "-N"], "TCP, MTU = 1500B, window = 8.0K")
test_cases.append(copy.deepcopy(scen))

scen.set_scenario(["iperf3", "-c", ip, "-p", "5201", "-u", "-P", "1", "-i", reporting_interval,
        "-f", "m", "-t", timer, "-l", "1500B", "-b", bandwith], "UDP, Packet (MTU) = 1500B")
test_cases.append(copy.deepcopy(scen))

scen.set_scenario(["iperf3", "-c", ip, "-p", "5201", "-u", "-P", "1", "-i", reporting_interval,
        "-f", "m", "-t", timer, "-l", "750B", "-b", bandwith], "UDP, Packet (MTU) = 750B")
test_cases.append(copy.deepcopy(scen))

scen.set_scenario(["iperf3", "-c", ip, "-p", "5201", "-u", "-P", "1", "-i", reporting_interval,
        "-f", "m", "-t", timer, "-l", "375B", "-b", bandwith], "UDP, Packet (MTU) = 375B")
test_cases.append(copy.deepcopy(scen))

scen.set_scenario(["iperf3", "-c", ip, "-p", "5201", "-u", "-P", "1", "-i", reporting_interval,
        "-f", "m", "-t", timer, "-l", "187B", "-b", bandwith], "UDP, Packet (MTU) = 187B")
test_cases.append(copy.deepcopy(scen))

scen.set_scenario(["iperf3", "-c", ip, "-p", "5201", "-u", "-P", "1", "-i", reporting_interval,
        "-f", "m", "-t", timer, "-w", "64.0K", "-l", "1500B", "-b", bandwith], "UDP, Packet (MTU) = 1500B, window = 64.0K")
test_cases.append(copy.deepcopy(scen))
scen.set_scenario(["iperf3", "-c", ip, "-p", "5201", "-u", "-P", "1", "-i", reporting_interval,
        "-f", "m", "-t", timer, "-w", "32.0K", "-l", "1500B", "-b", bandwith], "UDP, Packet (MTU) = 1500B, window = 32.0K")
test_cases.append(copy.deepcopy(scen))
scen.set_scenario(["iperf3", "-c", ip, "-p", "5201", "-u", "-P", "1", "-i", reporting_interval,
        "-f", "m", "-t", timer, "-w", "16.0K", "-l", "1500B", "-b", bandwith], "UDP, Packet (MTU) = 1500B, window = 16.0K")
test_cases.append(copy.deepcopy(scen))
scen.set_scenario(["iperf3", "-c", ip, "-p", "5201", "-u", "-P", "1", "-i", reporting_interval,
        "-f", "m", "-t", timer, "-w", "8.0K", "-l", "1500B", "-b", bandwith], "UDP, Packet (MTU) = 1500B, window = 8.0K")
test_cases.append(copy.deepcopy(scen))
