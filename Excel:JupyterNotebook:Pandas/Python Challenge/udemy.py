import os
import csv

udemy_csv = os.path.join("..","HW_Task2_UdemyZip","web_starter.csv")

title = []
price = []
subscribers = []
reviews = []
length = []

with open(udemy_csv, encoding = 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # loop through
    for row in csvreader:
        
        title.append(row[1])
        price.append(row[4])
        subscribers.append(float(row[5]))
        reviews.append(float(row[6]))
        length.append(row[9])
        
        #remove hours so number is left
        length = [i.split(' ', 1)[0] for i in length]
        #divide list review by subscribers
        percent_reviewed = [i / j *100 for i, j in zip(reviews, subscribers)]
        #round percent
        percent_reviewed = [round(x, 2) for x in percent_reviewed]

zipped_data = zip(title, price, subscribers, reviews, percent_reviewed, length) 

output_file = os.path.join("udemy_summary.csv")

with open(output_file, "w", newline='') as datafile:
        writer = csv.writer(datafile)
        
        writer.writerow(["Title","Price","Subscribers","Reviews","Percent Reviewed","Length"])
        writer.writerows(zipped_data)