import json
from sentistrength import PySentiStr
import pandas as pd
from sklearn.cluster import KMeans
from pyclustering.cluster import xmeans
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer
senti = PySentiStr()
senti.setSentiStrengthPath('/home/zezin/SentiStrength.jar')
senti.setSentiStrengthLanguageFolderPath('/home/zezin/SentiStrength_Data/')

count = 0

intermediate_file = "/home/zezin/Documents/tcc/elusa/tweets.jsonl"

final_file = "/home/zezin/Documents/tcc/elusa/week1p1.jsonl"
final_file2 = "/home/zezin/Documents/tcc/elusa/week1p2.jsonl"
final_file3 = "/home/zezin/Documents/tcc/elusa/week1p3.jsonl"

with open(intermediate_file, 'r') as file, open(final_file, 'a') as outfile, open(final_file2, 'a') as outfile2, open(final_file3, 'a') as outfile3,open('count.txt', 'a') as countfile:
    for idx, line in enumerate(file):
        #if idx == 3:
        #    break
        data = json.loads(line)
        timestamp = data['tweet']['created_at']['$date']
        #print(timestamp)
        if timestamp < 1474858800000 and timestamp > 1474599600000:#week 1#1 23-09/26-09 3am 
            outfile.write(json.dumps(data) + '\n')
        if timestamp < 1474945200000 and timestamp > 1474858800000:#week 1#2 26-09/27-09 3am 
            outfile2.write(json.dumps(data) + '\n')
        if timestamp < 1475204400000 and timestamp > 1474945200000:#week 1#3 27-09/30-09 3am 
            outfile3.write(json.dumps(data) + '\n')
        countfile.write(str(idx)+"\n")  
        print(idx)