#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 22:48:59 2019

@author: Manny
"""

# -*- coding: UTF-8 -*-
"""Employee Email Script.
​
This module allows us to create an email address using employee data from
a csv file.
​
Example:
    $ python employee_email.py
​
"""
import os
import csv
import pandas as pd
​
filepath = os.path.join(".","Resources", "employees.csv")
​
new_employee_data = []
email = []
first_name=[]
last_name=[]
ssn=[]
​
# Read data into dictionary and create a new email field
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        person_email = (row['first_name'] + "." + row['last_name'] + "@example.com")
        email.append(person_email)
        first_name.append(row['first_name'])
        last_name.append(row['last_name'])
        ssn.append(row['ssn'])
​
#Combine lists to df
​
df = pd.DataFrame(
    {"First Name": first_name,
     "Last Name": last_name,
     "Email": email,
     "SSN":ssn
     }
)
df
​
# Write updated data to csv file
df.to_csv("new_employee_data.csv",index=False,header=True)