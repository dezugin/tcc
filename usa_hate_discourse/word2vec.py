from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
import json

# Assume we have a list of sentences. For simplicity, let's use a dummy list.
sentences = [
    "This is a sample sentence",
    "Word2Vec is an interesting algorithm",
    "Bag of words is a common approach"
]

# Tokenize and preprocess the sentences
tokenized_sentences = [simple_preprocess(sentence) for sentence in sentences]

# Train the Word2Vec model
model = Word2Vec(sentences=tokenized_sentences, vector_size=100, window=5, min_count=1, workers=4)

# Now, let's convert the model's vocabulary and vectors into a JSONL format.
with open("word2vec.jsonl", "w") as file:
    for word in model.wv.index_to_key:
        vector = model.wv[word].tolist()  # Convert numpy array to list
        data = {"word": word, "vector": vector}
        file.write(json.dumps(data) + '\n')
