import random
import array
import logging

# Threading tests
import threading

# used for sleep - time.sleep(duration)
import time

# using with threads to try and pull data 
import queue

# for use with the database stuff for the "bank app"
import sqlite3
import bcrypt

space_variable = "-----------------------------------------------"

app_log_file = 'main_log_file'
log_level = logging.DEBUG

logger = logging.getLogger('py_learning_script')
logging.basicConfig(filename=app_log_file,
                    filemode='a',
                    format='%(asctime)s,%(msecs)03d %(name)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=log_level)

logging.info("Running Python Learning Script")