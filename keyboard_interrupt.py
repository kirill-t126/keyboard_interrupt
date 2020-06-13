import logging
from datetime import datetime
import time

attempts_number = 3
time_period = 5
assert time_period is int or float

logging.basicConfig(format='%(message)s', level = logging.DEBUG)

while True:
    try:
        current_time = datetime.strftime(datetime.now(), "%H:%M:%S")
        logging.info(f"Current time: {current_time}")
        time.sleep(time_period)
    except KeyboardInterrupt:
        attempts_number -= 1
        logging.warning(f"Attempts left: {attempts_number}")
        if attempts_number == 0:
            logging.warning("Are you sure want to exit? (Y/N)")
            exit_word = input('')
            if exit_word == "Y" or exit_word =="y":
                break
            else:
                attempts_number = 1
                continue
logging.info("Exit")