# 毕业论文

+ TextGrocery
+ Gensim
+ 中文分词
+ word2vec
+ 文本分类
+ 测试集和训练集
+ NLTK 来进行文本分类
+ 语料库
+ 主题模型
+ 推荐系统(需要开始写了)

## Result

Now we have a web-based GUI to present all the notes mapping from specific local folder supporting markdown/pdf/image/math equations. As time limited the knowledge graph and the information management tool is separated from this GUI and work as a command-line-tool.

For text classification, based on LibLinear, we get a precision rate about 79.4% and greatly reduce the amount of computing time compared with naive bayes and svm method. However as the training/testing data is small, it may represent personal interests but can not be applied to predict other language material from the web or other people.

For book recommendation, based on knowledge graph, the recommended items for are highly related to the text itself and can give detailed recommendation reason.

## Conclusion

This is a novel attempt to apply a small part of knowledge graph from the internet for personal information management. Though lots of human labeling efforts are needed, its high accuracy and structured information arranging method can help people turn notes into knowledge. It is a plain-text based system so that it is easy to implement on different platforms to create a complete information management enviroment.
