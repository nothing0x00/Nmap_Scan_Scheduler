import schedule
import time
import subprocess
from termcolor import colored
import argparse
import os
import datetime

parser = argparse.ArgumentParser(description = "Scheduler for nmap Scanning")
parser.add_argument("-t", "--targets", help="List of Targets")
parser.add_argument("-o", "--output", help="Output File Name")
parser.add_argument("-s", "--schedule", help="Time to Run Scan (Based on System Clock) Formatted As hour:minute")
parser.add_argument("--tcp", help="Basic TCP Scan of Common Ports")
parser.add_argument("--tcpall", help="Full TCP Port Scan with Discovery NSE Scripts")
parser.add_argument("--udp", help="Basic UDP Scan")
parser.add_argument("--udpall", help="Full UDP Port Scan")

args = parser.parse_args()
targets = args.targets
output = args.output
sched = args.schedule
tcp = args.tcp
tcp_all = args.tcpall
udp = args.udp
udp_all = args.udpall

if not os.geteuid() == 0:
    sys.exit("[!] Must Be Run As Root!")

now = datetime.datetime.now()
output_date = output.strftime("%d_%m_%Y")
print("-" * 20)
print(colored("[*] Starting nmap Scanning", "red", attrs=["bold"]))
print("-" * 20)
print("\n")
def nmap_test():
    if tcp:
        cmdstr = "sudo nmap -sS -sV -vv -oA {} -oN {}.txt -Pn -iL {}".format(output_date, output_date, targets)
    if tcp_all:
        cmdstr = "sudo nmap -sS -sV -A -O --script discovery -vv -p 1-65535 -oA {} -oN {}.txt -Pn -iL {}".format(output_date, output_date, targets)
    if udp:
        cmdstr = "sudo nmap -sU -sV -vv -oA {} -oN {}.txt -Pn -iL {}".format(output_date, output_date, targets)
    if udp_all:
        cmdstr = "sudo nmap -sU -sV -A -O --script discovery -vv -p 1-65535 -oA {} -oN {}.txt -Pn -iL {}".format(output_date, output_date, targets)
    subprocess.call(cmdstr, shell=True)

schedule.every().day.at(sched).do(nmap_test)

while True:
    schedule.run_pending()
    time.sleep(1)
