from knight.preprocess import PreprocessAPI

str = '小明硕士毕业于中国科学院计算所，后在哈佛大学深造'
test = PreprocessAPI(str)
print(test.preProcess())