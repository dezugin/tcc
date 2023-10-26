import json
import pandas as pd
import plotly.express as px
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
from datetime import datetime

from sklearn.feature_extraction.text import CountVectorizer


vectorizer_model = CountVectorizer(stop_words="english")
sentence_model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
topic_model = BERTopic(embedding_model=sentence_model, 
                        calculate_probabilities=False, 
                        top_n_words=20, 
                        nr_topics="auto",
                        vectorizer_model=vectorizer_model)

# Stream data and process it incrementally
file_path = '/home/zezin/Documents/tcc/elusa/week.jsonl'
output_file = "/home/zezin/Documents/tcc/elusa/week.csv"
batch_size = 100000
documents = []
dates = []
min_batch = 80000
count = 0
all_batches = []
with open(file_path, 'r') as f, open('/home/zezin/Documents/tcc/elusa/counter.txt','a') as countfile:
    batch_counter = 0
    for line in f:
        print (count)
        if count >= 200003:#522: #
            break
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
            a = {'date': dates, 'topic': topics}
            df = pd.DataFrame.from_dict(a, orient='index')
            df = df.transpose()
            all_batches.append(df)
            topic_model.save("/home/zezin/Documents/tcc/elusa/week_model")
            df.to_csv(output_file, mode='a', header=header, index=False)
    if documents and len(documents) > min_batch:
        topics, _ = topic_model.fit_transform(documents)
        topic_model.save("/home/zezin/Documents/tcc/elusa/week_model")
        a = {'date': dates, 'topic': topics}
        df = pd.DataFrame.from_dict(a, orient='index')
        df = df.transpose()
        all_batches.append(df)
        df.to_csv(output_file, mode='a', header=header, index=False)

# Create a dataframe with dates and topics
df = pd.concat(all_batches, ignore_index=True)

# Filter to keep only dates for a week
#df = df[df['date'].between('start_date', 'end_date')]  # replace with your dates

# Group by day and topic and count the number of tweets
grouped = df.groupby(['date', 'topic']).size().reset_index(name='counts')

# Plot the results using Plotly
fig = px.bar(grouped, x='date', y='counts', color='topic', title="Number of Tweets per Topic over a Week")
fig.show()
