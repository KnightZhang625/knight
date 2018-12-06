# This API is used for saving files with all knids of formats
# If you do not specify the saving path, the file will be saved in current directory automatically
# If you want to save in another directory, just specify the directory name, please create the directory in advance

import os
import pickle
from knight.Info import Info

class UtilsAPI(object):
    def __init__(self):
        self.path = os.path.abspath('')
        information = Info()

    def save_dict(self, filename, dic, path=None):
        if path == None:
            path = self.path
        file = filename.split('.')[0] + '.pickle'
        path = os.path.join(path, file)
        f = open(path, 'wb')
        pickle.dump(dic, f)
        f.close()
        self.display(filename, type(dic), path, True)

    def load_dict(self, filename, path=None):
        if path == None:
            path = self.path
        path = os.path.join(path, filename)
        f = open(path, 'rb')
        dic = pickle.load(f)
        self.display(filename, type(dic), path, False)
        return dic

    def save_list(self, filename, l, path=None):
        if path == None:
            path = self.path
        file = filename.split('.')[0] + '.pickle'
        path = os.path.join(path, file)
        f = open(path, 'wb')
        pickle.dump(l, f)
        f.close()
        self.display(filename, type(l), path, True)

    def load_list(self, filename, path=None):
        if path == None:
            path = self.path
        path = os.path.join(path, filename)
        print(path)
        f = open(path, 'rb')
        l = pickle.load(f)
        self.display(filename, type(l), path, False)
        return l

    def display(self, filename, t, path, save):
        if save:
            print('The "%s" <%s> has been saved in : %s/%s'%(filename, t, os.path.abspath(''), path))
        else:
            print('The "%s" has been loaded'%(filename))










