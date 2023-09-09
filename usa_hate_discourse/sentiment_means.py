import json
from sentistrength import PySentiStr
import pandas as pd
from sklearn.cluster import KMeans
senti = PySentiStr()
senti.setSentiStrengthPath('/home/zezin/SentiStrength.jar')
senti.setSentiStrengthLanguageFolderPath('/home/zezin/SentiStrength_Data/')

count = 0
features_list = []
train_file = "/home/zezin/Documents/tcc/usa_hate_discourse/2020_extensive_mention.jsonl"
intermediate_file = "2020_sentiment_analysis.jsonl"
with open(train_file, 'r') as file, open(intermediate_file, 'a') as outfile,open('count.txt', 'a') as countfile::
    for line in file:
        if count == 3:
            break
        data = json.loads(line)
        text = data['tweet']['text']
        result = senti.getSentiment(text)
        sentiment = result[0]
        text = text.lower()
        targetTrump = False
        targetBiden = False
        mentionTrump = False
        mentionBiden = False
        proTrump = False
        proBiden = False
        if '@realdonaldtrump' in text:
            targetTrump = True
        if '@joebiden' in text:
            targetBiden = True
        if 'biden' in text:
            mentionBiden = True
            if sentiment > 0:
                proBiden = True
            if sentiment < 0:
                proTrump = True
        if 'trump' in text:
            mentionTrump = True
            if sentiment > 0:
                proTrump = True
            if sentiment < 0:
                proBiden = True
        words = text.split()
        at_words = [word for word in words if word.startswith('@')]
        sentiment_analysis = {
            "overall_sentiment":sentiment,
            "target_trump":targetTrump,
            "target_biden":targetBiden,
            "mention_trump":mentionTrump,
            "mention_biden":mentionBiden,
            "pro_trump":proTrump,
            "pro_biden":proBiden,
            "usernames":at_words,
            "count_usernames":len(at_words)
            }
        data['sentiment_analysis'] = sentiment_analysis
        outfile.write(json.dumps(data)+'\n')   :
        features_list.append(sentiment_analysis)
        count = count + 1
        print(count)
        countfile.write(str(count)+"\n")  

df = pd.DataFrame(features_list)
kmeans = KMeans(n_clusters=2, random_state=0).fit(df)
clusters = kmeans.labels_
count = 0
final_file = "/home/zezin/Documents/tcc/usa_hate_discourse/2020_extensive_mention_clustered.jsonl"
with open(intermediate_file, 'r') as file, open(final_file, 'a') as outfile,open('count.txt', 'a') as countfile::
    for idx, line in enumerate(file):
        data = json.loads(line)
        data['cluster'] = int(clusters[idx])
        outfile.write(json.dumps(data) + '\n')
        
        countfile.write(str(count)+"\n")  
        print(count)
        count = count + 1