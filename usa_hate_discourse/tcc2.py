import json
from datetime import datetime
count = 0
train_file = "/home/zezin/Documents/tcc/elusa/tweets.jsonl"
with open(train_file, 'r') as file:
    for line in file:
        data = json.loads(line)

        name = data['tweet']['user']['username']
        text = data['tweet']['text']
        #datetime.fromtimestamp(int(str(data['tweet']['created_at']['$date'])[:-3]))
        date = data['tweet']['created_at']['$date']
        pro_trump = data['tweet']['semantics']['is_political_for_trump']
        pro_hillary = data['tweet']['semantics']['is_political_for_hillary']
        mention_trump = data['tweet']['semantics']['targeted']['trump']
        mention_hillary = data['tweet']['semantics']['targeted']['hillary']
        #if count == 3:
        #    break
        tweet = {'username': name, 'date': date, 'text':text,"trump":pro_trump, "hillary":pro_hillary, 'mention_trump': mention_trump, 'mention_hillary':mention_hillary}
        #print(tweet)
        count = count + 1
        with open('tweets_2016_trimmed.jsonl', 'a') as file:
            file.write(json.dumps(tweet)+"\n")