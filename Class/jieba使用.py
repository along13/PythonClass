import jieba
sentence = "他来到了网易杭研大厦"
# 精确模式 描述：最基本的分词模式，将句子切分成最小的词语单元，不存在冗余词语，切分后词语总次数余文章总次数相等。
words = jieba.cut(sentence, cut_all=False)
print( "/ ".join(words))
# 全模式 描述：全模式将句子中所有可能的词语都扫描出来，可能包含一些无意义或重复的词语，有冗余，即在文本中从不同角度分词。
words = jieba.cut(sentence, cut_all=True)
print( "/ ".join(words))
# 搜索引擎模式 描述：在精确模式的基础上进行了进一步的切分，对一些长词接下来再次切分，得到更细粒度的词语。
words = jieba.cut_for_search(sentence)
print( "/ ".join(words))