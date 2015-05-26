# Personal Information Management based on Knowledge Graph

Da Wang, A.Prof. Chenying Gao

## Abstract

This paper presents an effective toolkit for personal information management(PIM). The development of this toolkit is based on the idea that new information retrieval methods and natural language processing methods can help people extract useful information when facing the information explosion/chaos/overload. With a automatic and unified information processing pipeline, this toolkit focuses on improving the effectiveness of three main PIM processes: get/retrieve, understand/analyze and connect/organize.

keywords:

## 摘要

关键词：

## Chapter 1 Introduction

### 1.1 Background

With the development of Internet and Information Technology, the problem of Information Explosion has arisen, that is, Rich Data and Poor Information. Nowadays it is easy for almost everyone to get all kinds of data from newspaper, television as well as social networks but the problem is: how can we turn those data into information and transform them into knowledge.

Personal Information Management(PIM) is the focus of many scholars in the area of Personal Knowledge Management(PKM) and it is the process to capture or locate knowledge as defined by Seufert et al.(2003). The data is transformed to information and vice versa in this process and it mainly deals with the past knowledge, as argued by Russell Ackoff (1989). Knowledge conversion is in the form of explicit knowledge (from one media, e.g. hard copy to another media, e.g. electronic copy), and is the combination process as suggested by Nonaka and Takeuchi (1995).

The PIM is the foundation of PKM, where individuals are able to create their own knowledge database for immediate or future use in this process. The required skills / competences in PIM are retrieving, evaluating and organizing, which are the skills playing significant roles in capture / locate knowledge.

As it is, we must answer one of the most important question about PIM, that is, how to arrange the information. The idea of Knowledge Graph is one of the options to be the rules for information management. However, nowadays most techniques used on knowledge graph focus on information retrieval but not for information management. They focus on identifying identities from the web sources and find connections between them. They treat this problem in a large scale and make it impossible to apply it on personal information management. This paper presents a method to build a simplified knowledge graph to finish the information management task such as text classification and information recommendation.

Nowadays the most famous product close to PIM is Evernote, a note application that can be used in almost every platform. But it can only meet the needs of getting/retrieving and arranging information. When it comes to understand and connect the information, it becomes useless as few natural language processing techniques are integrated in it.

So we need a tool to help us understand what our notes are and find connection between our notes as well as the other information in the Internet. That is to say, it is a tool that can figure out what areas we are focusing on and help us arrange those information based on its understanding a.k.a. the Knowledge Graph.

### 1.2 Objectives

The goal of this work is to present an system for a full circle in the fields of personal information management including getting, understanding, connecting and sharing information as well as knowledge. Based on the Knowledge Graph, a note system and a book recommendation system are built in order to test the efficiency and accuracy of the usage of the Knowledge Graph. Also, a web-based user interface and several import/export toolkits are built to help user browse their personal information and collect other information on mobile devices. All the source code in this work are open sourced.

### 1.3 Related Works

As the personal information management system consists of three main parts, that is, Personal Knowledge Management, Natural Language Processing and Recommender System, different works are presented by many scholars.

For personal knowledge management across computer and internet tools and technologies, Ismail and Ahmad [2] suggested four main processes: get/retrieve, understand/analyze, share/ publish, and connect (GUSC). The concepts are based on different reviews by Grundspenkis [3], Jarche [4], [5], Martin [6], Avery et al. [7], Pettenati et al. [8], and Razmerita et al. [9].

The PKM processes consist of four main tasks:

+ Get/Retrieve knowledge: online search, RSS feed, wikipedia, twitter, facebook, etc
+ Understand/Analyze knowledge: automatic summarization, relationship extraction, sentiment analysis, etc
+ Share knowledge: blog, RSS, wiki, twitter, facebook, etc
+ Connect to other Knowledge: similar notes/information, related books, etc

They have such a huge goal and want to build a complete and complex system to cover every part of the PIM/PKM process which makes the whole system too large to use for common user in daily life.

For natural language processing, the main problem is that most works are based on English.   In order to handle Chinese, some extra works are needed such as word segmentation [10]. Also, analyzing text is also an important task. TextRank [11], Automatic Summarization [12], Sentence Extraction [13] and Multi-Document Summarization [14] are some of the useful techniques. Most of them are integrated in powerful NLP toolkit such as NLTK [15].

Knowledge Graph is one of the most advanced and undergoing research fields nowadays, different companies have their own applications based on it, [16] [17] [18]. Also, many knowledge bases are built based on the concepts of ontology: Freebase [19], DBpedia [20], XPLORE [21] and WordNet [22]. For Knowledge Graphs in Chinese language, the most famous works are HowNet [23] and SSCO [24].

There are also many research on recommender system. Google [25] [26], Amazon [27] and Netflix [28] [29] are two of the most famous companies that widely use the recommender system in their product. Most recommender systems are based on the following mechanisms: LFM [30], SVD [31], context-aware recommendation [32], information aggregation [33], top-n recommendation [34] and knowledge-based recommendation [35] [36].

### 1.4 Contribution

