import csv
import os
import time

#os.system("start /wait cmd /c /interactive")

currentmood = input("What's your current mood? ")
print("You said your current mood is" + " " + '"' + currentmood + '". ' 'Logging it.')
time.sleep(4)

#Write moodtowrite, time and date to new row

fields=[currentmood,time.strftime("%H:%M:%S"),time.strftime("%D")]
with open('CurrentMoodCSV.csv', 'a', newline = '') as moodcsv:
                writer = csv.writer(moodcsv)
                writer.writerow(fields)
