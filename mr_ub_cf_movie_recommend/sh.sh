HADOOP_CMD="/opt/hadoop-2.6.1/bin/hadoop" 
STREAM_JAR_PATH="/opt/hadoop-2.6.1/share/hadoop/tools/lib/hadoop-streaming-2.6.1.jar" 

#INPUT_FILE_PATH="/testAC.data"
INPUT_FILE_PATH="/rating-2k.dat"

OUTPUT_1_NORMALIZED_PATH="/mr_ub_cf_movie_recommend/1_normalized_data"
OUTPUT_2_GET_SINGEL_SIMILAR_PATH="/mr_ub_cf_movie_recommend/2_get_singel_similar_data"
OUTPUT_3_SUM_SIMILAR_PATH="/mr_ub_cf_movie_recommend/3_sum_similar_data"


#Step 1
$HADOOP_CMD fs -rmr $OUTPUT_1_NORMALIZED_PATH

$HADOOP_CMD jar $STREAM_JAR_PATH \
	-input $INPUT_FILE_PATH \
	-output $OUTPUT_1_NORMALIZED_PATH     \
	-mapper "python 1_normalized_map.py"  \
	-reducer  "python 1_normalized_red.py" \
	-jobconf "mapred.reduce.tasks=1" \
	-jobconf "mapred.job.name=1_normalized_data" \
	-file ./1_normalized_map.py   \
	-file ./1_normalized_red.py 

#Step2 
$HADOOP_CMD fs -rmr $OUTPUT_2_GET_SINGEL_SIMILAR_PATH

$HADOOP_CMD jar $STREAM_JAR_PATH \
	-input $OUTPUT_1_NORMALIZED_PATH \
	-output $OUTPUT_2_GET_SINGEL_SIMILAR_PATH     \
	-mapper "python 2_get_singel_similar_map.py"  \
	-reducer "python 2_get_singel_similar_red.py" \
	-jobconf "mapreduce.reduce.memory.mb=1024" \
	-jobconf "mapred.reduce.tasks=2" \
	-jobconf "mapred.job.name=2_get_singel_similar_data" \
	-file ./2_get_singel_similar_map.py   \
	-file ./2_get_singel_similar_red.py

#Step3
$HADOOP_CMD fs -rmr $OUTPUT_3_SUM_SIMILAR_PATH

$HADOOP_CMD jar $STREAM_JAR_PATH \
	-input $OUTPUT_2_GET_SINGEL_SIMILAR_PATH \
	-output $OUTPUT_3_SUM_SIMILAR_PATH     \
	-mapper "python 3_sum_similar_map.py"  \
	-reducer "python 3_sum_similar_red.py" \
	-jobconf "mapred.reduce.tasks=2" \
	-jobconf "mapred.job.name=3_sum_similar_data" \
	-file ./3_sum_similar_map.py   \
	-file ./3_sum_similar_red.py




