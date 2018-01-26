HADOOP_CMD="/opt/hadoop-2.6.1/bin/hadoop" 
STREAM_JAR_PATH="/opt/hadoop-2.6.1/share/hadoop/tools/lib/hadoop-streaming-2.6.1.jar" 

INPUT_FILE_PATH="/music_meta.txt.small"
OUTPUT_PATH="/music_meta_tags"

$HADOOP_CMD fs -rmr $OUTPUT_PATH

$HADOOP_CMD jar $STREAM_JAR_PATH \
	-input $INPUT_FILE_PATH \
	-output $OUTPUT_PATH     \
	-mapper "python map.py"  \
	-reducer  "cat" \
	-jobconf "mapred.reduce.tasks=1" \
	-jobconf "mapred.job.name=music-meta-data_jieba_tags" \
	-file ./map.py  \
	-file ./jieba.tar.gz


