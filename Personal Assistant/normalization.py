# from nltk.stem import WordNetLemmatizer
from nltk import WordNetLemmatizer
from nltk.stem import SnowballStemmer
# from nltk.stem.snowball import EnglishStemmer
import nltk
class Normalizer:

    def __init__(self):
        self.engStem = None
        self.snLem = None
        self.snStem = None
        self.wnLem=None

    def normlize(self,text):
        # WordNetLemmatizer.lemmatize(text)

        self.engStem = SnowballStemmer("english")
        self.snStem = self.engStem.stem(text)
        tokens=nltk.word_tokenize(text)
        wnl = nltk.WordNetLemmatizer()
        x=[wnl.lemmatize(t) for t in tokens]


        return x

    def snowBallStemmer(self,text):


        stems = None
        stemmer = SnowballStemmer("english")
        token = stemmer.stem(text)
        stems = token
        return stems



        # tokens = nltk.WhitespaceTokenizer().tokenize(text)
        # stems = []
        # stemmer = SnowballStemmer("english")
        # for token in tokens:
        #     token = stemmer.stem(token)
        #     if token != "":
        #         stems.append(token)
        # return stems






# print(Normalizer().snowBallStemmer("i wanna finding weather in egypt")[2])