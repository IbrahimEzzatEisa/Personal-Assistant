import nltk
from nltk.corpus import brown
from nltk.corpus import PlaintextCorpusReader
from cPickle import dump,load
from tokenizer import Tokenizer

class Tagger:
    def tag(self,text):
        brown_tagged_sents = brown.tagged_sents(categories='news')
        brown_sents = brown.sents(categories='news')
        size = int(len(brown_tagged_sents) * 0.9)
        train_sents = brown_tagged_sents[:size]
        test_sents = brown_tagged_sents[size:]
        t0 = nltk.DefaultTagger('NN')
        t1 = nltk.UnigramTagger(train_sents, backoff=t0)
        t2 = nltk.BigramTagger(train_sents, backoff=t1)
        t3 = nltk.UnigramTagger(train_sents, backoff=t2)
        createfile = open('t3.pkl','wb')  # we create file it's extension is pickle file to serialized  and unserialized data with binary format
        dump(t3, createfile, -1)  # here file created and insert training data
        createfile.close()
        loadfile = open('t3.pkl', 'rb')
        tagger = load(loadfile)#tag sentence by our sentaence
        loadfile.close()
        # taggedSen=tagger.tag(Tokenizer().tokenize(text))
        taggedSen = tagger.tag(text)
        return taggedSen


# x=Tagger().tag(nltk.tokenize.word_tokenize('i need to view dsfn'))
# print(x)
