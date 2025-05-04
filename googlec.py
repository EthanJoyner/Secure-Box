import google.cloud.logging
import time
import logging

# Initialize the logging client
client = google.cloud.logging.Client(project='securebox-458721')
client.setup_logging()

# Example function to log sensor data
def log_sensor_data(sensor_reading, sensor_type):
    try:
        # Create a structured log entry
        log_data = {
            'sensor_type': sensor_type,
            'reading': sensor_reading,
            'timestamp': time.time()
        }
        
        # Log the data
        logging.info('Sensor reading', extra={'json_fields': log_data})
        
    except Exception as e:
        logging.error(f"Failed to log sensor data: {str(e)}")

# Example usage
# log_sensor_data(23.5, "temperature")
