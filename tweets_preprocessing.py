# libraries
import json
import re
import string

import nltk
nltk.download()
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk import PorterStemmer


class TweetsPreprocesser():
    '''
    Class for preprocessing the tweets 
    '''

    def __init__(self):
        self.tweets = []

    # Gets the Tweets content
    def get_tweets_content(self):
        with open('fetched_tweets.txt', 'r') as f:
            for line in f:
                tweet = json.loads(line)
                self.tweets.append(tweet["text"])
        f.close()
        return self.tweets

    # combine texts into one text
    def combine_text(self, list_of_text):
      '''
      Takes a list of tweets text and combines them into one large chunk of text.
      '''
      return ' '.join(list_of_text)

    # Apply a first round of cleaning
    def clean_text_round1(self, text):
        '''
        Make text lowercase, remove text in square brackets, punctuation, words containing numbers, URLs and regular expressions, hashtags.
        '''
        text = text.lower()
        text = re.sub('\[.*?\]', '', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub('\w*\d\w*', '', text)  # Removing  numbers
        text = re.sub('([^0-9A-Za-z \t])|(\w+:\/\/\S+)', '',
                      text)  # Removing regular expressions and hyperlinks
        text = re.sub('#', '', text)  # Removing '#' hash tag
        text = re.sub('RT[\s]+', '', text)  # Removing RT
        return text

    # Apply a second round of cleaning
    def clean_text_round2(self, text):
        '''
        Get rid of some additional punctuation and non-sensical text that was missed the first time around.
        '''
        text = re.sub('[‘’“”…]', '', text)
        text = re.sub('\n', '', text)
        text = re.sub('  ', '', text)
        return text

    def preprocess_text_nltk(self, text):
        '''
        Use nltk library to preprocess the text of tweets, 
        1) stop word removal, 
        2) word tokenization, and
        3) word stemming
        '''
        stop_words = set(stopwords.words('english'))
        # Apply tokenization
        word_tokens = nltk.word_tokenize(text)
        filtered_txt = [word for word in text if word not in stop_words]
        filtered_txt = []
        # remove stop words in tokenizated text
        for w in word_tokens:
            if w not in stop_words:
                filtered_txt.append(w)
        # Apply Stemming
        ps = nltk.PorterStemmer()
        steemed_txt = [ps.stem(word) for word in filtered_txt]
        return steemed_txt

    # Main function for preprocessing the combined_tweets
    def main(self):

        # Fetch tweets from file then combine them into one text(array)
        tweets = self.get_tweets_content()
        combined_tweets = self.combine_text(tweets)

        # cleaning the text
        round1 = self.clean_text_round1(combined_tweets)
        round2 = self.clean_text_round2(round1)

        # start preprocessing the tweets
        preprocessed_text = self.preprocess_text_nltk(round2)
        return preprocessed_text
