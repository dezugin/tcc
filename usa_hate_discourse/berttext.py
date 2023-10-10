import json
from keybert import KeyBERT
from collections import defaultdict

# Initialize the KeyBERT model
kw_model = KeyBERT(model="distilbert-base-nli-mean-tokens")

# Create a defaultdict to count keyword occurrences
keywords_counter = defaultdict(int)

# Path to your jsonl file
file_path = "/home/zezin/Documents/tcc/elusa/week2.jsonl"
count = 0
# Loop through the JSONL file and extract keywords for each tweet's text
with open(file_path, 'r') as file:
    for line in file:
        print(count)
        #if count > 2:
        #S    break
        data = json.loads(line)
        text = data['tweet']['text']
        keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 1), top_n=5)
        for keyword, _ in keywords:
            keywords_counter[keyword] += 1
        count = count + 1

# Get the most frequent keywords
sorted_keywords = sorted(keywords_counter.items(), key=lambda x: x[1], reverse=True)
top_keywords = sorted_keywords[:100]

print("Top 100 keywords and their counts:")
for keyword, count in top_keywords:
    print(keyword, count)
week1_result_path = "/home/zezin/Documents/tcc/elusa/week2_result.txt"
with open(week1_result_path, 'a') as file:
    file.write("Top 100 keywords and their counts:\n")
    for keyword, count in top_keywords:
        file.write(keyword+ " "+ str(count)+"\n")  
