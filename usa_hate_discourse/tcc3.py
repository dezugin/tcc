import json
from datetime import datetime
count = 0
train_file = "/home/zezin/Documents/tcc/usa_hate_discourse/tweets.jsonl"
with open(train_file, 'r') as file:
    for line in file:
        #if count < 64999:
        #    count = count + 1
        #    continue
        try: 
            count = count + 1
            if count < 202532715:
                continue
            data = json.loads(line)
            #print(data)
            name = data['tweet']['user']['username']
            text = data['tweet']['text']
            #datetime.fromtimestamp(int(str(data['tweet']['created_at']['$date'])[:-3]))
            date = str(data['tweet']['created_at']['$date'])[:-3]
            #pro_trump = data['tweet']['semantics']['is_political_for_trump']
            #pro_hillary = data['tweet']['semantics']['is_political_for_hillary']
            #mention_trump = data['tweet']['semantics']['targeted']['trump']
            #mention_hillary = data['tweet']['semantics']['targeted']['hillary']
            
            tweet = {'username': name, 'date': date, 'text':text}
            print(count)
            print(date)
            
            with open('tweets_2020_trimmed.jsonl', 'a') as file:
                file.write(json.dumps(tweet)+"\n")
        except:
            count = count + 1
            data = json.loads(line)
            name = data['tweet']['user']['username']
            text = data['tweet']['text']
            date_string = data['tweet']['created_at']
            format_string = "%a %b %d %H:%M:%S %z %Y"
            dt = datetime.strptime(date_string, format_string)
            date = str(int(dt.timestamp()))
            tweet = {'username': name, 'date': date, 'text':text}
            print(count)
            
            with open('tweets_2020_trimmed.jsonl', 'a') as file:
                file.write(json.dumps(tweet)+"\n")
            
            
            continue