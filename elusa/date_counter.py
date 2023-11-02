import json
import csv
from collections import Counter
import pandas as pd
from datetime import datetime
# Path to your jsonl file
file_path = 'path_to_your_file.jsonl'
file_path1 = "/home/zezin/Documents/tcc/elusa/week2d1.jsonl"
file_path2 = "/home/zezin/Documents/tcc/elusa/week2d2.jsonl"
file_path3 = "/home/zezin/Documents/tcc/elusa/week2d3.jsonl"
file_path4 = "/home/zezin/Documents/tcc/elusa/week2d4.jsonl"
file_path5 = "/home/zezin/Documents/tcc/elusa/week2d5.jsonl"
file_path6 = "/home/zezin/Documents/tcc/elusa/week2d6.jsonl"
file_path7 = "/home/zezin/Documents/tcc/elusa/week2d7.jsonl"

csv_output_path = 'dates_count.csv'

# Counter to store the occurrences of each date
date_counter = Counter()
"""
# Count dates from the jsonl file
with open(file_path1, 'r') as f:
    for line in f:
        tweet = json.loads(line)
        date = tweet['tweet']['created_at']['$date']  # Extract the date
        date = date  # Extracting only the YYYY-MM-DD part
        date_counter[date] += 1
        
with open(file_path2, 'r') as f:
    for line in f:
        tweet = json.loads(line)
        date = tweet['tweet']['created_at']['$date']  # Extract the date
        date = date  # Extracting only the YYYY-MM-DD part
        date_counter[date] += 1
        
with open(file_path3, 'r') as f:
    for line in f:
        tweet = json.loads(line)
        date = tweet['tweet']['created_at']['$date']  # Extract the date
        date = date  # Extracting only the YYYY-MM-DD part
        date_counter[date] += 1
        
with open(file_path4, 'r') as f:
    for line in f:
        tweet = json.loads(line)
        date = tweet['tweet']['created_at']['$date']  # Extract the date
        date = date  # Extracting only the YYYY-MM-DD part
        date_counter[date] += 1
        
with open(file_path5, 'r') as f:
    for line in f:
        tweet = json.loads(line)
        date = tweet['tweet']['created_at']['$date']  # Extract the date
        date = date  # Extracting only the YYYY-MM-DD part
        date_counter[date] += 1
        
with open(file_path6, 'r') as f:
    for line in f:
        tweet = json.loads(line)
        date = tweet['tweet']['created_at']['$date']  # Extract the date
        date = date  # Extracting only the YYYY-MM-DD part
        date_counter[date] += 1
        
with open(file_path7, 'r') as f:
    for line in f:
        tweet = json.loads(line)
        date = tweet['tweet']['created_at']['$date']  # Extract the date
        date = date  # Extracting only the YYYY-MM-DD part
        date_counter[date] += 1
        

# Save to CSV
with open(csv_output_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Date", "Count"])  # Writing header
    for date, count in date_counter.items():
        writer.writerow([datetime.utcfromtimestamp(date/ 1000).strftime('%Y-%m-%d'), count])
"""
df = pd.read_csv(csv_output_path)
grouped = df.groupby('Date').sum().reset_index()
for index, row in grouped.iterrows():
    print(f"Date: {row['Date']}, Sum: {row['Count']}")