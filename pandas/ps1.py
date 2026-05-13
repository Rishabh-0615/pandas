# // [10:53 PM, 5/10/2026] RSA New: [cloudera@quickstart HiveQL]$ hdfs dfs -ls /
# // [10:53 PM, 5/10/2026] RSA New: [cloudera@quickstart HiveQL]$ hdfs dfs -mkdir input3/
# // [cloudera@quickstart HiveQL]$ hdfs dfs -ls/
# // [10:54 PM, 5/10/2026] RSA New: [cloudera@quickstart HiveQL]$ hdfs dfs -put /home/cloudera/Desktop/1/logTime.csv input3/
# // [10:54 PM, 5/10/2026] RSA New: [cloudera@quickstart HiveQL]$ hadoop jar /home/cloudera/Desktop/HiveQL/loginduration.jar/ loginD.loginDuration input3/ output3/
# // [10:55 PM, 5/10/2026] RSA New: [cloudera@quickstart HiveQL]$ hdfs dfs -ls output3/
# // [10:55 PM, 5/10/2026] RSA New: [cloudera@quickstart HiveQL]$ hdfs dfs -cat output3/part-r-00000
# // 10.10.10.221	3420
# // [cloudera@quickstart HiveQL]$

package wordcount;

import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;

import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;

import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class WordCount {

    public static class WordMapper
            extends Mapper<Object, Text, Text, IntWritable> {

        private final static IntWritable one =
                new IntWritable(1);

        private Text word = new Text();

        public void map(Object key,
                        Text value,
                        Context context)
                throws IOException, InterruptedException {

            String line = value.toString();

            String[] words = line.split(" ");

            for (String w : words) {

                word.set(w);

                context.write(word, one);
            }
        }
    }

    // Reducer Class
    public static class WordReducer
            extends Reducer<Text, IntWritable,
                            Text, IntWritable> {

        public void reduce(Text key,
                           Iterable<IntWritable> values,
                           Context context)
                throws IOException, InterruptedException {

            int sum = 0;

            for (IntWritable val : values) {
                sum += val.get();
            }

            context.write(key,
                    new IntWritable(sum));
        }
    }

    // Main Method
    public static void main(String[] args)
            throws Exception {

        Configuration conf =
                new Configuration();

        Job job =
                Job.getInstance(conf,
                        "Word Count");

        job.setJarByClass(
                WordCount.class);

        job.setMapperClass(
                WordMapper.class);

        job.setReducerClass(
                WordReducer.class);

        job.setOutputKeyClass(
                Text.class);

        job.setOutputValueClass(
                IntWritable.class);

        FileInputFormat.addInputPath(
                job,
                new Path(args[0]));

        FileOutputFormat.setOutputPath(
                job,
                new Path(args[1]));

        System.exit(
                job.waitForCompletion(true)
                        ? 0 : 1);
    }
}