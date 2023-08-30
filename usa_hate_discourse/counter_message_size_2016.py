import json

count = 0
counterHillary = 0
counterTrump = 0
#unique_names = set()
total_tweets = 2705408
total_chars = 317805325
total_words = 45483931
stahp = 2704822
train_file = "/home/zezin/Documents/tcc/elusa/tweets.jsonl"
with open(train_file, 'r') as file:
    for line in file:
        if count <= stahp:
            count = count + 1
            continue
        data = json.loads(line)
        text = data['tweet']['text']
        chars = len(text)
        words = len(text.split())
        total_chars += chars
        total_words += words
        total_tweets += 1
        with open('2016_tweets.txt', 'a') as file:
            file.write(str(total_tweets)+"\n")   
        with open('2016_words.txt', 'a') as file:
            file.write(str(total_words)+"\n")
        with open('2016_chars.txt', 'a') as file:
            file.write(str(total_chars)+"\n")
        #if count == 3:
         #   break
        
        
        count = count + 1
        print(count)
        
avg_chars = total_chars / total_tweets if total_tweets > 0 else 0
avg_words = total_words / total_tweets if total_tweets > 0 else 0
print(f"Total number of tweets: {total_tweets}")
print(f"Total character count: {total_chars}")
print(f"Average characters per tweet: {avg_chars:.2f}")
print(f"Total word count: {total_words}")
print(f"Average words per tweet: {avg_words:.2f}")
with open('message_size_2016.txt', 'w') as file:
    file.write(f"Total number of tweets: {total_tweets}"+"\n")
    file.write(f"Total character count: {total_chars}"+"\n")
    file.write(f"Average characters per tweet: {avg_chars:.2f}"+"\n")
    file.write(f"Total word count: {total_words}"+"\n")
    file.write(f"Average words per tweet: {avg_words:.2f}"+"\n")