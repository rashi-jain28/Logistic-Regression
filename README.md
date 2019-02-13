# Logistic-Regression

### Execution Steps on DSBA Cluster

1.hdfs dfs -mkdir /user/rjain12/cloud

2.Putting the files on dsba cluster from local. Run below commands in Cloudera local:
	scp /home/cloudera/Desktop/asgn4/linreg.py rjain12@dsba-hadoop.uncc.edu:/users/rjain12/cloud	
	
	Same command is used to put the other 2 input files on dsba cluster
	scp /home/cloudera/Desktop/asgn4/yxlin.csv rjain12@dsba-hadoop.uncc.edu:/users/rjain12/cloud
	scp /home/cloudera/Desktop/asgn4/yxlin2.csv rjain12@dsba-hadoop.uncc.edu:/users/rjain12/cloud
	
3.Go to the folder created on the dsba cluster i.e. cd cloud/

4.Put the files on dsba hdfs :
	hdfs dfs -put yxlin.csv /user/rjain12/cloud
	hdfs dfs -put yxlin2.csv /user/rjain12/cloud
	
5. Execute the code for both the files:
 spark-submit linreg.py /user/rjain12/cloud/yxlin.csv
 spark-submit linreg.py /user/rjain12/cloud/yxlin2.csv






