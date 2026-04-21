# LINE 1: Import the logging module
# Python's built-in logging module for tracking events, errors, and debugging information
import logging

# LINE 3-6: Configure the basic logging settings
# This sets up how logs will be displayed and what level of logs to capture
logging.basicConfig(
    level=logging.INFO,              # Set the minimum log level to capture
    format="%(asctime)s - %(levelname)s - %(message)s"  # Define how logs look
)

# LINE 8: Create a logger instance for this module
# Get a logger with the name of the current module (__name__ = current file name)
logger = logging.getLogger(__name__)