import json
import pandas as pd
import plotly.express as px
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
from datetime import datetime
import os
from sklearn.feature_extraction.text import CountVectorizer
import seaborn as sns
import matplotlib.pyplot as plt

vectorizer_model = CountVectorizer(stop_words="english")
sentence_model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
topic_model = BERTopic(embedding_model=sentence_model, 
                        low_memory=True,
                        calculate_probabilities=False, 
                        top_n_words=20, 
                        nr_topics="auto",
                        vectorizer_model=vectorizer_model)

# Stream data and process it incrementally
file_path = "/home/zezin/Documents/tcc/elusa/week1d1.jsonl"
file_path2 = "/home/zezin/Documents/tcc/elusa/week1d2.jsonl"
file_path3 = "/home/zezin/Documents/tcc/elusa/week1d3.jsonl"
file_path4 = "/home/zezin/Documents/tcc/elusa/week1d4.jsonl"
file_path5 = "/home/zezin/Documents/tcc/elusa/week1d5.jsonl"
file_path6 = "/home/zezin/Documents/tcc/elusa/week1d6.jsonl"
file_path7 = "/home/zezin/Documents/tcc/elusa/week1d7.jsonl"
output_file = "/home/zezin/Documents/tcc/elusa/week.csv"
model_file = '/home/zezin/Documents/tcc/elusa/week_model'
#topic_model = BERTopic.load(model_file)
batch_size = 522
documents = []
dates = []
count = 0
len_file = 0
with open(file_path, 'r') as f, open('/home/zezin/Documents/tcc/elusa/counter.txt','a') as countfile:
    batch_counter = 0
    for line in f:
        #if count <= final_counter: #1565663#1456565: #10000:#200003:#522: #
        #    count += 1
        #    print (count)
        #    continue
        print ('a'+count)
        countfile.write((str(count))+'\n')
        tweet = json.loads(line)
        documents.append(tweet['tweet']['text'])
        tweet_date = datetime.utcfromtimestamp(tweet['tweet']['created_at']['$date'] / 1000).strftime('%Y-%m-%d')
        print(tweet_date)
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
            existing_df = pd.read_csv(output_file)
            merged_df = pd.merge(existing_df, counted_df, on=['date', 'topic_n'], how='outer').fillna(0)
            merged_df['counts'] = merged_df['counts_x'] + merged_df['counts_y']
            merged_df = merged_df.drop(columns=['counts_x', 'counts_y'])
            topic_model.save(model_file)
            merged_df.to_csv(output_file, index=False)
with open(file_path1, 'r') as f, open('/home/zezin/Documents/tcc/elusa/counter.txt','a') as countfile:
    batch_counter = 0
    for line in f:
        #if count <= final_counter: #1565663#1456565: #10000:#200003:#522: #
        #    count += 1
        #    print (count)
        #    continue
        print ('b'+count)
        countfile.write((str(count))+'\n')
        tweet = json.loads(line)
        documents.append(tweet['tweet']['text'])
        tweet_date = datetime.utcfromtimestamp(tweet['tweet']['created_at']['$date'] / 1000).strftime('%Y-%m-%d')
        print(tweet_date)
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
            existing_df = pd.read_csv(output_file)
            merged_df = pd.merge(existing_df, counted_df, on=['date', 'topic_n'], how='outer').fillna(0)
            merged_df['counts'] = merged_df['counts_x'] + merged_df['counts_y']
            merged_df = merged_df.drop(columns=['counts_x', 'counts_y'])
            topic_model.save(model_file)
            merged_df.to_csv(output_file, index=False)

with open(file_path2, 'r') as f, open('/home/zezin/Documents/tcc/elusa/counter.txt','a') as countfile:
    batch_counter = 0
    for line in f:
        #if count <= final_counter: #1565663#1456565: #10000:#200003:#522: #
        #    count += 1
        #    print (count)
        #    continue
        print ('c'+count)
        countfile.write((str(count))+'\n')
        tweet = json.loads(line)
        documents.append(tweet['tweet']['text'])
        tweet_date = datetime.utcfromtimestamp(tweet['tweet']['created_at']['$date'] / 1000).strftime('%Y-%m-%d')
        print(tweet_date)
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
            existing_df = pd.read_csv(output_file)
            merged_df = pd.merge(existing_df, counted_df, on=['date', 'topic_n'], how='outer').fillna(0)
            merged_df['counts'] = merged_df['counts_x'] + merged_df['counts_y']
            merged_df = merged_df.drop(columns=['counts_x', 'counts_y'])
            topic_model.save(model_file)
            merged_df.to_csv(output_file, index=False)

with open(file_path3, 'r') as f, open('/home/zezin/Documents/tcc/elusa/counter.txt','a') as countfile:
    batch_counter = 0
    for line in f:
        #if count <= final_counter: #1565663#1456565: #10000:#200003:#522: #
        #    count += 1
        #    print (count)
        #    continue
        print ('d'+count)
        countfile.write((str(count))+'\n')
        tweet = json.loads(line)
        documents.append(tweet['tweet']['text'])
        tweet_date = datetime.utcfromtimestamp(tweet['tweet']['created_at']['$date'] / 1000).strftime('%Y-%m-%d')
        print(tweet_date)
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
            existing_df = pd.read_csv(output_file)
            merged_df = pd.merge(existing_df, counted_df, on=['date', 'topic_n'], how='outer').fillna(0)
            merged_df['counts'] = merged_df['counts_x'] + merged_df['counts_y']
            merged_df = merged_df.drop(columns=['counts_x', 'counts_y'])
            topic_model.save(model_file)
            merged_df.to_csv(output_file, index=False)

