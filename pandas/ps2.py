# // [10:53 PM, 5/10/2026] RSA New: [cloudera@quickstart HiveQL]$ hdfs dfs -ls /
# // [10:53 PM, 5/10/2026] RSA New: [cloudera@quickstart HiveQL]$ hdfs dfs -mkdir input3/
# // [cloudera@quickstart HiveQL]$ hdfs dfs -ls/
# // [10:54 PM, 5/10/2026] RSA New: [cloudera@quickstart HiveQL]$ hdfs dfs -put /home/cloudera/Desktop/1/logTime.csv input3/
# // [10:54 PM, 5/10/2026] RSA New: [cloudera@quickstart HiveQL]$ hadoop jar /home/cloudera/Desktop/HiveQL/loginduration.jar/ loginD.loginDuration input3/ output3/
# // [10:55 PM, 5/10/2026] RSA New: [cloudera@quickstart HiveQL]$ hdfs dfs -ls output3/
# // [10:55 PM, 5/10/2026] RSA New: [cloudera@quickstart HiveQL]$ hdfs dfs -cat output3/part-r-00000
# // 10.10.10.221	3420
# // [cloudera@quickstart HiveQL]$

package logduration;

import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;

import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;

import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class LogDuration {

    // =========================
    // Mapper Class
    // =========================

    public static class LogMapper
            extends Mapper<Object, Text,
            Text, IntWritable> {

        private Text user = new Text();

        private IntWritable durationWritable =
                new IntWritable();

        public void map(Object key,
                        Text value,
                        Context context)
                throws IOException,
                InterruptedException {

            try {

                // Read one line
                String line = value.toString();

                // Split CSV using comma
                String[] parts = line.split(",");

                // Ensure enough columns exist
                if(parts.length >= 8) {

                    // MAC/User
                    String username = parts[0].trim();

                    // Login time
                    String loginTime =
                            parts[5].trim();

                    // Logout time
                    String logoutTime =
                            parts[7].trim();

                    // Date format
                    SimpleDateFormat sdf =
                            new SimpleDateFormat(
                                    "M/d/yyyy HH:mm");

                    // Convert string to date
                    Date loginDate =
                            sdf.parse(loginTime);

                    Date logoutDate =
                            sdf.parse(logoutTime);

                    // Difference in milliseconds
                    long diff =
                            logoutDate.getTime()
                            - loginDate.getTime();

                    // Convert to minutes
                    int totalMinutes =
                            (int)(diff / (1000 * 60));

                    // Ignore negative values
                    if(totalMinutes >= 0) {

                        user.set(username);

                        durationWritable.set(
                                totalMinutes);

                        context.write(
                                user,
                                durationWritable);
                    }
                }

            } catch(Exception e) {

                // Ignore invalid rows
            }
        }
    }

    // =========================
    // Reducer Class
    // =========================

    public static class LogReducer
            extends Reducer<Text, IntWritable,
            Text, IntWritable> {

        private int maxDuration = 0;

        private String maxUser = "";

        public void reduce(Text key,
                           Iterable<IntWritable> values,
                           Context context)
                throws IOException,
                InterruptedException {

            int sum = 0;

            // Add durations
            for(IntWritable val : values) {

                sum += val.get();
            }

            // Find maximum
            if(sum > maxDuration) {

                maxDuration = sum;

                maxUser = key.toString();
            }
        }

        // Runs after reducer completes
        protected void cleanup(Context context)
                throws IOException,
                InterruptedException {

            context.write(
                    new Text(maxUser),
                    new IntWritable(maxDuration));
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
                        "Login Duration");

        job.setJarByClass(
                LogDuration.class);

        job.setMapperClass(
                LogMapper.class);

        job.setReducerClass(
                LogReducer.class);

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