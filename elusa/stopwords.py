import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

languages = ['english','spanish']
all_stopwords = set()
for lang in languages:
    all_stopwords.update(set(stopwords.words(lang)))
def remove_url(text):
    url_pattern = r"http\S+|www\S+|rt\s|RT\s|amp\s|AMP\s"
    text = re.sub(url_pattern, '',text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.lower() not in all_stopwords and word.isalnum()]
    return ' '.join(tokens)
# Function to clean tweets

def clean_tweet(tweet):
    # Remove URLs
    tweet = tweet.lower()
    tweet = re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)
    
    # Lowercase the tweet
    
    
    # Remove mentions and hashtags
    tweet = re.sub(r'@\w+|#\w+', '', tweet)
    
    # Remove punctuations
    #tweet = re.sub(r'\p{P}+', '', tweet)
    
    # Tokenize the tweet
    tweet_tokens = word_tokenize(tweet)
    
    # Remove stopwords
    filtered_words = [word for word in tokens if word.lower() not in all_stopwords and word.isalnum()]
    
    return " ".join(filtered_words)

# Example usage
tweet = "Check out this cool link about #NLP: https://nlp.example.coma wesome @user"
cleaned_tweet = clean_tweet(tweet)
#cleaned_tweet = remove_url(tweet)
print(cleaned_tweet)