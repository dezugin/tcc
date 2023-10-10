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

final_file = "/home/zezin/Documents/tcc/elusa/week3.jsonl"
with open(intermediate_file, 'r') as file, open(final_file, 'a') as outfile,open('count.txt', 'a') as countfile:
    for idx, line in enumerate(file):
        #if idx == 3:
        #    break
        data = json.loads(line)
        timestamp = data['tweet']['created_at']['$date']
        #print(timestamp)
#week1 = sep 26        if timestamp < 1475197200000 and timestamp > 1474592400000:
#week2 = oct 20        if timestamp < 1477184400000 and timestamp > 1476666000000:
        if timestamp < 1476234000000 and timestamp > 1475715600000:
            outfile.write(json.dumps(data) + '\n')
        countfile.write(str(idx)+"\n")  
        print(idx)