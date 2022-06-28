# Marathi Reviews and Opinion Analysis using NLP

import nltk
import io

 
# opening positive datset
pos_data = io.open("pos_marathi.txt",'r',encoding='utf-8')

# opening negative dataset
neg_data =  io.open("neg_marathi.txt",'r',encoding='utf-8')

# merging the two datasets into a single list of tuples
text_samples = []
sentiment = "positive"
for words in pos_data.readlines():
    words_filtered = [i.lower() for i in words.split() if len(i) >= 3] 
    text_samples.append((words_filtered, sentiment))

sentiment = "negative"
for words in neg_data.readlines():
    words_filtered = [i.lower() for i in words.split() if len(i) >= 3] 
    text_samples.append((words_filtered, sentiment))



# term frequencies of data set



def term_freq(data):
    all_words = []
    for (words, sentiment) in data:
      all_words.extend(words)
    word_list_freq = nltk.FreqDist(all_words)
    word_freqDist = word_list_freq.keys()
    return word_freqDist

word_features = term_freq(text_samples)


# building a feature function for training
def feature_function(text):
    text_words = set(text)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in text_words)
    return features

training_set = nltk.classify.apply_features(feature_function, text_samples)

# training the classifier 
classifier = nltk.NaiveBayesClassifier.train(training_set)

def classify_text(text):
	return classifier.classify(feature_function(text.split()))