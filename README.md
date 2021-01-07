# design-tweets-analysis

An example of big-data analysis, using Twitter. The project provides the following functions:

- Data retrieval: retrieving 3000 Tweets about design, user experience, and art vs design, accessing Twitter API with [tweepy](http://www.tweepy.org/).

- Clean the collected tweets, using the Stanford Natural Language Toolkit ([NLTK](http://www.nltk.org/)) libraries, which provides these functions:

  1. stop word removal,
  2. word tokenization, and
  3. word stemming

- Sentiment analysis of the cleaned tweets, such as subjectivity and polarity.

- Further analysis using the [scikitlearn](https://scikit-learn.org/stable/) module:

  1. Text feature extraction with Term Frequency Inverse document frequency library ([TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html))
  2. Perform clustering, using the [K-Means](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) and [MiniBatchKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html) algorithms, ensuring to get and evaluate the 10 clusters documents. Additionally, perform the elbow method to visulize the appropriate number of clusers.

- Three different Visualizations of the collected tweets:
  1. Collected tweets visualization, using [wordCloud](https://pypi.org/project/wordcloud/)
  2. Visualisation of the tweets clustering analysis (elbow method)
  3. Visualisation of the tweets sentiment analysis

# Collection

The collector scripts allow defining a campaign to collect the tweets, using two classes:

- TweetStreamer: for handling the API authentication and establishing the connection.
- TwitterListener: takes the streamer as an argument and listen to the received tweets and saves them into a standard out file (fetched_tweets.text)

# Pre Processing

The preprocessing scripts modify the content of tweets, preparing them for further analysis. The process follows the steps:

1. combining a list of tweets into one large chunk of text,
2. performing two stages of cleaning,
   1. Stage 1: Make text lowercase, remove text in square brackets, punctuation, words containing numbers, URLs and regular expressions, hashtags.
   2. Stage 2: Remove any additional punctuation and non-sensical text that was missed in Stage 1 of the cleaning.
3. performing stop word removal,
4. performing word tokenization, and
5. performing word stemming

# Feature Extractor and KMean analysis

Before performing the clustering analysis, features (words) were extracted from the cleaned tweets. k = 10 was predicted when executing the KMeans algorithms; however, the result from the elbow method analysis shows the cluster that has a sharp decrease is at K = 4, so K at the cut-off point represent the best cluster.
