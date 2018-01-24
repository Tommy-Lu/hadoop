HADOOP_CMD="/opt/hadoop-2.6.1/bin/hadoop" 
STREAM_JAR_PATH="/opt/hadoop-2.6.1/share/hadoop/tools/lib/hadoop-streaming-2.6.1.jar" 

INPUT_FILE_PATH="/merge_file.txt"
TF_OUTPUT_PATH="/tf_output"
TF_IDF_OUT_PATH="/tf-idf_output"
#Step 1 : Calculate the TF of the words and save the result to /tf_output
$HADOOP_CMD fs -rm -r $TF_OUTPUT_PATH
$HADOOP_CMD jar $STREAM_JAR_PATH \
	-input $INPUT_FILE_PATH \
	-output $TF_OUTPUT_PATH     \
	-mapper "python map.py"  \
	-reducer  "python red_tf.py" \
	-jobconf "mapred.reduce.tasks=1" \
	-jobconf "mapred.job.name=calculate-tf" \
	-file ./map.py  \
	-file ./red_tf.py

#Step 2: Calculate the tf-idf value use the result of step1 and input document 
#Save the value to 
$HADOOP_CMD fs -rm -r $TF_IDF_OUT_PATH
$HADOOP_CMD jar $STREAM_JAR_PATH \
    -input $INPUT_FILE_PATH  \
	-output $TF_IDF_OUT_PATH  \
	-mapper "python map_tf-idf.py map_fun  tf_table"  \
	-reducer "cat" \
	-jobconf "mapred.reduce.tasks=1" \
	-jobconf "mapred.job.name=calculate-tf-idf" \
	-cacheFile "hdfs://master:9000/tf_output/part-00000#tf_table" \
	-file ./map_tf-idf.py




