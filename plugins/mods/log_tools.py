# plugins/mods/log_tools.py
# plugins/mods/log_tools.py
import os
import logging
import csv
from datetime import datetime

# Ensure the log directory exists
log_dir = 'plugins/logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Path to the log file
log_file = os.path.join(log_dir, 'cli_logs.csv')

# Set up logging
def setup_logger(level=logging.DEBUG):
    """
    Set up a logger that logs to a CSV file.
    Uses the module's name dynamically for the logger name.
    """
    # Get the name of the current module (i.e., the script that is calling this function)
    module_name = __name__.split('.')[-1]  # This gives just the module name, not the full path
    logger = logging.getLogger(module_name)
    logger.setLevel(level)
    
    # Create a formatter with ISO format for date and time
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%dT%H:%M')
    
    # File handler to write logs to a CSV file
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    
    # Add the file handler to the logger
    logger.addHandler(file_handler)

    # Ensure the CSV header is written if the file is empty
    if os.stat(log_file).st_size == 0:
        with open(log_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['timestamp', 'level', 'module', 'message'])
    
    return logger

# Log to CSV function (write directly to CSV format)
def log_to_csv(level, module, message):
    with open(log_file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M')
        writer.writerow([timestamp, level, module, message])
