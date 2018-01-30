HADOOP_CMD="/opt/hadoop-2.6.1/bin/hadoop" 
STREAM_JAR_PATH="/opt/hadoop-2.6.1/share/hadoop/tools/lib/hadoop-streaming-2.6.1.jar" 

INPUT_FILE_PATH="/music_meta.txt.small"
OUTPUT_TW_PATH="/get-tags-weight"

OUTPUT_INVERT_PATH="/invert_data"

#Step 1
$HADOOP_CMD fs -rmr $OUTPUT_TW_PATH

$HADOOP_CMD jar $STREAM_JAR_PATH \
	-input $INPUT_FILE_PATH \
	-output $OUTPUT_TW_PATH     \
	-mapper "python map_get_tags_weight.py"  \
	-reducer  "cat" \
	-jobconf "mapred.reduce.tasks=1" \
	-jobconf "mapred.job.name=map-get-tags-weight" \
	-file ./map_get_tags_weight.py  \
	-file ./jieba.tar.gz

#Step2 
$HADOOP_CMD fs -rmr $OUTPUT_INVERT_PATH

$HADOOP_CMD jar $STREAM_JAR_PATH \
	-input $OUTPUT_TW_PATH \
	-output $OUTPUT_INVERT_PATH     \
	-mapper "python map_invert.py"  \
	-reducer "python red_invert.py" \
	-jobconf "mapred.reduce.tasks=1" \
	-jobconf "mapred.job.name=invert-data" \
	-file ./map_invert.py   \
	-file ./red_invert.py




