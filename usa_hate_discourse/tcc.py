import json

count = 0
counter = 0
unique_names = set()
train_file = "/home/zezin/Documents/tcc/elusa/tweets.jsonl"
with open(train_file, 'r') as file:
    for line in file:
        data = json.loads(line)

        name = data['tweet']['user']['username']
        
        #if count == 3:
        #    break
        if name is not None and name not in unique_names:
            unique_names.add(name)
            counter += 1
        count = count + 1
print(unique_names)
print(counter)

with open('users_2016.txt', 'w') as file:
    file.write(str(counter))