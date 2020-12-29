# class from the files
from tweets_preprocessing import TweetsPreprocesser
# Import textblob
from textblob import TextBlob


class TweetAnalyzer():
    """
    Class for Sentiment analysis of tweets content, such subjectivity and polarity.
    """

    # can be extended to further sentiment analysis like counting the positive negative tweets etc.

    def __init__(self):
        self.tweets = []
        self.subjectivity = []
        self.polarity = []
        self.cleaned_tweet1 = []

    def get_clean_tweets(self):
        preprocesser = TweetsPreprocesser()
        # Get the tweets content
        self.tweets = preprocesser.get_tweets_content()  # Clean the tweets
        for tweet in self.tweets:
            self.cleaned_tweet1.append(preprocesser.clean_text_round1(tweet))
        return self.cleaned_tweet1

    #function to get the subjectivity of the text returns: an array of subjectivity score for each tweet
    def getSubjectivity(self, text):
        for x in text:
            self.subjectivity.append(TextBlob(x).sentiment.subjectivity)
        return self.subjectivity

    #function to get the polarity of the text returns: an array of polarity score for each tweet
    def getPolarity(self, text):
        for x in text:
            self.polarity.append(TextBlob(x).sentiment.polarity)
        return self.polarity
