# Homework 3

Task 0: 用完记得关掉

Task 1:

+ export PATH=$PATH:$HOME/hadoop-2.4.0/bin
+ export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64
+ wget https://cmu.box.com/shared/static/2fwqjutnf8u299sbotkgqamoc7iweawx.gz -O Proj3.tar.gz
+ tar –zxvf Proj3.tar.gz
+ cd Proj3
+ mkdir –p data/tweets10m
+ cd data/tweets10m
+ wget https://cmu.box.com/shared/static/701hqlebgkpek9n9qtcd2vqzt6k98x84.bz2 -O tweets10m.txt.bz2
+ bunzip2 tweets10m.txt.bz2
+ # Split out a small trunk of data
+ mkdir ../tweets1m
+ head -1000000 tweets10m.txt > ../tweets1m/tweets1m.txt
+ ls –l lib/ 
+ ant
+ hadoop jar 18645-proj3-0.1-latest.jar -program ngramcount -n 1 -input data/tweets10m/tweets10m.txt -output data/ngram10m 
+ hadoop jar 18645-proj3-0.1-latest.jar -program hashtagsim -input data/tweets1m/tweets1m.txt -output data/hashtag1m -tmpdir tmp

Task 3:

In local file

+ aws s3 mb s3://dawang.fastcode
+ aws s3 cp 18645-proj3-0.1-latest.jar s3://dawang.fastcode

Test cluster ngramcount

aws emr create-cluster --name "Test cluster ngramcount" --ami-version 3.3.2 --log-uri s3://dawang.log-uri.ngramcount --enable-debugging --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=c1.medium InstanceGroupType=CORE,InstanceCount=4,InstanceType=c1.medium --steps Type=CUSTOM_JAR,Jar=s3://dawang.fastcode/18645-proj3-0.1-latest.jar,Args=["-input","s3://dawang.tweets10m/tweets10m.txt","-output","s3://dawang.output/ngram10m","-program","ngramcount"] --auto-terminate

"ClusterId": "j-3UCGDB2BI4KBP"

这个命令会返回一个CID

# Check cluster status from command line
aws emr describe-cluster --cluster-id $CID
aws emr describe-cluster --cluster-id j-3UCGDB2BI4KBP

aws emr create-cluster --name "Test cluster hashtagsim" --ami-version 3.3.2 --log-uri s3://dawang.log-uri.hashtagsim --enable-debugging --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=c1.medium InstanceGroupType=CORE,InstanceCount=4,InstanceType=c1.medium --steps Type=CUSTOM_JAR,Jar=s3://dawang.fastcode/18645-proj3-0.1-latest.jar,Args=["-input","s3://dawang.tweets1m/tweets1m.txt","-output","s3://dawang.output/hashtag1m","-program","hashtagsim","-tmpdir","tmp"] --auto-terminate

 "ClusterId": "j-3SNCE9K14PV5W"

# Check cluster status from command line
aws emr describe-cluster --cluster-id $CID
aws emr describe-cluster --cluster-id j-3SNCE9K14PV5W
