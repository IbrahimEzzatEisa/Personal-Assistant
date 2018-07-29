from nltk.corpus import WordNetCorpusReader
from nltk.corpus import wordnet as wn
import gui
gui.jsonify({'status':'OK','answer':'would you like try quick service ?if you want write yes and  quit to exit '})

print(wn.synsets('country'))

country = wn.synset('country.n.04')
types_of_country = country.hyponyms()
print(types_of_country,len(types_of_country))
# print(wn.synset('state.n.04').hyponyms())
print(wn.synset('country.n.02').hyponyms())
print(wn.synset('country.n.02').hypernym_paths())
print(wn.synset('country.n.02').root_hypernyms())
# sorted([lemma.name for synset in types_of_country for lemma in synset.lemmas])