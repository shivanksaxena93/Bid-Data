// cc MaxTemperatureMapper Mapper for maximum temperature example
// vv MaxTemperatureMapper
import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MaxTemperatureMapper4
  extends Mapper<LongWritable, Text, Text, IntWritable> {

  enum CustomCounters{
      TEMPERATURE_OVER_50,
      MALFORMED_RECORDS
  }

  private static final int MISSING = 9999;
  @Override
  public void map(LongWritable key, Text value, Context context)
      throws IOException, InterruptedException {

    try{
        String line = value.toString();
        String year = line.substring(15, 19);
        int airTemperature;
        if (line.charAt(87) == '+') { // parseInt doesn't like leading plus signs
          airTemperature = Integer.parseInt(line.substring(88, 92));
        } else {
          airTemperature = Integer.parseInt(line.substring(87, 92));
        }
        String quality = line.substring(92, 93);
        if(airTemperature == MISSING){
          context.getCounter(CustomCounters.MALFORMED_RECORDS).increment(1);
        }
        if (airTemperature != MISSING && quality.matches("[01459]"))   {
          if (airTemperature > 500){
             context.getCounter(CustomCounters.TEMPERATURE_OVER_50).increment(1);
          }

          context.write(new Text(year), new IntWritable(airTemperature));
        }
    } catch(Exception e){
      context.getCounter(CustomCounters.MALFORMED_RECORDS).increment(1);
    }

  }
}