In my work, based on Knowledge Graph, I build an effective toolkit for personal information management that can perform information aggregation and find connections between different information in order to help people turn rich data into rich information and knowledge. With the assists of the system, people can focus on the information itself as most of the data is filtered and hidden links between information are revealed.

The system consists of the following components:

+ A directory-based Note System using Markdown syntax powered by flask
+ A book recommendation System finding related books according to user’s notes
+ A personal Knowledge Graph generated from the internet data and user notes
+ Import/Export toolkits for connecting different devices and share in different ways

The novelty of the present work, compared to the previous ones, is that it use the Knowledge Graph to arrange all the information. With this graph data structure, it is more natural to find connection and give out recommendation using the information of current node and neighboring nodes. Also, as the knowledge graph is dynamic, it can learn to understand the user’s habits and be more effective and accurate if the user keeps on using it for some time.

And the philosophy in building the Knowledge Graph is to simulate the structure of knowledge generated by billions of people around the world which can be regarded as a self-organized complex system. No human-defined rules are used in building the knowledge graph so there are no fixed categories in this graph. As it is, it is highly flexible to change from time to time without further modification.

### 1.5 Structure of this Thesis

This thesis is divided into four main chapters.

Chapter 2 describes the basis concepts of knowledge representation and the construction procedure of the knowledge graph. Finally, some rendering result of the knowledge graph are put at the end of this chapter.

Chapter 3 is about the design and implementation of the note system. It contains how I arrange the data and display them in a web-based user interface. Also an introduction about how to extract the features and classifying text according to them will be given as well as how to find the similar notes based on knowledge graph.

Chapter 4 is about the design and implementation of the book recommendation system. The following introduction will be in this part: how to get the book information, how to extract features and attach them to different node in the knowledge graph, and how to build the recommender system based on knowledge graph.

Chapter 5 is the conclusion part which contains the comparison result of the text classification, related note discovery and book recommendation among different methods. The results shows that the method presented in this paper has better performance in finishing these tasks.

Appendix A is a brief user guide in installing and using the system.

## Chapter 2 Knowledge Graph

### 2.1 Introduction

### 2.2 Knowledge Representation

### 2.3 Building Knowledge Graph

### 2.4 Results

## Chapter 3 Note System

### 3.1 Introduction

### 3.2 Data Management

### 3.3 Web UI

### 3.4 Integrated with Knowledge Graph

### 3.5 Applications

## Chapter 4 Recommender System

### 4.1 Introduction

### 4.2 Data Acquisition and Parsing

Scapy

### 4.3 Integrated with Knowledge Graph

### 4.4 Connected to Note System

## Chapter 5 Conclustion

This is a novel attempt to apply a small part of knowledge graph from the internet for personal information management. Though lots of human labeling efforts are needed, its high accuracy and structured information arranging method can help people turn notes into knowledge. It is a plain-text based system so that it is easy to implement on different platforms to create a complete information management environment.

Now we have a web-based GUI to present all the notes mapping from specific local folder supporting markdown/pdf/image/math equations. As time limited the knowledge graph and the information management tool is separated from this GUI and work as a command-line-tool.

For text classification, based on LibLinear, we get a precision rate about 79.4% and greatly reduce the amount of computing time compared with naive bayes and svm method. However as the training/testing data is small, it may represent personal interests but can not be applied to predict other language material from the web or other people.

For book recommendation, based on knowledge graph, the recommended items for are highly related to the text itself and can give detailed recommendation reason.

### 5.1 Comparison on Note System

### 5.2 Comparison on Recommender System

### 5.3 Future Work

## Bibliography

