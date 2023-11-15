import json
import pandas as pd
import plotly.express as px
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
from datetime import datetime
import os
from sklearn.feature_extraction.text import CountVectorizer
import seaborn as sns
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from bertopic.representation import MaximalMarginalRelevance
representation_model = MaximalMarginalRelevance(diversity=0.2)
from bertopic.vectorizers import ClassTfidfTransformer
from hdbscan import HDBSCAN
hdbscan_model = HDBSCAN(min_cluster_size=150, metric='euclidean', cluster_selection_method='eom', prediction_data=True)
ctfidf_model = ClassTfidfTransformer(reduce_frequent_words=True)
vectorizer_model = CountVectorizer(stop_words="english")
sentence_model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
topic_model = BERTopic(embedding_model=sentence_model, 
                        low_memory=True,
                        calculate_probabilities=False, 
                        top_n_words=20, 
                        nr_topics="auto",
                        representation_model=representation_model,
                        ctfidf_model=ctfidf_model,
                        n_gram_range=(1,4),
                        min_topic_size=20,
                        #vectorizer_model=vectorizer_model
                        )

# Stream data and process it incrementally
file_path1 = "/home/zezin/Documents/tcc/elusa/week2d1.jsonl"
file_path2 = "/home/zezin/Documents/tcc/elusa/week2d2.jsonl"
file_path3 = "/home/zezin/Documents/tcc/elusa/week2d3.jsonl"
file_path4 = "/home/zezin/Documents/tcc/elusa/week2d4.jsonl"
file_path5 = "/home/zezin/Documents/tcc/elusa/week2d5.jsonl"
file_path6 = "/home/zezin/Documents/tcc/elusa/week2d6.jsonl"
file_path7 = "/home/zezin/Documents/tcc/elusa/week2d7.jsonl"
output_file = "/home/zezin/Documents/tcc/elusa/week2.csv"
model_file = '/home/zezin/Documents/tcc/elusa/week2_model'
map_file = '/home/zezin/Documents/tcc/elusa/topic_mapping2.txt'
week_html = "/home/zezin/Documents/tcc/elusa/week2.html"
#topic_model = BERTopic.load(model_file)
batch_size = 522
documents = []
dates = []
count = 0
len_file = 0
nltk.download('stopwords')
#nltk.download('punkt')
languages = ['english','spanish']
all_stopwords = set()
for lang in languages:
    all_stopwords.update(set(stopwords.words(lang)))
def remove_url(tweet):
    tweet = tweet.lower()
    tweet = re.sub(r"http\S+|www\S+|rt\s|amp\s|(@[A-Za-z0-9]+)", '', tweet, flags=re.MULTILINE)
    #tweet = re.sub(r"http\S+|www\S+|rt\s", '', tweet, flags=re.MULTILINE)
    tweet_tokens = word_tokenize(tweet)
    filtered_words = [word for word in tweet_tokens if word.lower() not in all_stopwords and word.isalnum()]
    
    return " ".join(filtered_words)
  #  return tweet
final_counter =100000

with open(file_path1, 'r') as f, open('/home/zezin/Documents/tcc/elusa/counter.txt','a') as countfile:
    batch_counter = 0
    for line in f:
        if count >= final_counter:#1565663#1456565: #10000:#200003:#522: #
            break
        #    count += 1
        #    print (count)
        #    continue
        
        print ('kk'+str(count))
        countfile.write((str(count))+'\n')
        tweet = json.loads(line)
        text = tweet['tweet']['text']
        cleaned_text = remove_url(text)
        print("raw:"+text)
        print("cleaned:"+cleaned_text)
        documents.append(cleaned_text)
        tweet_date = datetime.utcfromtimestamp(tweet['tweet']['created_at']['$date'] / 1000).strftime('%Y-%m-%d')
        #print(tweet_date)
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
topic_name_mapping = {topic_num: ", ".join([word for word, _ in words]) for topic_num, words in topic_model.get_topics().items()}
print(topic_name_mapping)
with open(map_file, 'w') as f:
    f.write(str(topic_name_mapping))
