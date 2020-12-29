# from tweets_preprocessing import get_preprocessed_data
# from tweets_clustering import tweets_processing
from nltk.corpus import stopwords

from wordcloud import WordCloud
import matplotlib.pyplot as plt


class DataVisualization():
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def visualize_tweets(self, preprocess_tweets):
        tweets = ' '.join(preprocess_tweets)  #convert list to string
        wordcloud = WordCloud(
            width=800,
            height=500,
            random_state=21,
            max_font_size=110,
            background_color='white',
            stopwords=self.stop_words).generate(tweets)
        wordcloud.to_file("img/tweets_wordcloud.png")
        plt.figure(figsize=(10, 7))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

    def visualize_tweets_clustering(self, sse):
        plt.style.use('fivethirtyeight')
        plt.figure(figsize=(13, 10))
        plt.plot(range(1, 11), sse)
        plt.xticks(range(1, 11))
        plt.xlabel('Number of Clusters')
        plt.ylabel('SSE')
        plt.savefig('img/tweets_clustering.png')
        plt.show()

    def visualize_sentiment_analysis(self, polarity, subjectivity):
        plt.figure(figsize=(13, 10))
        for i in range(len(polarity)):
            plt.scatter(polarity[i], subjectivity[i], color='Blue')
        plt.xlabel('Polarity')
        plt.ylabel('Subjectivity')
        plt.title('Sentiment Analysis')
        plt.savefig('img/sentiment_analysis.png')
        plt.show()
