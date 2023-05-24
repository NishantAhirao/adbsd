import java.io.BufferedReader;
import java.io.FileReader; 
 
import java.io.IOException;

public class WeatherDataProcessor {
public static void main(String[] args) throws IOException { String filePath = "E:\\TE\\Sem 6\\DS&BDA
LAB\\DSBDAL_Assignment12_TCOB03\\src\\sample_weather.txt";

// Open the file for reading
BufferedReader reader = new BufferedReader(new FileReader(filePath));

// Skip the header line
String line = reader.readLine();

// Initialize the sum and count variables
double sumTemperature = 0.0; double sumDewPoint = 0.0; double sumWindSpeed = 0.0; int count = 0;

// Read each line of the file
while ((line = reader.readLine()) != null) {
// Split the line into fields String[] fields = line.split(",");

// Parse the values
double temperature = Double.parseDouble(fields[1]); double dewPoint = Double.parseDouble(fields[2]); double windSpeed = Double.parseDouble(fields[3]);

// Add the values to the sum variables sumTemperature += temperature;
 
sumDewPoint += dewPoint; sumWindSpeed += windSpeed;

// Increment the count variable count++;
}

// Calculate the averages
double avgTemperature = sumTemperature / count; double avgDewPoint = sumDewPoint / count; double avgWindSpeed = sumWindSpeed / count;

// Print the averages
System.out.println("Average Temperature: " + avgTemperature); System.out.println("Average Dew Point: " + avgDewPoint); System.out.println("Average Wind Speed: " + avgWindSpeed);

// Close the file reader.close();
}
}

