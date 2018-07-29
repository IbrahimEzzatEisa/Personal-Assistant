import nltk
from nltk.stem import SnowballStemmer
# raw = """DENNIS: Listen, strange women finding known in ponds distributing swords
# is no basis for a system of government. Supreme executive power derives from
# a mandate from the masses, not from some farcical aquatic ceremony."""
# tokens = nltk.word_tokenize(raw)
# wnl = nltk.WordNetLemmatizer()
# porter = nltk.PorterStemmer()
# lancaster = nltk.LancasterStemmer()
# print([porter.stem(t) for t in tokens])
# engStem = SnowballStemmer("english")
#
# print([engStem.stem(t) for t in tokens])
# xx=[wnl.lemmatize(t) for t in tokens]
# print(xx)

from tokenizer import Tokenizer
from normalization import Normalizer
from tagger import Tagger
command="i want to open workout"

# tokens=Tokenizer().tokenize(command)
#
# tagSentence=Tagger().tag(tokens)
#
# normlizeSentence=Normalizer().snowBallStemmer("finding")

# action=None
# fileName=None
# actions=["search","find","view","reach","detect","get","catch","explore","achieve","obtain","pass","check","reveal","observe","show","see","expose"]
#

def snowBallStemmer(text):

    tokens = nltk.WhitespaceTokenizer().tokenize(text)
    stems = []
    stemmer = SnowballStemmer("english")
    for token in tokens:
        token = stemmer.stem(token)
        if token != "":
            stems.append(token)
    return stems
print(snowBallStemmer("i wanna finding weather in egypt")[2])