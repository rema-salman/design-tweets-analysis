# import class from file
from tweets_preprocessing import TweetsPreprocesser

# import libraries
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import MiniBatchKMeans, KMeans


class TweetsClustering():
    '''
    Class for tweets clustering analysis, using KMeans and Mini-Batch KMeans algorithms.
    Apply an evaluation of the clustering by performing text-clustering
    Apply elbow method for getting the appropriate clusters number, then 
        returning the result to be visualized
    '''

    def __init__(self):
        self.vec = TfidfVectorizer(stop_words='english', use_idf=True)
        self.k = 10

    def feature_extraction(self, documents):
        self.vec.fit(documents)  # tokenize and build vocab
        features = self.vec.transform(documents)  # encode document
        # summarize encoded vector
        print(features.shape)
        print(features.toarray())
        return features

    def clustering_miniBatchKMeans(self, scaled_features):
        # perform the mini batch K-means and fit on the whole data
        mbk = MiniBatchKMeans(
            n_clusters=self.k, random_state=True).fit(scaled_features)
        # mbk.lables
        # mbk.predict(scaled_features)
        return mbk

    def clustering_KMeans(self, scaled_features):
        # perform the K-means and fit on the scaled documents
        km = KMeans(
            n_clusters=self.k, random_state=True).fit(scaled_features)
        return km

    def clustering_evaluation(self, mbk):
        # perform text clustering
        sorted_centroids = mbk.cluster_centers_.argsort()[:, ::-1]
        terms = self.vec.get_feature_names()
        for i in range(self.k):
            print("cluster %d:" % i, end='')
            for x in sorted_centroids[i, :5]:
                print("%s " % terms[x], end='')
            print()
            print()
        print()
        # can be extended to cover topic models and coherent values of semantics

    def get_appropriate_clusters_num(self, scaled_features):
        kmeans_kwargs = {
            "init": "random",
            "n_init": 10,
            "max_iter": 300,
            "random_state": 42,
        }
        # A list holds the SSE values for each k
        sse = []
        for k in range(1, 11):
            kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
            kmeans.fit(scaled_features)
            sse.append(kmeans.inertia_)
        return sse


    def main(self):
        # Getting preprocessed data and extract the documents
        preprocesser = TweetsPreprocesser()
        preprocessed_tweets = preprocesser.main()
        extracted_features = self.feature_extraction(preprocessed_tweets)
        
        mbk = self.clustering_miniBatchKMeans(extracted_features)
        km = self.clustering_KMeans(extracted_features)
        
        # Perform clustering evaluation for mini batch K-means and K-means algorithms 
        self.clustering_evaluation(mbk)
        self.clustering_evaluation(km)

        sse = self.get_appropriate_clusters_num(extracted_features)
        return sse
