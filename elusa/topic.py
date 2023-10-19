import json
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import CountVectorizer


vectorizer_model = CountVectorizer(stop_words="english")
sentence_model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
topic_model = BERTopic(embedding_model=sentence_model, 
                        calculate_probabilities=False, 
                        top_n_words=20, 
                        nr_topics="auto",
                        vectorizer_model=vectorizer_model)

# Prepare data
documents = []
file_path = "/home/zezin/Documents/tcc/elusa/week1p2.jsonl"
count = 0
batch_size = 1000
min_batch = 500
load = False
final_load = False
len_file = 0
final_counter = 0
with open(file_path, 'r') as file:
    len_file = num_lines = sum(1 for _ in file)
    final_counter = len_file - 999
# Extract text data from JSONL file
with open(file_path, 'r') as file, open('/home/zezin/Documents/tcc/elusa/counter.txt','a') as countfile:
    batch_counter = 0
    for line in file:
        print (count)
        countfile.write((str(count))+'\n')
        ##if count > 2000:
         ##   break
        """if count < final_counter:#1759035: #1758999:
            load = True
            count += 1
            continue
        if load:
            topic_model = BERTopic.load("/home/zezin/Documents/tcc/elusa/week_model")
            load = False
"""
        data = json.loads(line)
        text = data['tweet']['text']
        documents.append(text)
        count = count + 1
        batch_counter += 1

        if batch_counter >= batch_size:
            topics, _ = topic_model.fit_transform(documents)
            documents = []  # Clear the batch
            batch_counter = 0  # Reset the counter
            topic_model.save("/home/zezin/Documents/tcc/elusa/week1p2_model")
    if documents and len(documents) > min_batch:
       ### print("len=",len(documents))
        topics, _ = topic_model.fit_transform(documents)        


# Visualize topics
fig = topic_model.visualize_topics()
fig.write_html("/home/zezin/Documents/tcc/elusa/week1p2.html")
fig = topic_model.visualize_barchart()
fig.write_html("/home/zezin/Documents/tcc/elusa/week1p2bar.html")
fig.show()
fig = topic_model.visualize_heatmap()
fig.write_html("/home/zezin/Documents/tcc/elusa/week1p2heat.html")