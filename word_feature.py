# This API is used for calculating tf-idf by sklearn, and extracting key words

import sys
import jieba.analyse
import jieba.posseg as pseg
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from stanfordcorenlp import StanfordCoreNLP
from knight.Info import Info

class TfidfAPI(object):
    def __init__(self, data):
        self.data = data    # data must be list which is composed of strings, strings must be tokenized
        information = Info()

    def keyWords_Extract(self, topK, select='tfidf', withWeight=False):
        if select == 'tfidf':
            return self.tfidf_Extract(topK, withWeight)
        elif select == 'textrank':
            return self.textRank_Extract(topK, withWeight)

    def tfidf_Extract(self, topK, withWeight=False):
        jieba.analyse.set_stop_words('stopwords.txt')
        data_temp = ' '.join(self.data)
        keyWords_list = jieba.analyse.extract_tags(data_temp, topK=topK, withWeight=withWeight)
        return keyWords_list

    def textRank_Extract(self, topK, withWeight=False):
        jieba.analyse.set_stop_words('stopwords.txt')
        data_temp = ' '.join(self.data)
        keyWords_list = jieba.analyse.textrank(data_temp, topK=topK, withWeight=withWeight)
        return keyWords_list

    def tfidf_calculate(self, array=False):                 # ngram_range = (), the minimum length and the maximum length
        self._vectorizer = CountVectorizer()                    # min_df indicates the minimum number of documents a token needs to appear
        self._transformer = TfidfTransformer()                  # max_df indicates the maximum number of documents a token needs to appear
        self.tfidf = self._transformer.fit_transform(self._vectorizer.fit_transform(self.data))
        self._word = self._vectorizer.get_feature_names()   # this function returns the word of the vocabulary in order
        if array:                                               # vocabulary_ returns the count of the word
            return self.tfidf.toarray()
        else:
            return self.tfidf

    def get_preTrained_vector(self):
        return self._vectorizer, self._transformer

    def display(self):
        tfidf = self.tfidf.toarray()
        for i in range(tfidf.shape[0]):
            print('\nthis is the %dth document\n'%i)
            for j in range(tfidf.shape[1]):
                print(self._word[j], tfidf[i][j])

class TaggingAPI(object):
    def __init__(self, model_select, path=None):
        self.model_select = model_select
        if self.model_select == 'stanford':
            self.nlp = StanfordCoreNLP(path, lang='zh')
    
    def PoSTagging(self, data):
        if self.model_select == 'jieba':
            return self._PoSTagging_jieba(data)
        elif self.model_select == 'stanford':
            return self._PoSTagging_stanford(data, path)
        else:
            raise Exception('Choose one model: stanford or jieba ?')
        
    def _PoSTagging_jieba(self, data):      # data should be string, no need to be tokenized
        try:
            assert(type(data) == str)
        except Exception as e:
            raise Exception('data should be string, no need to be tokenized')
        else:
            data = ''.join(data.split(' '))
            return pseg.cut(data)
    
    def _PoSTagging_stanford(self, data):
        try:
            assert(type(data) == str)
        except Exception as e:
            raise Exception('data should be string, no need to be tokenized')
        else:
            data = ''.join(data.split(' '))
            return self.nlp.pos_tag(data)

    def addDict(self, dict_name):       # this is for jieba
        # load own dictionary, if A/B/C, could be AB/C, however, it could not transfer AB/C to A/B/C
        # dict should be such format: word word_frequency pos/entity, split by space, pos/entity should be lowercase 
        if self.model_select == 'jieba':
            print('successfully load %s'%dict_name)
            jieba.load_userdict(dict_name)
        else:
            print('these is no need to load user dictionary in %s mode'%self.model_select)
    
    def EntityTagging(self, data):
        if self.model_select == 'stanford':
            return self._EntityTagging_stanford(data)
        else:
            raise Exception('the %s doesn\'t provide this function'%self.model_select)
    
    def _EntityTagging_stanford(self, data):
        try:
            assert(type(data) == str)
        except Exception as e:
            raise Exception('data should be string, no need to be tokenized')
        else:
            data = ''.join(data.split(' '))
            return self.nlp.ner(data)
