# Import classes from files
from tweets_collection import TwitterStreamer
from tweets_visualization import DataVisualization
from tweets_clustering import TweetsClustering
from tweets_preprocessing import TweetsPreprocesser
from tweets_analysis import TweetAnalyzer

# Executions of functions
if __name__ == "__main__":

    # Create an instance of the classes
    streamer = TwitterStreamer()
    preprocesser = TweetsPreprocesser()
    dv = DataVisualization()
    analyzer = TweetAnalyzer()
    dc = TweetsClustering()

    #Tweets Collection
    streamer.main()

    # Tweets Cleaning
    preprocessed_tweets = preprocesser.main()

    # Tweets Sentiment Analysis
    cleaned_tweets = analyzer.get_clean_tweets()
    polarity = analyzer.getPolarity(cleaned_tweets)
    subjectivity = analyzer.getSubjectivity(cleaned_tweets)

    # Tweets clustering analysis
    sse = dc.main()

    # Tweets Visualization: Visualize the collected tweets and their clustering and sentiment analysis
    dv.visualize_tweets(preprocessed_tweets)
    dv.visualize_tweets_clustering(sse)
    dv.visualize_sentiment_analysis(polarity, subjectivity)
