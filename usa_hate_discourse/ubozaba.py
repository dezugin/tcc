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

final_file = "/home/zezin/Documents/tcc/elusa/week.jsonl"
with open(intermediate_file, 'r') as file, open(final_file, 'a') as outfile,open('count.txt', 'a') as countfile:
    for idx, line in enumerate(file):
        #if idx == 3:
        #    break
        data = json.loads(line)
        timestamp = data['tweet']['created_at']['$date']
        #print(timestamp)
        if timestamp < 1475197200000 and timestamp > 1474592400000:
            outfile.write(json.dumps(data) + '\n')
        countfile.write(str(idx)+"\n")  
        print(idx)