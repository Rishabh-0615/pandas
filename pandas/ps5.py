# // [10:53 PM, 5/10/2026] RSA New: [cloudera@quickstart HiveQL]$ hdfs dfs -ls /
# // [10:53 PM, 5/10/2026] RSA New: [cloudera@quickstart HiveQL]$ hdfs dfs -mkdir input3/
# // [cloudera@quickstart HiveQL]$ hdfs dfs -ls/
# // [10:54 PM, 5/10/2026] RSA New: [cloudera@quickstart HiveQL]$ hdfs dfs -put /home/cloudera/Desktop/1/logTime.csv input3/
# // [10:54 PM, 5/10/2026] RSA New: [cloudera@quickstart HiveQL]$ hadoop jar /home/cloudera/Desktop/HiveQL/loginduration.jar/ loginD.loginDuration input3/ output3/
# // [10:55 PM, 5/10/2026] RSA New: [cloudera@quickstart HiveQL]$ hdfs dfs -ls output3/
# // [10:55 PM, 5/10/2026] RSA New: [cloudera@quickstart HiveQL]$ hdfs dfs -cat output3/part-r-00000
# // 10.10.10.221	3420
# // [cloudera@quickstart HiveQL]$

package movierating;

import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;

import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;

import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class MovieRating {

    // =========================
    // Mapper Class
    // =========================

    public static class MovieMapper
            extends Mapper<Object, Text,
            Text, DoubleWritable> {

        public void map(Object key,
                        Text value,
                        Context context)
                throws IOException,
                InterruptedException {

            try {

                // Read one line
                String line = value.toString();

                // Skip header row
                if(line.startsWith("userId")) {
                    return;
                }

                // Split CSV
                String[] parts = line.split(",");

                // Dataset:
                // userId,movieId,rating,timestamp

                if(parts.length >= 4) {

                    String movieId =
                            parts[1].trim();

                    double rating =
                            Double.parseDouble(
                                    parts[2].trim());

                    // key = movieId
                    // value = rating

                    context.write(
                            new Text(movieId),
                            new DoubleWritable(
                                    rating));
                }

            } catch(Exception e) {

                // Ignore invalid rows
            }
        }
    }

    // =========================
    // Reducer Class
    // =========================

    public static class MovieReducer
            extends Reducer<Text,
            DoubleWritable,
            Text,
            DoubleWritable> {

        private double maxAverage = 0;

        private String bestMovie = "";

        public void reduce(Text key,
                           Iterable<DoubleWritable> values,
                           Context context)
                throws IOException,
                InterruptedException {

            double sum = 0;

            int count = 0;

            // Calculate total ratings
            for(DoubleWritable val : values) {

                sum += val.get();

                count++;
            }

            // Average rating
            double average =
                    sum / count;

            // Find best rated movie
            if(average > maxAverage) {

                maxAverage = average;

                bestMovie = key.toString();
            }
        }

        // Final output
        protected void cleanup(Context context)
                throws IOException,
                InterruptedException {

            context.write(
                    new Text(bestMovie),
                    new DoubleWritable(
                            maxAverage));
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
                        "Movie Recommendation");

        job.setJarByClass(
                MovieRating.class);

        job.setMapperClass(
                MovieMapper.class);

        job.setReducerClass(
                MovieReducer.class);

        job.setOutputKeyClass(
                Text.class);

        job.setOutputValueClass(
                DoubleWritable.class);

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
