HADOOP_CMD="/opt/hadoop-2.6.1/bin/hadoop" 
STREAM_JAR_PATH="/opt/hadoop-2.6.1/share/hadoop/tools/lib/hadoop-streaming-2.6.1.jar" 

INPUT_FILE_PATH="/lcs_input.data "
OUTPUT_PATH="/nlp-lcs_output"

$HADOOP_CMD fs -rm -r $OUTPUT_PATH
$HADOOP_CMD jar $STREAM_JAR_PATH \
	-input $INPUT_FILE_PATH \
	-output $OUTPUT_PATH     \
	-mapper "python map.py"  \
	-reducer "cat" \
	-jobconf "mapred.reduce.tasks=1" \
	-jobconf "mapred.job.name=nlp-lcs" \
	-file ./map.py
