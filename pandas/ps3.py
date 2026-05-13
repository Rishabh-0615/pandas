# // [10:53 PM, 5/10/2026] RSA New: [cloudera@quickstart HiveQL]$ hdfs dfs -ls /
# // [10:53 PM, 5/10/2026] RSA New: [cloudera@quickstart HiveQL]$ hdfs dfs -mkdir input3/
# // [cloudera@quickstart HiveQL]$ hdfs dfs -ls/
# // [10:54 PM, 5/10/2026] RSA New: [cloudera@quickstart HiveQL]$ hdfs dfs -put /home/cloudera/Desktop/1/logTime.csv input3/
# // [10:54 PM, 5/10/2026] RSA New: [cloudera@quickstart HiveQL]$ hadoop jar /home/cloudera/Desktop/HiveQL/loginduration.jar/ loginD.loginDuration input3/ output3/
# // [10:55 PM, 5/10/2026] RSA New: [cloudera@quickstart HiveQL]$ hdfs dfs -ls output3/
# // [10:55 PM, 5/10/2026] RSA New: [cloudera@quickstart HiveQL]$ hdfs dfs -cat output3/part-r-00000
# // 10.10.10.221	3420
# // [cloudera@quickstart HiveQL]$
package musiclisteners;

import java.io.IOException;
import java.util.HashSet;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;

import org.apache.hadoop.io.Text;

import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;

import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class MusicListeners {

    // =========================
    // Mapper Class
    // =========================

    public static class MusicMapper
            extends Mapper<Object, Text,
            Text, Text> {

        public void map(Object key,
                        Text value,
                        Context context)
                throws IOException,
                InterruptedException {

            try {

                // Read one line
                String line = value.toString();

                // Skip header row
                if(line.startsWith("UserId")) {
                    return;
                }

                // Split CSV
                String[] parts = line.split(",");

                // Check valid columns
                if(parts.length >= 5) {

                    // Dataset format:
                    // UserId, TrackId, Shared, Radio, Skip

                    String user =
                            parts[0].trim();

                    String track =
                            parts[1].trim();

                    String shared =
                            parts[2].trim();

                    // Send:
                    // key = TrackId
                    // value = UserId:Shared

                    context.write(
                            new Text(track),
                            new Text(user
                                    + ":"
                                    + shared));
                }

            } catch(Exception e) {

                // Ignore invalid rows
            }
        }
    }

    // =========================
    // Reducer Class
    // =========================

    public static class MusicReducer
            extends Reducer<Text, Text,
            Text, Text> {

        public void reduce(Text key,
                           Iterable<Text> values,
                           Context context)
                throws IOException,
                InterruptedException {

            // Store unique users
            HashSet<String> users =
                    new HashSet<String>();

            int shareCount = 0;

            for(Text val : values) {

                String[] data =
                        val.toString().split(":");

                // Add user
                users.add(data[0]);

                // Count shares
                if(data[1].equals("1")) {

                    shareCount++;
                }
            }

            context.write(
                    key,
                    new Text(
                            "UniqueListeners="
                                    + users.size()
                                    + " Shares="
                                    + shareCount));
        }
    }

    // =========================
    // Driver Class
    // =========================

    public static void main(String[] args)
            throws Exception {

        Configuration conf =
                new Configuration();

        Job job =
                Job.getInstance(conf,
                        "Music Listeners");

        job.setJarByClass(
                MusicListeners.class);

        job.setMapperClass(
                MusicMapper.class);

        job.setReducerClass(
                MusicReducer.class);

        job.setOutputKeyClass(
                Text.class);

        job.setOutputValueClass(
                Text.class);

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