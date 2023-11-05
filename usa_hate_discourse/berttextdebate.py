import json
from keybert import KeyBERT
from collections import defaultdict

# Initialize the KeyBERT model
kw_model = KeyBERT(model="distilbert-base-nli-mean-tokens")

# Create a defaultdict to count keyword occurrences
keywords_counter = defaultdict(int)
keywords_counter_trump = defaultdict(int)
keywords_counter_clinton = defaultdict(int)

# Path to your jsonl file
file_path = "/home/zezin/Documents/tcc/usa_hate_discourse/week3debate.txt"
trump_path = "/home/zezin/Documents/tcc/usa_hate_discourse/week3debatetrump.txt"
clinton_path = "/home/zezin/Documents/tcc/usa_hate_discourse/week3debateclinton.txt"
count = 0
# Loop through the JSONL file and extract keywords for each tweet's text
with open(file_path, 'r') as file, open(trump_path, 'a') as trumpfile, open(clinton_path, 'a') as clintonfile:
    for line in file:
        print(count)
        #if count > 2:
        #    break
        text = line
        if "Trump:" in text:
            #trumpfile.write(line + '\n')
            text = text.replace('Trump:', '')
            keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 1), top_n=5)
            for keyword, _ in keywords:
                keywords_counter_trump[keyword] += 1
        if "Clinton:" in text:    
            #clintonfile.write(line + '\n')
            text = text.replace('Clinton:', '')
            keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 1), top_n=5)
            for keyword, _ in keywords:
                keywords_counter_clinton[keyword] += 1
        keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 1), top_n=5)
        for keyword, _ in keywords:
            keywords_counter[keyword] += 1
        count = count + 1

# Get the most frequent keywords
sorted_keywords = sorted(keywords_counter.items(), key=lambda x: x[1], reverse=True)
top_keywords = sorted_keywords[:100]
sorted_keywords_trump = sorted(keywords_counter_trump.items(), key=lambda x: x[1], reverse=True)
top_keywords_trump = sorted_keywords_trump[:100]
sorted_keywords_clinton = sorted(keywords_counter_clinton.items(), key=lambda x: x[1], reverse=True)
top_keywords_clinton = sorted_keywords_clinton[:100]

print("Top 100 keywords and their counts:")
for keyword, count in top_keywords:
    print(keyword, count)
for keyword, count in top_keywords_trump:
    print(keyword, count)
for keyword, count in top_keywords_clinton:
    print(keyword, count)
week1_result_path = "/home/zezin/Documents/tcc/elusa/week3debate_result.txt"
week1_result_path_trump = "/home/zezin/Documents/tcc/elusa/week3debate_result_trump.txt"
week1_result_path_clinton = "/home/zezin/Documents/tcc/elusa/week3debate_result_clinton.txt"
with open(week1_result_path, 'a') as file,open(week1_result_path_trump, 'a') as trumpfile,open(week1_result_path_clinton, 'a') as clintonfile:
    file.write("Top 100 keywords and their counts:\n")
    trumpfile.write("Top 100 keywords and their counts:\n")
    clintonfile.write("Top 100 keywords and their counts:\n")
    for keyword, count in top_keywords:
        file.write(keyword+ " "+ str(count)+"\n")  
    for keyword, count in top_keywords_trump:
        trumpfile.write(keyword+ " "+ str(count)+"\n")  
    for keyword, count in top_keywords_clinton:
        clintonfile.write(keyword+ " "+ str(count)+"\n")  
