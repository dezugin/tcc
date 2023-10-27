import json
import pandas as pd
import plotly.express as px
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
from datetime import datetime
import os
from sklearn.feature_extraction.text import CountVectorizer


vectorizer_model = CountVectorizer(stop_words="english")
sentence_model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
topic_model = BERTopic(embedding_model=sentence_model, 
                        low_memory=True,
                        calculate_probabilities=False, 
                        top_n_words=20, 
                        nr_topics="auto",
                        vectorizer_model=vectorizer_model)

# Stream data and process it incrementally
file_path = '/home/zezin/Documents/tcc/elusa/week.jsonl'
output_file = "/home/zezin/Documents/tcc/elusa/week.csv"
model_file = '/home/zezin/Documents/tcc/elusa/week_model'
#topic_model = BERTopic.load(model_file)
batch_size = 522
documents = []
dates = []
count = 0
pathexists = False
if os.path.exists(output_file):
    pathexists = True
len_file = 0
final_counter = 1758509 - 524
#with open(file_path, 'r') as file:
#    len_file = num_lines = sum(1 for _ in file)
#    final_counter = len_file - 524
with open(file_path, 'r') as f, open('/home/zezin/Documents/tcc/elusa/counter.txt','a') as countfile:
    batch_counter = 0
    for line in f:
        #if count <= final_counter: #1565663#1456565: #10000:#200003:#522: #
        #    count += 1
        #    print (count)
        #    continue
        print (count)
        countfile.write((str(count))+'\n')
        tweet = json.loads(line)
        documents.append(tweet['tweet']['text'])
        tweet_date = datetime.utcfromtimestamp(tweet['tweet']['created_at']['$date'] / 1000).strftime('%Y-%m-%d')
        dates.append(tweet_date)
        batch_counter += 1
        count = count + 1
        if batch_counter >= batch_size:
            topics, _ = topic_model.fit_transform(documents)
            documents = []  # Clear the batch
            batch_counter = 0
            a = {'date': dates, 'topic_n': topics}
            df = pd.DataFrame.from_dict(a, orient='index')
            df = df.transpose()
            counted_df = df.groupby(['date', 'topic_n']).size().reset_index(name='counts')
            if pathexists:
                existing_df = pd.read_csv(output_file)
                merged_df = pd.merge(existing_df, counted_df, on=['date', 'topic_n'], how='outer').fillna(0)
                merged_df['counts'] = merged_df['counts_x'] + merged_df['counts_y']
                merged_df = merged_df.drop(columns=['counts_x', 'counts_y'])
    
            else:
                merged_df = counted_df
            topic_model.save(model_file)
            merged_df.to_csv(output_file, index=False)



df = pd.read_csv(output_file)
topic_name_mapping = {topic_num: ", ".join([word for word, _ in words]) for topic_num, words in topic_model.get_topics().items()}
df['topic'] = df['topic_n'].map(topic_name_mapping)


#grouped = df.groupby(['date', 'topic']).size().reset_index(name='counts')

# Plot the results using Plotly
fig = px.bar(df, x='date', y='counts', color='topic', title="Number of Tweets per Topic over a Week")
fig.write_html("/home/zezin/Documents/tcc/elusa/week.html")
fig.show()
