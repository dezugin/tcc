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
intermediate_file = "/home/zezin/Documents/tcc/usa_hate_discourse/2020_sentiment_analysis.jsonl"
with open(train_file, 'r') as file, open(intermediate_file, 'a') as outfile,open('count.txt', 'a') as countfile:
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
        feature_targetTrump = 0
        feature_targetBiden = 0
        feature_mentionTrump = 0
        feature_mentionBiden = 0
        feature_proTrump = 0
        feature_proBiden = 0
        if '@realdonaldtrump' in text:
            targetTrump = True
            feature_targetTrump = 1
        if '@joebiden' in text:
            targetBiden = True
            feature_targetBiden = 1
        if 'biden' in text:
            mentionBiden = True
            feature_mentionTrump = 1
            if sentiment > 0:
                proBiden = True
                feature_proBiden = 1
            if sentiment < 0:
                proTrump = True
                feature_proTrump = 0
        if 'trump' in text:
            mentionTrump = True
            feature_mentionBiden = 1
            if sentiment > 0:
                proTrump = True
                feature_proTrump = 0
            if sentiment < 0:
                proBiden = True
                feature_proBiden = 1

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
        features = {
            "overall_sentiment":sentiment,
            "target_trump":feature_targetTrump,
            "target_biden":feature_targetBiden,
            "mention_trump":feature_mentionTrump,
            "mention_biden":feature_mentionBiden,
            "pro_trump":feature_proTrump,
            "pro_biden":feature_proBiden,
            "count_usernames":len(at_words)
            }
        data['sentiment_analysis'] = sentiment_analysis
        outfile.write(json.dumps(data)+'\n')
        features_list.append(features)
        count = count + 1
        print(count)
        countfile.write(str(count)+"\n")  

df = pd.DataFrame(features_list)
kmeans = KMeans(n_clusters=2, random_state=0).fit(df)
clusters = kmeans.labels_
final_file = "/home/zezin/Documents/tcc/usa_hate_discourse/2020_extensive_mention_clustered.jsonl"
with open(intermediate_file, 'r') as file, open(final_file, 'a') as outfile,open('count.txt', 'a') as countfile:
    for idx, line in enumerate(file):
        if idx == 3:
            break
        data = json.loads(line)
        data['cluster'] = int(clusters[idx])
        outfile.write(json.dumps(data) + '\n')
        countfile.write(str(idx)+"\n")  
        print(idx)