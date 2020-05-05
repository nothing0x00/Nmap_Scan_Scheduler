import schedule
import time
import subprocess
from termcolor import colored
import argparse
import os

parser = argparse.ArgumentParser(description = "Scheduler for nmap Scanning")
parser.add_argument("-t", "--targets", help="List of Targets")
parser.add_argument("-o", "--output", help="Output File Name")
parser.add_argument("-s", "--schedule", help="Time to Run Scan (Based on System Clock) Formatted As hour:minute")
args = parser.parse_args()
targets = args.targets
output = args.output
sched = args.schedule

if not os.geteuid() == 0:
    sys.exit("[!] Must Be Run As Root!")

print("-" * 20)
print(colored("[*] Starting nmap Scanning", "red", attrs=["bold"]))
print("-" * 20)
print("\n")
def nmap_test():
    cmdstr = "sudo nmap -sS -sV -A -O --script discovery -vv -p 1-65535 -oA {} -oN {}.txt -Pn -iL {}".format(output, output, targets)
    subprocess.call(cmdstr, shell=True)
    #print(cmdstr)

schedule.every().day.at(sched).do(nmap_test)

while True:
    schedule.run_pending()
    time.sleep(1)