[1] Schmitt, U., 2013. Managing Personal Knowledge to make a Difference, 27th British Academy of Management Conference Proceedings (BAM), Sep 10–12, 2013, Liverpool, UK, 978–0–9549608–6–5.
[2] S. Ismail, M. S. Ahmad, “Emergence of Social Intelligence in Social Network: A Quantitative Analysis for Agent-mediated PKM Processes”, in Proc. of the ICIMu 2011 Conference, Malaysia, 2011.
[3] J. Grundspenkis, “Agent based approach for organization and personal knowledge modelling: Knowledge management perspective”, Journal of Intelligent Manufacturing, vol. 18, 2007, pp 451-457.
[4] H. Jarche, “PKM in 2010”, Life in Perpetual Beta. 2010. [5] H. Jarche, “Sense-Making with PKM”, Life in Perpetual Beta. 2009. [6] J. Martin, “Personal Knowledge Management”, Managing Knowledge:
Case Studies in Innovation. Edmonton: Spotted Cow Press. 2000. [7] S. Avery, R. Brooks, J. Brown, P. Dorsey, M. O’ Connor, “Personal knowledge management: framework for integration and partnerships”, in Proc. of the Association of Small Computer Users in Education Conference, 2001, pp. 29-39. [8] M. C. Pettenati, E. Cigognini, J. Mangione, E. Guerin, “Using social
software for personal knowledge management in formal online learning”, Turkish Online Journal of Distance Education, vol. 8, 2007, pp. 52-65.
[9] L. Razmerita, K. Kirchner, F. Sudzina, “Personal knowledge management: The role of Web 2.0 tools for managing knowledge at individual and organisational levels”, Online Information Review, vol. 33, 2009, pp. 1021-1039.
[10] “Chinese word segmentation as character tagging,” pp. 1–19, May 2003.
[11] “TextRank: Bringing Order into Texts,” pp. 1–8, Mar. 2015.
[12] A. Nenkova, “Automatic Summarization,” FNT in Information Retrieval, vol. 5, no. 2, pp. 103–233, 2011.
[13] “Graph-based Ranking Algorithms for Sentence Extraction, Applied to Text Summarization,” pp. 1–4, Mar. 2015.
[14] J. Goldstein, V. Mittal, J. Carbonell, and M. Kantrowitz, “Multi-Document Summarization By Sentence Extraction,” pp. 1–9, Aug. 2002.
[15] Bird, Steven. "NLTK: the natural language toolkit." Proceedings of the COLING/ACL on Interactive presentation sessions. Association for Computational Linguistics, 2006.
[16] “Ontology Reasoning for the Semantic Web and Its Application to Knowledge Graph,” pp. 1–53, Oct. 2014.
[17] “Building, Maintaining, and Using Knowledge Bases: A Report from the Trenches,” pp. 1–12, Apr. 2013.
[18] “NLP Techniques in Knowledge Graph,” pp. 1–39, Oct. 2013.
[19] Bollacker, Kurt, et al. "Freebase: a collaboratively created graph database for structuring human knowledge." Proceedings of the 2008 ACM SIGMOD international conference on Management of data. ACM, 2008.
[20] Auer, Sören, et al. Dbpedia: A nucleus for a web of open data. Springer Berlin Heidelberg, 2007.
[21] Wang, Zhigang, et al. "XLore: A Large-scale English-Chinese Bilingual Knowledge Graph." International Semantic Web Conference (Posters & Demos). Vol. 1035. 2013.
[22] Miller, George A. "WordNet: a lexical database for English." Communications of the ACM 38.11 (1995): 39-41.
[23] Carpuat, Marine, et al. "Creating a bilingual ontology: A corpus-based approach for aligning WordNet and HowNet." Proceedings of the 1st Global WordNet Conference. 2002.
[24] Hu, Fanghuai, Zhiqing Shao, and Tong Ruan. "Self-supervised chinese ontology learning from online encyclopedias." The Scientific World Journal 2014 (2014).
[25] Das, Abhinandan S., et al. "Google news personalization: scalable online collaborative filtering." Proceedings of the 16th international conference on World Wide Web. ACM, 2007.
[26] Liu, Jiahui, Peter Dolan, and Elin Rønby Pedersen. "Personalized news recommendation based on click behavior." Proceedings of the 15th international conference on Intelligent user interfaces. ACM, 2010.
[27] Sarwar, Badrul, et al. "Item-based collaborative filtering recommendation algorithms." Proceedings of the 10th international conference on World Wide Web. ACM, 2001.
[28] Zhou, Yunhong, et al. "Large-scale parallel collaborative filtering for the netflix prize." Algorithmic Aspects in Information and Management. Springer Berlin Heidelberg, 2008. 337-348.
[29] Salakhutdinov, Ruslan, Andriy Mnih, and Geoffrey Hinton. "Restricted Boltzmann machines for collaborative filtering." Proceedings of the 24th international conference on Machine learning. ACM, 2007.
[30] Koren, Yehuda. "Factorization meets the neighborhood: a multifaceted collaborative filtering model." Proceedings of the 14th ACM SIGKDD international conference on Knowledge discovery and data mining. ACM, 2008.
[31] Koren, Yehuda. "Collaborative filtering with temporal dynamics."Communications of the ACM 53.4 (2010): 89-97.
[32] Adomavicius, Gediminas, and Alexander Tuzhilin. "Context-aware recommender systems." Recommender systems handbook. Springer US, 2011. 217-253.
[33] Garcia-Molina, Hector, Georgia Koutrika, and Aditya Parameswaran. "Information seeking: convergence of search, recommendations, and advertising." Communications of the ACM 54.11 (2011): 121-130.
[34] Cremonesi, Paolo, Yehuda Koren, and Roberto Turrin. "Performance of recommender algorithms on top-n recommendation tasks." Proceedings of the fourth ACM conference on Recommender systems. ACM, 2010.
[35] Trewin, Shari. "Knowledge-based recommender systems." Encyclopedia of Library and Information Science: Volume 69-Supplement 32 (2000): 180.
[36] Liang, Ting-Peng, et al. "A semantic-expansion approach to personalized knowledge recommendation." Decision Support Systems 45.3 (2008): 401-412.
[37]
[38]



[10] Y. G. P. D. Y. Z. Guandong Xu, “SemRec: A Semantic Enhancement Framework for Tag based Recommendation,” pp. 1–6, Jun. 2011.

## Appendix A

## Acknowledgements
