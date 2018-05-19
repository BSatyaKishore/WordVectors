import multiprocessing
from gensim.corpora.wikicorpus import WikiCorpus
from gensim.models.word2vec import Word2Vec

wiki = WikiCorpus('/Users/p345/WordVectors/0.Preprocessing/enwiki-latest-pages-articles.xml.bz2', 
                  lemmatize=False, dictionary={})
sentences = list(wiki.get_texts())
params = {'size': 200, 'window': 10, 'min_count': 10, 
          'workers': max(1, multiprocessing.cpu_count() - 1), 'sample': 1E-3,}
word2vec = Word2Vec(sentences, **params)

word2vec.save('en-model.m')
