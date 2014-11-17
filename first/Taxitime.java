import java.io.IOException;
import java.util.*;
import java.text.*;

//import au.com.bytecode.opencsv.*;
import com.opencsv.*;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
        
public class Taxitime {
        
    public static class Map extends Mapper<LongWritable,
    Text, Text, IntWritable> {
        @Override
        public void map(LongWritable key, Text value, Context context) throws IOException,
        InterruptedException {
            /*if(key.get()>0) {
                //try{
                    CSVParser parser = new CSVParser();
                    String[] lines = parser.parseLine(value.toString());
                    String dtstr = lines[3].substring(0,10);
                    context.write(new Text(dtstr), new IntWritable(1));
                //} catch (ParseException e) {}
            }
            */
            if (key.get() > 0) {
                try {
                    CSVParser parser = new CSVParser();
                    String[] lines = parser.parseLine(value.toString());
                    
                    SimpleDateFormat formatter =
                    new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
                    Date dt = formatter.parse(lines[5]);
                    formatter.applyPattern("dd-MM-yyyy");
                    
                    String dtstr = formatter.format(dt);
                    context.write(new Text(dtstr), new IntWritable(1));
                } catch (ParseException e) {}
            }
             
        }
    }
        
    public static class Reduce extends Reducer<Text, IntWritable, Text,
    IntWritable> {
        @Override
        public void reduce(Text key, Iterable<IntWritable> values, Context context)
        throws IOException, InterruptedException {
            int count = 0;
            for (IntWritable value : values) {
                count++;
            }
            context.write(key, new IntWritable(count));
        }
    }
        
 public static void main(String[] args) throws Exception {
    //Configuration conf = new Configuration();
        
        //Job job = new Job(conf, "wordcount");
     Job job = new Job();
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);
        
    job.setMapperClass(Map.class);
    job.setReducerClass(Reduce.class);
        
    //job.setInputFormatClass(TextInputFormat.class);
    //job.setOutputFormatClass(TextOutputFormat.class);

    //job.setNumReduceTasks(1);
    job.setJarByClass(Taxitime.class);
        
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    System.exit(job.waitForCompletion(true) ? 0 : 1);
    //job.waitForCompletion(true);
 }
        
}