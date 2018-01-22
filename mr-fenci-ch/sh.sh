HADOOP_CMD="/opt/hadoop-2.6.1/bin/hadoop" 
STREAM_JAR_PATH="/opt/hadoop-2.6.1/share/hadoop/tools/lib/hadoop-streaming-2.6.1.jar" 

INPUT_FILE_PATH="/fenci-test.txt"
OUTPUT_PATH="/fenci-output"

$HADOOP_CMD fs -rmr $OUTPUT_PATH

$HADOOP_CMD jar $STREAM_JAR_PATH \
	-input $INPUT_FILE_PATH \
	-output $OUTPUT_PATH     \
	-mapper "python map.py"  \
	-reducer  "python red.py" \
	-jobconf "mapred.reduce.tasks=2" \
	-jobconf "mapred.job.name=chinese-fenci-word-count" \
	-file ./map.py  \
	-file ./red.py  \
	-file ./jieba.tar.gz


