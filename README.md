## Nmap Scan Scheduler

During penetration tests we are often asked to only perform asset discovery during certain times of the day. Rather than staying up till all hours of the night, a far preferable approach is to schedule the scans to run at an appointed time.


This simple script allows a user to set a list of targets, the name of output files and the time of the scan into the commandline options in order to schedule nmap to run at the specified time. The way the script is structured the scan will run at the appointed time every day, but this loop can be exited simple by exiting the script.


While the scan is running the script will output the results to the screen, as well as writing results to a text file, xml file and gnmap file for ingestion into other tools. The nmap scans utilize pre-set options, which can be identified in the script and modified if the user would like.

The options for the script can be seen below:

```Scheduler for nmap Scanning

optional arguments:
  -h, --help            show this help message and exit
  -t TARGETS, --targets TARGETS
                        List of Targets
  -o OUTPUT, --output OUTPUT
                        Output File Name
  -s SCHEDULE, --schedule SCHEDULE
                        Time to Run Scan (Based on System Clock) Formatted As
                        hour:minute
```

### Installation and Use

To install the dependencies run the following:

`pip3 install -r requirements.txt`


After installing dependencies run the script with the following command:

`sudo python3 scan_sched.py -t [targets list] -o [output file names] -s [time to run scan]`

It is important to note that the time to run the scan is set based on the system clock for the machine running the script, with the time identified on a 24 hour time clock, rather than a 12 hour clock; eg 16:00 not 04:00 for 4PM.
