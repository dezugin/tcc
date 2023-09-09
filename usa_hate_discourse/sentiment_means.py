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
        if "trump" in text:
            counterTrump += 1
        if "biden" in text:
            counterBiden += 1
        #if count == 200:
        #    break
        
        if "trump" in text or "biden" in text:
            with open('2020_extensive_mention.jsonl', 'a') as file:
                file.write(line)   
            with open('trump_extensive_2020.txt', 'a') as file:
                file.write(str(counterTrump)+"\n")
            with open('biden_extensive_2020.txt', 'a') as file:
                file.write(str(counterBiden)+"\n")
            #print(line)
        count = count + 1
        print(count)
        with open('count.txt', 'a') as file:
            file.write(str(count)+"\n")  
        

