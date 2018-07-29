import nltk
from nltk.tokenize import RegexpTokenizer
class Tokenizer:
    def __init__(self):
        pass

    def tokenize(self,text):
       pattern=r'''(?x)([A-Z]\.)+
       |\w+(-\w+)*
       |\$?\d+(\.\d+)?%?
       |\.\.\.
       | [][.,;"'?():-_`]'''

       tokens=nltk.tokenize.word_tokenize(text)
       # regexTokens=nltk.regexp_tokenize(text,pattern)
       return tokens

class regexTokenizer:
    def __init(self):
        pass

    def regexTokenize(self,text):
       pattern=RegexpTokenizer(r'''(?x)
       ([A-Z]\.)+
       |\w+(-\w+)*
       |\$?\d+(\.\d+)?%?
       |\.\.\.
       | [][.,;"'?():-_`]''')
       #'That U.S.A. poster-print costs $12.40...'
       pattern.tokenize(text)