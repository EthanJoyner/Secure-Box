import google.cloud.logging
import logging
import time
import sys

def test_logging():
    try:
        # 1. Print initial status
        print("Starting logging test...")
        
        # 2. Initialize client with explicit project
        client = google.cloud.logging.Client(project='securebox-458721')
        print("Successfully created logging client")
        
        # 3. Create a custom logger
        logger = client.logger('test-logger')
        print("Created logger object")
        
        # 4. Try different logging methods
        # Method 1: Direct logger
        logger.log_text("Normal log test NORMAL1")
        print("Sent direct log")
        
        # Method 2: Standard logging
        client.setup_logging()
        logging.warning("Standard logging test WARNING2")
        print("Sent standard log")
        
        # # Method 3: Structured logging
        # logger.log_struct({
        #     'message': 'Structured log test',
        #     'timestamp': time.time(),
        #     'severity': 'WARNING'
        # })
        # print("Sent structured log")
        
        # # 5. Force flush
        # logger.force_flush()
        # print("Forced flush of logs")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        print(f"Error type: {type(e)}")
        traceback.print_exc()

if __name__ == "__main__":
    test_logging()
    print("Test complete - check Google Cloud Console")
