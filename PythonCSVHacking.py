"""Working on learning how to interact with a csv via Python.
"""

import csv
import time

moodtowrite = "medium"
#moodtime = time.strftime("%H:%M:%S")

"""
#setup the csv with headers
csvwriterobject = csv.writer(open("CurrentMoodCSV.csv", "w"))

csvwriterobject.writerow(["Current Mood","Time","Date"])
"""

"""

with open('CurrentMoodCSV.csv', 'w') as mycsvfile:
    thedatawriter = csv.writer(mycsvfile, dialect='excel')
    thedatawriter.writerow(moodtowrite)
"""


#Write moodtowrite, time and date to new row

fields=[moodtowrite,time.strftime("%H:%M:%S"),time.strftime("%D")]
with open('CurrentMoodCSV.csv', 'a', newline = '') as moodcsv:
                writer = csv.writer(moodcsv)
                writer.writerow(fields)


#thedatawriter.writerow(moodtowrite,time.strftime("%H:%M:%S"))
"""

Homework: Implement this next Time. It will append.

import csv
fields=['first','second','third']
with open(r'name', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(fields)


Open function and what the different flags (a, w, etc) mean https://docs.python.org/3/library/functions.html#open
"""
