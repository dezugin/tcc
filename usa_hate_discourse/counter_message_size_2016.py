import json

count = 0
counterHillary = 0
counterTrump = 0
#unique_names = set()
train_file = "/home/zezin/Documents/tcc/elusa/tweets.jsonl"
with open(train_file, 'r') as file:
    for line in file:
        data = json.loads(line)

        trump = data['tweet']['semantics']['targeted']['trump']
        hillary = data['tweet']['semantics']['targeted']['hillary']
        #if count == 3:
        #    break
        if trump is not None and trump == True:
            counterTrump += 1
        if hillary is not None and hillary == True:
            counterHillary += 1
        count = count + 1
        print("linha ",count,", ",count/4334627,"%")

with open('trump_2016.txt', 'w') as file:
    file.write(str(counterTrump))
with open('hillary_2016.txt', 'w') as file:
    file.write(str(counterHillary))