"""
count = 0
with open(file_path1, 'r') as f, open('/home/zezin/Documents/tcc/elusa/counter.txt','a') as countfile:
    batch_counter = 0
    for line in f:
        #if count <= final_counter:#1565663#1456565: #10000:#200003:#522: #
        #    count += 1
        #   print (count)
        #    continue
        
        print ('a'+str(count))
        countfile.write((str(count))+'\n')
        tweet = json.loads(line)
        text = tweet['tweet']['text']
        cleaned_text = remove_url(text)
        documents.append(cleaned_text)
        tweet_date = datetime.utcfromtimestamp(tweet['tweet']['created_at']['$date'] / 1000).strftime('%Y-%m-%d')
        #print(tweet_date)
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

dates = []
count = 0
with open(file_path2, 'r') as f, open('/home/zezin/Documents/tcc/elusa/counter.txt','a') as countfile:
    batch_counter = 0
    for line in f:
        #if count <= final_counter: #1565663#1456565: #10000:#200003:#522: #
        #    count += 1
        #    print (count)
        #    continue
        print ('b'+str(count))
        countfile.write((str(count))+'\n')
        tweet = json.loads(line)
        text = tweet['tweet']['text']
        cleaned_text = remove_url(text)
        documents.append(cleaned_text)
        tweet_date = datetime.utcfromtimestamp(tweet['tweet']['created_at']['$date'] / 1000).strftime('%Y-%m-%d')
        #print(tweet_date)
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
            
dates = []
count = 0
with open(file_path3, 'r') as f, open('/home/zezin/Documents/tcc/elusa/counter.txt','a') as countfile:
    batch_counter = 0
    for line in f:
        #if count <= final_counter: #1565663#1456565: #10000:#200003:#522: #
        #    count += 1
        #    print (count)
        #    continue
        print ('c'+str(count))
        countfile.write((str(count))+'\n')
        tweet = json.loads(line)
        text = tweet['tweet']['text']
        cleaned_text = remove_url(text)
        documents.append(cleaned_text)
        tweet_date = datetime.utcfromtimestamp(tweet['tweet']['created_at']['$date'] / 1000).strftime('%Y-%m-%d')
        #print(tweet_date)
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
topic_name_mapping = {topic_num: ", ".join([word for word, _ in words]) for topic_num, words in topic_model.get_topics().items()} 
with open(map_file, 'w') as f:
    f.write(str(topic_name_mapping))       
dates = []
count = 0
with open(file_path4, 'r') as f, open('/home/zezin/Documents/tcc/elusa/counter.txt','a') as countfile:
    batch_counter = 0
    for line in f:
        #if count <= final_counter: #1565663#1456565: #10000:#200003:#522: #
        #    count += 1
        #    print (count)
        #    continue
        print ('d'+str(count))
        countfile.write((str(count))+'\n')
        tweet = json.loads(line)
        text = tweet['tweet']['text']
        cleaned_text = remove_url(text)
        documents.append(cleaned_text)
        tweet_date = datetime.utcfromtimestamp(tweet['tweet']['created_at']['$date'] / 1000).strftime('%Y-%m-%d')
        #print(tweet_date)
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
            
dates = []
count = 0
with open(file_path5, 'r') as f, open('/home/zezin/Documents/tcc/elusa/counter.txt','a') as countfile:
    batch_counter = 0
    for line in f:
        #if count <= final_counter: #1565663#1456565: #10000:#200003:#522: #
        #    count += 1
        #    print (count)
        #    continue
        print ('e'+str(count))
        countfile.write((str(count))+'\n')
        tweet = json.loads(line)
        text = tweet['tweet']['text']
        cleaned_text = remove_url(text)
        documents.append(cleaned_text)
        tweet_date = datetime.utcfromtimestamp(tweet['tweet']['created_at']['$date'] / 1000).strftime('%Y-%m-%d')
        #print(tweet_date)
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
dates = []
count = 0
#final_counter = 121172
with open(file_path6, 'r') as f, open('/home/zezin/Documents/tcc/elusa/counter.txt','a') as countfile:
    batch_counter = 0
    for line in f:
        print ('f'+str(count))
        countfile.write((str(count))+'\n')
        tweet = json.loads(line)
        text = tweet['tweet']['text']
        cleaned_text = remove_url(text)
        documents.append(cleaned_text)
        tweet_date = datetime.utcfromtimestamp(tweet['tweet']['created_at']['$date'] / 1000).strftime('%Y-%m-%d')
        #print(tweet_date)
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
            
dates = []
count = 0
with open(file_path7, 'r') as f, open('/home/zezin/Documents/tcc/elusa/counter.txt','a') as countfile:
    batch_counter = 0
    for line in f:
        #if count <= final_counter: #1565663#1456565: #10000:#200003:#522: #
        #    count += 1
        #    print (count)
        #    continue
        print ('g'+str(count))
        countfile.write((str(count))+'\n')
        tweet = json.loads(line)
        text = tweet['tweet']['text']
        cleaned_text = remove_url(text)
        documents.append(cleaned_text)
        tweet_date = datetime.utcfromtimestamp(tweet['tweet']['created_at']['$date'] / 1000).strftime('%Y-%m-%d')
        #print(tweet_date)
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
"""
df = pd.read_csv(output_file)
topic_name_mapping = {topic_num: ", ".join([word for word, _ in words]) for topic_num, words in topic_model.get_topics().items()}
df['topic'] = df['topic_n'].map(topic_name_mapping)


#grouped = df.groupby(['date', 'topic']).size().reset_index(name='counts')

# Plot the results using Plotly
fig = px.bar(df, x='date', y='counts', color='topic', title="Number of Tweets per Topic over a Week")
fig.write_html(week_html)
fig.show()

print(topic_name_mapping)
with open(map_file, 'w') as f:
    f.write(str(topic_name_mapping))

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

sums = df.groupby('topic_n')['counts'].sum().reset_index()
sums['date'] = 'All Days'


plt.figure(figsize=(15, 10))
sns.barplot(data=sums, x='date', y='counts', hue='topic_n', ci=None)

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

def create_wordcloud(model, topic):
    text = {word: value for word, value in model.get_topic(topic)}
    wc = WordCloud(background_color="white", max_words=1000)
    wc.generate_from_frequencies(text)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
for topic_num in sorted(topic_model.get_topics().keys()):
    create_wordcloud(topic_model, topic=topic_num)