with open(file_path4, 'r') as f, open('/home/zezin/Documents/tcc/elusa/counter.txt','a') as countfile:
    batch_counter = 0
    for line in f:
        #if count <= final_counter: #1565663#1456565: #10000:#200003:#522: #
        #    count += 1
        #    print (count)
        #    continue
        print ('e'+count)
        countfile.write((str(count))+'\n')
        tweet = json.loads(line)
        documents.append(tweet['tweet']['text'])
        tweet_date = datetime.utcfromtimestamp(tweet['tweet']['created_at']['$date'] / 1000).strftime('%Y-%m-%d')
        print(tweet_date)
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
            existing_df = pd.read_csv(output_file)
            merged_df = pd.merge(existing_df, counted_df, on=['date', 'topic_n'], how='outer').fillna(0)
            merged_df['counts'] = merged_df['counts_x'] + merged_df['counts_y']
            merged_df = merged_df.drop(columns=['counts_x', 'counts_y'])
            topic_model.save(model_file)
            merged_df.to_csv(output_file, index=False)

with open(file_path5, 'r') as f, open('/home/zezin/Documents/tcc/elusa/counter.txt','a') as countfile:
    batch_counter = 0
    for line in f:
        #if count <= final_counter: #1565663#1456565: #10000:#200003:#522: #
        #    count += 1
        #    print (count)
        #    continue
        print ('e'+count)
        countfile.write((str(count))+'\n')
        tweet = json.loads(line)
        documents.append(tweet['tweet']['text'])
        tweet_date = datetime.utcfromtimestamp(tweet['tweet']['created_at']['$date'] / 1000).strftime('%Y-%m-%d')
        print(tweet_date)
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
            existing_df = pd.read_csv(output_file)
            merged_df = pd.merge(existing_df, counted_df, on=['date', 'topic_n'], how='outer').fillna(0)
            merged_df['counts'] = merged_df['counts_x'] + merged_df['counts_y']
            merged_df = merged_df.drop(columns=['counts_x', 'counts_y'])
            topic_model.save(model_file)
            merged_df.to_csv(output_file, index=False)

with open(file_path6, 'r') as f, open('/home/zezin/Documents/tcc/elusa/counter.txt','a') as countfile:
    batch_counter = 0
    for line in f:
        #if count <= final_counter: #1565663#1456565: #10000:#200003:#522: #
        #    count += 1
        #    print (count)
        #    continue
        print ('f'+count)
        countfile.write((str(count))+'\n')
        tweet = json.loads(line)
        documents.append(tweet['tweet']['text'])
        tweet_date = datetime.utcfromtimestamp(tweet['tweet']['created_at']['$date'] / 1000).strftime('%Y-%m-%d')
        print(tweet_date)
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
            existing_df = pd.read_csv(output_file)
            merged_df = pd.merge(existing_df, counted_df, on=['date', 'topic_n'], how='outer').fillna(0)
            merged_df['counts'] = merged_df['counts_x'] + merged_df['counts_y']
            merged_df = merged_df.drop(columns=['counts_x', 'counts_y'])
            topic_model.save(model_file)
            merged_df.to_csv(output_file, index=False)

with open(file_path7, 'r') as f, open('/home/zezin/Documents/tcc/elusa/counter.txt','a') as countfile:
    batch_counter = 0
    for line in f:
        #if count <= final_counter: #1565663#1456565: #10000:#200003:#522: #
        #    count += 1
        #    print (count)
        #    continue
        print ('g'+count)
        countfile.write((str(count))+'\n')
        tweet = json.loads(line)
        documents.append(tweet['tweet']['text'])
        tweet_date = datetime.utcfromtimestamp(tweet['tweet']['created_at']['$date'] / 1000).strftime('%Y-%m-%d')
        print(tweet_date)
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
            existing_df = pd.read_csv(output_file)
            merged_df = pd.merge(existing_df, counted_df, on=['date', 'topic_n'], how='outer').fillna(0)
            merged_df['counts'] = merged_df['counts_x'] + merged_df['counts_y']
            merged_df = merged_df.drop(columns=['counts_x', 'counts_y'])
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


sums = df.groupby('topic')['counts'].sum().reset_index()
sums['date'] = 'All Days'
df = pd.concat([df, sums], ignore_index=True)
plt.figure(figsize=(15, 10))
sns.barplot(data=df, x='date', y='counts', hue='topic_n', ci=None)

# Set the title and labels
plt.title('Number of Tweets per Topic per Day')
plt.xlabel('Date')
plt.ylabel('Number of Tweets')
plt.legend(title='Topics', bbox_to_anchor=(1.05, 1), loc='upper left')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust the layout
plt.tight_layout()

# Show the plot
plt.show()