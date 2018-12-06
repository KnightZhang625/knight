import sys
import jieba.analyse
import jieba.posseg as pseg
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from stanfordcorenlp import StanfordCoreNLP
# from Info import Info

class Word_Feature_API(object):
    def __init__(self, stop_word_path=None, user_dict_path=None):
        '''
            Please set the absolute path
        '''
        self.stop_word_path = stop_word_path
        self.user_dict_path = user_dict_path
        # information = Info()
    
    def keyWords_Extract(self, data_list, topK, select='tfidf', withWeight=False):
        if select == 'tfidf':
            return self._tfidf_Extract(data_list, topK, withWeight)
        elif select == 'textRank':
            return self._textRank_Extract(data_list, topK, withWeight)
    
    def _tfidf_Extract(self, data_list, topK, withWeight):
        '''
            data_list : a list which consists of tokenized strings, the same as below
        '''
        self._load_stopwords()
        data_temp = ' '.join(data_list)     # as for keyword extraction, the data format should be strings, no list
        keyWords_list = jieba.analyse.extract_tags(data_temp, topK=topK, withWeight=withWeight)
        return keyWords_list

    def _textRank_Extract(self, data_list, topK, withWeight=False):
        self._load_stopwords()
        data_temp = ' '.join(data_list)
        keyWords_list = jieba.analyse.textrank(data_temp, topK=topK, withWeight=withWeight)
        return keyWords_list
    
    def tfidf_calculate(self, data_list, array=False):                 # ngram_range = (), the minimum length and the maximum length
        self._vectorizer = CountVectorizer()                    # min_df indicates the minimum number of documents a token needs to appear
        self._transformer = TfidfTransformer()                  # max_df indicates the maximum number of documents a token needs to appear
        self.tfidf = self._transformer.fit_transform(self._vectorizer.fit_transform(data_list))
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
    
    def _load_stopwords(self):
        if self.stop_word_path is not None:
            try:
                jieba.analyse.set_stop_words(self.stop_word_path)
            except FileNotFoundError as e:
                print(e)
                sys.exit()
    
class TaggingAPI(object):
    def __init__(self, model_select, path=None):
        '''
            model_select : [stanford, jieba]
            path : the path where StanfordCoreNLP is saved
        '''
        self.model_select = model_select
        self.path = path
        if self.model_select == 'stanford':
            self.nlp = StanfordCoreNLP(path, lang='zh')
    
    def PoSTagging(self, data):
        if self.model_select == 'jieba':
            return self._PoSTagging_jieba(data)
        elif self.model_select == 'stanford':
            return self._PoSTagging_stanford(data)
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

if __name__ == '__main__':
    data = ['我 毕业 于 谢菲尔德大学', '他 毕业 于 纽约大学', '他 毕业 于 斯坦福大学', '我 在 吃饭']
    # tagging = TaggingAPI('stanford', path='/Users/knight/Work_Code_Server/Stanford_CoreNLP/stanford-corenlp-full-2018-10-05')
    tagging = TaggingAPI('jieba')
    tagging.addDict('dict.txt')
    for d in data:
        results = tagging.PoSTagging(d)
        for re in results:
            print(re)