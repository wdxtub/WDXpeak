让 menon 一边看一边改

Here are the places we are not sure about:

+ when will you give us the data for other four expressions
+ source of 3D face data (we need more detailed information)
+ we can't open the links you gave me, can you give us the pdf version of the references
+ what do you mean by saying 'image processing device', an application that can be used in mobile devices?
+ what do you expect to achieve finally
+ Besides the speed-up of the calculation process, what else can we improve
+ what should we focus on our project and the thesis
+ how can we write two theses

### Abstract

Background: In recent years, automatic recognition of facial expressions has been an active research field targeting applications in several different areas such as identifying and diagnosing patients with Attention Deficit Disorder(ADD) and Psychology research. Traditionally, human facial expressions have been studied using either 2D static images or 2D video sequences. The 2D-based analysis is incapable of handing large pose variations. Although 3D modeling techniques have been extensively used for 3D face recognition and 3D face animation, barely any research on 3D facial expression recognition using 3D range data has been reported. A primary factor for preventing such research is the lack of a publicly available 3D facial expression database.

Methods: This paper proposes a novel method for recognizing six basic facial expressions based on the information extracted from the face with PCA and LDA method, using the data from xx database. The database contains a regional distance (scalar) and a vector (three components) for each point on the neutral (or expressionless) face surface.

The expressions were computed at 3D space points tracked on human faces. The approach called Fisher LDA is based on feature classification. A phase-to-phase Hausdorff Distance(HD) was computed at each tracked points using the HD computed between consecutive facial phases. The preprocessing stage consists of selecting tracked points and standardizing the data. After preprocessing, it uses a two-stage method PCA plus LDA to generate sub-sampled feature. Finally it adopts K nearest neighbor classifier to recognize universal facial expressions.

Results: Experimental results show that the method is effective for both dimension reduction and recognition performance. The final result outperforms the results reported in the prior work, which only uses PCA classifier or LDA classifier that yields an average recognition rate of 70% and takes plenty of time on the same database.

The PCA method classified 70% of expressions correctly from our current testcases. This improved to 100% with inclusion of both PCA and LDA method. was congruent with improvements in both sensitivity for classifying expression and efficiency of calculation process. The best average recognition rate of 100% was achieved, which indicated this method was suit for facial expression analysis.

Conclusion: The novelty of the method is to deal with 4D data and accelerate calculation speed, which increases the application range.. The algorithm is simple, fast, easy to implement, experiment results show that recognition performance is good, besides it holds some robustness and generalization.
