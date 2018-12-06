# this API is used for preprocessing the string

import os
import re
import sys
import jieba
import jieba.analyse
from knight.Info import Info

class PreprocessAPI(object):
    def __init__(self, data):
        self.data = data
        if self._judge():
            jieba.analyse.set_stop_words('stopwords.txt')   # no need to create object for jieba, just set stopwords directly
        else:
            print('Please put the stopwords.txt file in this path')
            sys.exit()
        information = Info()

    def _judge(self):
        # judge whether 'stopwords.txt' exists
        file_lists = os.listdir()
        if 'stopwords.txt' in file_lists:
            return True
        else:
            return False

    def addDict(self, dict_name):
        # load own dictionary, if A/B/C, could be AB/C, however, it could not transfer AB/C to A/B/C
        jieba.load_userdict(dict_name)

    def preProcess(self, cut_all=False, cut_for_search=False, HMM=False, enable=(False, None)):
        '''
            lower, cut, remover punctuation, return list composed of strings
            enable : the first item indicates open multiprocess or not, the second item indicates how many processes
            all parameters will be passed into _tokenize(), in which jieba.cut() will use

        '''
        self.data_list = []
        for sentence in self.data:
            sentence = self._removePunctuation(sentence)
            sentence = self._tokenize(sentence, cut_all, cut_for_search, HMM, enable)
            self.data_list.append(sentence)
        return self.data_list

    def _tokenize(self, sentence, cut_all, cut_for_search, HMM, enable):
        if enable[0]:
            print('use multiprocessing')
            jieba.enable_parallel(enable[1])
        else:
            jieba.disable_parallel()
        if not cut_for_search:
            sentence_temp = ' '.join(jieba.cut(sentence, cut_all, HMM))
            return sentence_temp
        else:
            sentence_temp = ' '.join(jieba.cut_for_search(sentence, HMM))
            return sentence_temp

    def _removePunctuation(self, sentence):
        r_punctuation = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~。（）：＊※，·… 、？！\n👍]+'
        r_emoji = u'[\uD800-\uDBFF][\uDC00-\uDFFF]'
        sentence_temp = sentence.strip()
        sentence_temp = re.sub(r_punctuation, '', sentence_temp)
        sentence_temp = re.sub(r_emoji, '', sentence_temp)
        sentence_temp = re.sub(' ', '', sentence_temp)
        sentence_temp = sentence_temp.lower()
        return sentence_temp