import asyncio
import serial_asyncio
import google.cloud.logging
import logging
import time
import sys

client = google.cloud.logging.Client(project='securebox-458721')
logger = client.logger('test-logger')

async def read_serial():
    reader, _ = await serial_asyncio.open_serial_connection(url='COM10', baudrate=9600)
    print("Serial connection established. Reading data...")
    try:
        while True:
            line = await reader.readline()
            status = line.decode().strip()
            if (status == "SECURE"):
                logger.log_text(status)
            else :
                logger.log_text(status, severity="ERROR")
    except asyncio.CancelledError:
        print("Serial reading task cancelled.")
    finally:
        print("Closing serial connection.")
        reader.transport.close()

async def main():
    task = asyncio.create_task(read_serial())
    try:
        await asyncio.sleep(3600)  # Run for 1 hour or until manually stopped
    except KeyboardInterrupt:
        print("Interrupted by user.")
    finally:
        task.cancel()
        await task

if __name__ == "__main__":
    asyncio.run(main())