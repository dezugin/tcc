import json

count = 0
counterBiden = 0
counterTrump = 0
#unique_names = set()
train_file = "/home/zezin/Documents/tcc/usa_hate_discourse/tweets.jsonl"
with open(train_file, 'r') as file:
    for line in file:
        data = json.loads(line)
        text = data['tweet']['text']
        text = text.lower()
        if "@realdonaldtrump" in text:
            counterTrump += 1
        if "@joebiden" in text:
            counterBiden += 1
        #if count == 3:
            #break
        
        if "@realdonaldtrump" in text or "@joebiden" in text:
            with open('2020_mention.jsonl', 'a') as file:
                file.write(line)   
            with open('trump_2020.txt', 'a') as file:
                file.write(str(counterTrump)+"\n")
            with open('biden_2020.txt', 'a') as file:
                file.write(str(counterBiden)+"\n")
        count = count + 1
        print(count)
        

